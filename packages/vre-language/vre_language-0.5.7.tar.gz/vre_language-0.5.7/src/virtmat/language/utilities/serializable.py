"""serialization/deserialization code"""
import typing
from dataclasses import dataclass
from json import JSONEncoder
from itertools import islice
from functools import cached_property
import numpy
import pandas
import pint_pandas
from fireworks.utilities.fw_serializers import FWSerializable
from fireworks.utilities.fw_serializers import serialize_fw
from fireworks.utilities.fw_serializers import recursive_serialize
from fireworks.utilities.fw_serializers import recursive_deserialize
from fireworks.utilities.fw_serializers import recursive_dict, load_object
from fireworks.utilities.fw_utilities import get_fw_logger
from virtmat.language.utilities import ioops, amml, chemistry
from .errors import RuntimeTypeError
from .units import ureg
from .lists import list_flatten

pint_pandas.pint_array.DEFAULT_SUBDTYPE = None

DATA_SCHEMA_VERSION = 7


def versioned_deserialize(func):
    """func must be a *from_dict* method"""
    def decorator(cls, dct):
        assert isinstance(cls, type) and issubclass(cls, FWSerializable)
        assert dct.pop('_fw_name') == getattr(cls, '_fw_name')
        assert isinstance(dct, dict)
        version = dct.pop('_version', None)
        if version == DATA_SCHEMA_VERSION:
            return func(cls, dct)  # current version
        if version is None:  # non-tagged is implicitly version 6, to be deprecated
            return func(cls, dct)
        return getattr(cls, f'from_dict_{version}')(cls, dct)
    return decorator


def versioned_serialize(func):
    """func must be a *to_dict* method"""
    def decorator(*args, **kwargs):
        dct = func(*args, **kwargs)
        dct['_version'] = DATA_SCHEMA_VERSION
        return dct
    return decorator


def get_json_size(obj, max_size):
    """compute JSON size in bytes of a JSON serializable object up to max_size"""
    gen = JSONEncoder().iterencode(obj)
    chunk_size = 1024
    json_size = 0
    next_chunk = len(''.join(islice(gen, chunk_size)).encode())
    while next_chunk and json_size < max_size:
        json_size += next_chunk
        next_chunk = len(''.join(islice(gen, chunk_size)).encode())
    return json_size


@dataclass
class FWDataObject(FWSerializable):
    """top-level FWSerializable dataclass to hold any FWSerializable objects"""
    __value: typing.Any = None
    datastore: dict = None
    filename: str = None
    _fw_name = '{{' + __loader__.name + '.' + __qualname__ + '}}'

    @serialize_fw
    @versioned_serialize
    def to_dict(self):
        f_name = f'{__name__}.{self.__class__.__name__}.to_dict()'
        logger = get_fw_logger(f_name)
        logger.debug('%s: starting', f_name)
        if self.datastore is None:
            logger.debug('%s: data type: %s', f_name, type(self.__value))
            self.__value = recursive_dict(self.__value)
            if ioops.DATASTORE_CONFIG['type'] is not None:
                b_thres = ioops.DATASTORE_CONFIG['inline-threshold']
                b_size = get_json_size(self.__value, b_thres)
                logger.debug('%s: data size [B]: %s', f_name, b_size)
                logger.debug('%s: inline-threshold [B]: %s', f_name, b_thres)
                if b_size > b_thres:
                    logger.info('%s: inline data limit exceeded: %s', f_name, b_size)
                    self.datastore, self.filename = ioops.offload_data(self.__value)
                    assert self.datastore['type'] is not None
                    logger.info('%s: data offloaded in %s', f_name, self.filename)
                    return {'datastore': self.datastore, 'filename': self.filename}
            self.datastore = {'type': None}
            logger.info('%s: data not offloaded', f_name)
            return {'value': self.__value, 'datastore': self.datastore}
        logger.debug('%s: datastore: %s', f_name, self.datastore)
        if self.datastore['type'] is None:
            return {'value': self.__value, 'datastore': self.datastore}
        logger.debug('%s: data in file: %s', f_name, self.filename)
        return {'datastore': self.datastore, 'filename': self.filename}

    @classmethod
    @versioned_deserialize
    def from_dict(cls, m_dict):
        assert 'datastore' in m_dict and m_dict['datastore'] is not None
        if m_dict['datastore']['type'] is None:
            return cls(m_dict['value'], m_dict['datastore'])
        assert 'filename' in m_dict and m_dict['filename'] is not None
        assert 'value' not in m_dict
        return cls(None, m_dict['datastore'], m_dict['filename'])

    @cached_property
    def value(self):
        """restore the value if datastore is defined, otherwise just return"""
        assert self.datastore is not None
        # value created with from_obj must not be restored, no known use case
        # if self.datastore is None:  # from_obj() sets datastore to None
        #    return self.__value

        def restore_value(val):
            @recursive_deserialize
            def restore_from_dict(_, dct):
                return dct
            return restore_from_dict(None, {'v': val})['v']

        if self.datastore['type'] is None:
            return restore_value(self.__value)
        assert self.filename is not None
        assert self.__value is None
        self.__value = ioops.lade_data(self.datastore, self.filename)
        return restore_value(self.__value)

    @classmethod
    def from_obj(cls, obj):
        """create an instance from a serializable object of any type"""
        return cls(get_serializable(obj))


class FWDataFrame(pandas.DataFrame, FWSerializable):
    """JSON serializable pandas.DataFrame"""
    _fw_name = '{{' + __loader__.name + '.' + __qualname__ + '}}'

    def __init__(self, *args, **kwargs):
        pandas.DataFrame.__init__(self, *args, **kwargs)

    @serialize_fw
    @recursive_serialize
    @versioned_serialize
    def to_dict(self):  # pylint: disable=arguments-differ
        return {'data': [get_serializable(self[c]) for c in self.columns]}

    @classmethod
    @recursive_deserialize
    @versioned_deserialize
    def from_dict(cls, m_dict):  # pylint: disable=arguments-differ
        if len(m_dict['data']) == 0:
            return cls()
        return cls(pandas.concat(m_dict['data'], axis=1))

    def to_base(self):
        """return an instance of the base class"""
        return pandas.DataFrame(self)


class FWSeries(pandas.Series, FWSerializable):
    """JSON serializable pandas.Series"""
    _fw_name = '{{' + __loader__.name + '.' + __qualname__ + '}}'

    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            if len(args[0]) == 0:
                kwargs['dtype'] = 'object'
        elif len(kwargs['data']) == 0:
            kwargs['dtype'] = 'object'
        pandas.Series.__init__(self, *args, **kwargs)

    @serialize_fw
    @recursive_serialize
    @versioned_serialize
    def to_dict(self):  # pylint: disable=arguments-differ
        if not isinstance(self.dtype, pint_pandas.PintType):
            return {'name': self.name, 'data': get_serializable(self.tolist()),
                    'datatype': str(self.dtype)}
        units = [str(x.to_reduced_units().units) for x in self]
        unit = max(((u, units.count(u)) for u in set(units)), key=lambda c: c[1])[0]
        data = [get_serializable(x.to(unit).magnitude) for x in self]
        datatypes = [type(e).__name__ for e in data if e is not None]
        datatype = next(iter(datatypes)) if datatypes else None
        datatype = 'complex' if datatype == 'tuple' else datatype
        return {'name': self.name, 'data': data, 'units': unit, 'datatype': datatype}

    @classmethod
    @recursive_deserialize
    @versioned_deserialize
    def from_dict(cls, m_dict):
        datatype = m_dict['datatype']
        if datatype in ('int', 'float'):
            dtype = pint_pandas.PintType(m_dict.get('units', 'dimensionless'))
            return cls(data=m_dict['data'], name=m_dict['name'], dtype=dtype)
        if datatype == 'complex':
            data = [complex(*e) for e in m_dict['data']]
            dtype = pint_pandas.PintType(m_dict.get('units', 'dimensionless'))
            return cls(data=data, name=m_dict['name'], dtype=dtype)
        return cls(data=m_dict['data'], name=m_dict['name'])


class FWQuantity(FWSerializable, ureg.Quantity):
    """JSON serializable pint.Quantity"""
    _fw_name = '{{' + __loader__.name + '.' + __qualname__ + '}}'

    @serialize_fw
    @recursive_serialize
    @versioned_serialize
    def to_dict(self):
        mag, unit = self.to_tuple()
        return {'data': (get_serializable(mag), unit)}

    @classmethod
    @recursive_deserialize
    @versioned_deserialize
    def from_dict(cls, m_dict):
        assert isinstance(m_dict['data'], (list, tuple))
        mag, unit = m_dict['data']
        if isinstance(mag, (int, float)):
            return super().from_tuple(m_dict['data'])
        if mag is None:
            return super().from_tuple((pandas.NA, unit))
        assert isinstance(mag, (list, tuple))
        return super().from_tuple((complex(*mag), unit))

    @classmethod
    def from_base(cls, obj):
        """return an instance from an instance of the base class"""
        return cls.from_tuple(obj.to_tuple())


class FWBoolArray(numpy.ndarray, FWSerializable):
    """JSON serializable bool numpy.ndarray"""
    _fw_name = '{{' + __loader__.name + '.' + __qualname__ + '}}'

    def __new__(cls, data):
        return numpy.asarray(data).view(cls)

    @serialize_fw
    @recursive_serialize
    @versioned_serialize
    def to_dict(self):
        return {'data': self.tolist()}

    @classmethod
    @recursive_deserialize
    @versioned_deserialize
    def from_dict(cls, m_dict):
        assert isinstance(m_dict['data'], list)
        assert all(isinstance(e, bool) for e in list_flatten(m_dict['data']))
        return cls(m_dict['data'])


class FWStrArray(numpy.ndarray, FWSerializable):
    """JSON serializable str numpy.ndarray"""
    _fw_name = '{{' + __loader__.name + '.' + __qualname__ + '}}'

    def __new__(cls, data):
        return numpy.asarray(data).view(cls)

    @serialize_fw
    @recursive_serialize
    @versioned_serialize
    def to_dict(self):
        return {'data': self.tolist()}

    @classmethod
    @recursive_deserialize
    @versioned_deserialize
    def from_dict(cls, m_dict):
        assert isinstance(m_dict['data'], list)
        assert all(isinstance(e, str) for e in list_flatten(m_dict['data']))
        return cls(m_dict['data'])


class FWNumArray(FWSerializable, ureg.Quantity):
    """JSON serializable numeric array"""
    _fw_name = '{{' + __loader__.name + '.' + __qualname__ + '}}'

    @serialize_fw
    @recursive_serialize
    @versioned_serialize
    def to_dict(self):
        tpl = self.to_tuple()
        return {'data': (tpl[0].tolist(), tpl[1]),
                'dtype': self.magnitude.dtype.name}

    @classmethod
    @recursive_deserialize
    @versioned_deserialize
    def from_dict(cls, m_dict):
        array = numpy.array(m_dict['data'][0], dtype=m_dict['dtype'])
        return super().from_tuple((array, m_dict['data'][1]))

    @classmethod
    def from_base(cls, obj):
        """return an instance from an instance of the base class"""
        return cls.from_tuple(obj.to_tuple())


class FWAMMLStructure(amml.AMMLStructure, FWSerializable):
    """JSON serializable amml.AMMLStructure"""
    _fw_name = '{{' + __loader__.name + '.' + __qualname__ + '}}'

    @serialize_fw
    @recursive_serialize
    @versioned_serialize
    def to_dict(self):
        return {'data': get_serializable(self.tab), 'name': self.name}

    @classmethod
    @recursive_deserialize
    @versioned_deserialize
    def from_dict(cls, m_dict):
        return cls(m_dict['data'], m_dict['name'])

    @classmethod
    def from_base(cls, obj):
        """return an instance from an instance of the base class"""
        return cls(obj.tab, obj.name)


class FWCalculator(amml.Calculator, FWSerializable):
    """JSON serializable amml.Calculator"""
    _fw_name = '{{' + __loader__.name + '.' + __qualname__ + '}}'
    _keys = ['name', 'parameters', 'pinning', 'version', 'task']

    @serialize_fw
    @recursive_serialize
    @versioned_serialize
    def to_dict(self):
        return {k: get_serializable(getattr(self, k)) for k in self._keys}

    @classmethod
    @recursive_deserialize
    @versioned_deserialize
    def from_dict(cls, m_dict):
        return cls(**m_dict)

    @classmethod
    def from_base(cls, obj):
        """return an instance from an instance of the base class"""
        return cls(**{k: getattr(obj, k) for k in cls._keys})


class FWAlgorithm(amml.Algorithm, FWSerializable):
    """JSON serializable amml.Calculator"""
    _fw_name = '{{' + __loader__.name + '.' + __qualname__ + '}}'
    _keys = ['name', 'parameters', 'many_to_one']

    @serialize_fw
    @recursive_serialize
    @versioned_serialize
    def to_dict(self):
        return {k: get_serializable(getattr(self, k)) for k in self._keys}

    @classmethod
    @recursive_deserialize
    @versioned_deserialize
    def from_dict(cls, m_dict):
        return cls(**m_dict)

    @classmethod
    def from_base(cls, obj):
        """return an instance from an instance of the base class"""
        return cls(**{k: getattr(obj, k) for k in cls._keys})


class FWProperty(amml.Property, FWSerializable):
    """JSON serializable amml.Property"""
    _fw_name = '{{' + __loader__.name + '.' + __qualname__ + '}}'
    _keys = ('names', 'structure', 'calculator', 'algorithm', 'constraints', 'results')

    @serialize_fw
    @recursive_serialize
    @versioned_serialize
    def to_dict(self):
        return {k: get_serializable(getattr(self, k)) for k in self._keys}

    @classmethod
    @recursive_deserialize
    @versioned_deserialize
    def from_dict(cls, m_dict):
        return cls(**m_dict)

    @classmethod
    def from_base(cls, obj):
        """return an instance from an instance of the base class"""
        kwargs = {k: getattr(obj, k) for k in cls._keys}
        return cls(**kwargs)


class FWConstraint(amml.Constraint, FWSerializable):
    """JSON serializable amml.Constraint"""
    _fw_name = '{{' + __loader__.name + '.' + __qualname__ + '}}'

    @serialize_fw
    @recursive_serialize
    @versioned_serialize
    def to_dict(self):
        ser_kwargs = {k: get_serializable(v) for k, v in self.kwargs.items()}
        return {'name': self.name, **ser_kwargs}

    @classmethod
    @recursive_deserialize
    @versioned_deserialize
    def from_dict(cls, m_dict):
        return cls(**m_dict)

    @classmethod
    def from_base(cls, obj):
        """return an instance from an instance of the base class"""
        return cls(obj.name, **obj.kwargs)


class FWTrajectory(amml.Trajectory, FWSerializable):
    """JSON serializable amml.Trajectory"""
    _fw_name = '{{' + __loader__.name + '.' + __qualname__ + '}}'
    _keys = ('description', 'structure', 'properties', 'constraints', 'filename')

    @serialize_fw
    @recursive_serialize
    @versioned_serialize
    def to_dict(self):
        return {k: get_serializable(getattr(self, k)) for k in self._keys}

    @classmethod
    @recursive_deserialize
    @versioned_deserialize
    def from_dict(cls, m_dict):
        return cls(**m_dict)

    @classmethod
    def from_base(cls, obj):
        """return an instance from an instance of the base class"""
        kwargs = {k: getattr(obj, k) for k in cls._keys}
        return cls(**kwargs)


class FWChemSpecies(chemistry.ChemSpecies, FWSerializable):
    """JSON serializable chemistry.ChemSpecies"""
    _fw_name = '{{' + __loader__.name + '.' + __qualname__ + '}}'
    _keys = ['name', 'composition', 'props']

    @serialize_fw
    @recursive_serialize
    @versioned_serialize
    def to_dict(self):
        return {k: get_serializable(getattr(self, k)) for k in self._keys}

    @classmethod
    @recursive_deserialize
    @versioned_deserialize
    def from_dict(cls, m_dict):
        return cls(**m_dict)

    @classmethod
    def from_base(cls, obj):
        """return an instance from an instance of the base class"""
        kwargs = {k: getattr(obj, k) for k in cls._keys}
        return cls(**kwargs)


class FWChemReaction(chemistry.ChemReaction, FWSerializable):
    """JSON serializable chemistry.ChemReaction"""
    _fw_name = '{{' + __loader__.name + '.' + __qualname__ + '}}'
    _keys = ['terms', 'props']

    @serialize_fw
    @recursive_serialize
    @versioned_serialize
    def to_dict(self):
        return {k: get_serializable(getattr(self, k)) for k in self._keys}

    @classmethod
    @recursive_deserialize
    @versioned_deserialize
    def from_dict(cls, m_dict):
        return cls(**m_dict)

    @classmethod
    def from_base(cls, obj):
        """return an instance from an instance of the base class"""
        return cls(obj.terms, obj.props)


def get_serializable(obj):
    """convert an arbitrary Python object to a JSON serializable object"""
    if not isinstance(obj, FWSerializable):
        if isinstance(obj, numpy.generic):
            retval = get_serializable(getattr(obj, 'item', lambda: obj)())
        elif isinstance(obj, (bool, int, float, str, type(None))):
            retval = obj
        elif isinstance(obj, (list, tuple)):
            retval = [get_serializable(o) for o in obj]
        elif isinstance(obj, dict):
            retval = {k: get_serializable(v) for k, v in obj.items()}
        elif obj is pandas.NA or obj is numpy.nan:
            retval = None
        elif isinstance(obj, complex):
            retval = (obj.real, obj.imag)
        elif isinstance(obj, ureg.Quantity):
            if isinstance(obj.magnitude, numpy.ndarray):
                retval = FWNumArray.from_base(obj)
            else:
                retval = FWQuantity.from_base(obj)
        elif isinstance(obj, pandas.DataFrame):
            retval = FWDataFrame(obj)
        elif isinstance(obj, pandas.Series):
            retval = FWSeries(obj)
        elif isinstance(obj, numpy.ndarray):
            if obj.dtype.type is numpy.bool_:
                retval = FWBoolArray(obj)
            else:
                assert obj.dtype.type is numpy.str_
                retval = FWStrArray(obj)
        elif isinstance(obj, amml.AMMLStructure):
            retval = FWAMMLStructure.from_base(obj)
        elif isinstance(obj, amml.Calculator):
            retval = FWCalculator.from_base(obj)
        elif isinstance(obj, amml.Algorithm):
            retval = FWAlgorithm.from_base(obj)
        elif isinstance(obj, amml.Property):
            retval = FWProperty.from_base(obj)
        elif isinstance(obj, amml.Constraint):
            retval = FWConstraint.from_base(obj)
        elif isinstance(obj, amml.Trajectory):
            retval = FWTrajectory.from_base(obj)
        elif isinstance(obj, chemistry.ChemSpecies):
            retval = FWChemSpecies.from_base(obj)
        elif isinstance(obj, chemistry.ChemReaction):
            retval = FWChemReaction.from_base(obj)
        else:
            raise TypeError(f'cannot serialize {obj} with type {type(obj)}')
    else:
        retval = obj
    return retval


def tag_serialize(tagtab):
    """allowed types: DataFrame, tuple / list, Quantity, bool, str"""
    assert isinstance(tagtab, pandas.DataFrame)

    def _recursive_serialize(obj):
        if isinstance(obj, pandas.DataFrame):
            out = {}
            for key, val in obj.to_dict(orient='list').items():
                assert isinstance(val, list)
                assert len(val) == 1
                out[key] = _recursive_serialize(val[0])
            return out
        if isinstance(obj, ureg.Quantity):
            return get_serializable(obj).to_dict()
        if isinstance(obj, (bool, str)) or obj is None:
            return obj
        if isinstance(obj, (tuple, list)):
            return [_recursive_serialize(e) for e in obj]
        raise RuntimeTypeError(f'unsupported type for query/tag: {type(obj)}')
    return _recursive_serialize(tagtab)


def tag_deserialize(tagdct):
    """deserialize a tag dict to a DataFrame object"""
    assert isinstance(tagdct, dict)

    def _recursive_deserialize(obj):
        if isinstance(obj, dict):
            if '_fw_name' in obj:
                return load_object(obj)
            dct = {k: [_recursive_deserialize(v)] for k, v in obj.items()}
            return pandas.DataFrame.from_dict(dct)
        if isinstance(obj, (bool, str)) or obj is None:
            return obj
        assert isinstance(obj, (tuple, list))
        return [_recursive_deserialize(e) for e in obj]
    return _recursive_deserialize(tagdct)
