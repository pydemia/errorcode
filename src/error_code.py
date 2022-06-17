from .enums import BaseEnum
from typing import Union, Iterable
from enum import Enum, unique
import json
import pydantic

from pydantic import BaseModel, Field


__all__ = [
    "Code",
    "CodeEnum",
    "ErrorCode",
]

class Code(BaseModel):
    code: int = Field(ge=-9999, le=1, multiple_of=1)
    message: str = Field(default="NotImplementedError")

    def __init__(self, code, message=None):
        super().__init__(
            code=code
        )
        # if message is None:
            





@unique
class ErrorCode(int, Enum):

    SUCCESS = 1
    FAIL = -1
    UNDEFINED_ERROR = 9999

    def __new__(cls, value):
        if isinstance(value, int):
            obj = int.__new__(cls, value)
            obj._value_ = value
            obj.message = "NotImplementedMsg"
        elif isinstance(value, Iterable):
            num, msg = value
            obj = int.__new__(cls, num)
            obj._value_ = num
            obj.message = msg
        else:
            raise TypeError(f"given value '{value}' is not a valid type.")

        return obj

    # def __call__(cls, config_dict):
    def __call__(cls, val_and_msg, names=None, *, module=None, qualname=None, type=None, start=1):
        if names is None:  # simple value lookup
            return cls.__new__(cls, *val_and_msg)
        return cls._create_(
                value,
                names,
                module=module,
                qualname=qualname,
                type=type,
                start=start,
                )
    def _validate_values():
        pass

    def __setattr__(cls, name, value):
        """
        Block attempts to reassign Enum members.

        A simple assignment to the class namespace only changes one of the
        several possible ways to get an Enum member from the Enum class,
        resulting in an inconsistent Enumeration.
        """
        # member_map = cls.__dict__.get('_member_map_', {})
        # if name != "_value_" and name in member_map:
        #     pass
        # else:
        
        # if name in member_map:
        #     raise AttributeError('Cannot reassign members.')
        if cls.__class__.__name__ == "ErrorCode":
            super().__setattr__(name, value)
        else:
            raise AttributeError('Cannot assign new member.')

        # member_map = cls.__dict__.get('_member_map_', {})
        # if name in member_map:
        #     super().__setattr__(name, value)
        # else:
        #     raise AttributeError('Cannot assign new member.')

    @staticmethod
    def _check_for_existing_members(class_name, bases):
        for chain in bases:
            for base in chain.__mro__:
                if issubclass(base, Enum) and base._member_names_:
                    raise TypeError(
                            "%s: cannot extend enumeration %r"
                            % (class_name, base.__name__)
                            )
    # def _validate_(cls, class_name, names, *, module=None, qualname=None, type=None, start=1):
    #     member_map = cls.__dict__.get('_member_map_', {})

    # def __call__(cls, value, names=None, *, module=None, qualname=None, type=None, start=1):
    #     """
    #     Either returns an existing member, or creates a new enum class.

    #     This method is used both when an enum class is given a value to match
    #     to an enumeration member (i.e. Color(3)) and for the functional API
    #     (i.e. Color = Enum('Color', names='RED GREEN BLUE')).

    #     When used for the functional API:

    #     `value` will be the name of the new class.

    #     `names` should be either a string of white-space/comma delimited names
    #     (values will start at `start`), or an iterator/mapping of name, value pairs.

    #     `module` should be set to the module this class is being created in;
    #     if it is not set, an attempt to find that module will be made, but if
    #     it fails the class will not be picklable.

    #     `qualname` should be set to the actual location this class can be found
    #     at in its module; by default it is set to the global scope.  If this is
    #     not correct, unpickling will fail in some circumstances.

    #     `type`, if set, will be mixed in as the first base class.
    #     """
    #     if names is None:  # simple value lookup
    #         return cls.__new__(cls, value)
    #     # otherwise, functional API: we're creating a new Enum type
    #     # return cls._create_(
    #     #         value,
    #     #         names,
    #     #         module=module,
    #     #         qualname=qualname,
    #     #         type=type,
    #     #         start=start,
    #     #         )
    #     return cls._check_(
    #         [value],
    #         [message],
    #     )

    # def _check_(cls, values, messages):
    #     ...



    
    # def _create_(cls, class_name, names, *, module=None, qualname=None, type=None, start=1):
    #     """
    #     Convenience method to create a new Enum class.

    #     `names` can be:

    #     * A string containing member names, separated either with spaces or
    #       commas.  Values are incremented by 1 from `start`.
    #     * An iterable of member names.  Values are incremented by 1 from `start`.
    #     * An iterable of (member name, value) pairs.
    #     * A mapping of member name -> value pairs.
    #     """
    #     metacls = cls.__class__
    #     bases = (cls, ) if type is None else (type, cls)
    #     _, first_enum = cls._get_mixins_(cls, bases)
    #     classdict = metacls.__prepare__(class_name, bases)

    #     # special processing needed for names?
    #     if isinstance(names, str):
    #         names = names.replace(',', ' ').split()
    #     if isinstance(names, (tuple, list)) and names and isinstance(names[0], str):
    #         original_names, names = names, []
    #         last_values = []
    #         for count, name in enumerate(original_names):
    #             value = first_enum._generate_next_value_(name, start, count, last_values[:])
    #             last_values.append(value)
    #             names.append((name, value))

    #     # Here, names is either an iterable of (name, value) or a mapping.
    #     for item in names:
    #         if isinstance(item, str):
    #             member_name, member_value = item, names[item]
    #         else:
    #             member_name, member_value = item
    #         classdict[member_name] = member_value
    #     enum_class = metacls.__new__(metacls, class_name, bases, classdict)

    #     # TODO: replace the frame hack if a blessed way to know the calling
    #     # module is ever developed
    #     if module is None:
    #         try:
    #             module = sys._getframe(2).f_globals['__name__']
    #         except (AttributeError, ValueError, KeyError) as exc:
    #             pass
    #     if module is None:
    #         _make_class_unpicklable(enum_class)
    #     else:
    #         enum_class.__module__ = module
    #     if qualname is not None:
    #         enum_class.__qualname__ = qualname

    #     return enum_class

    @property
    def describe(self):
        # self is the member here
        return self.name, self.value


    def __str__(self) -> str:
        return str(self.value)


    def __repr__(self) -> str:
        return json.dumps(self.value)


    def __eq__(cls, v):
        return cls.value == cls.of(v).value


    @classmethod
    def _missing_(cls, type):
        if isinstance(type, str):
            for item in cls:
                if item.value.lower() == type.lower():
                    return item
        else:
            for item in cls:
                if item.value == type:
                    return item


    def ignore_case(self) -> str:
        return str(self.value).lower()


    @classmethod
    def of(cls, type):
        return cls._missing_(type)

class CodeEnum: ...
# @unique
# class MutableEnum(Enum):

#     def __new__(cls, value):
#         obj = object.__new__(cls)
#         obj._value_ = value
#         return obj

#     # def __new__(cls, value):
#     #     # all enum instances are actually created during class construction
#     #     # without calling this method; this method is called by the metaclass'
#     #     # __call__ (i.e. Color(3) ), and by pickle
#     #     if type(value) is cls:
#     #         # For lookups like Color(Color.RED)
#     #         return value
#     #     # by-value search for a matching enum member
#     #     # see if it's in the reverse mapping (for hashable values)
#     #     try:
#     #         return cls._value2member_map_[value]
#     #     except KeyError:
#     #         # Not found, no need to do long O(n) search
#     #         pass
#     #     except TypeError:
#     #         # not there, now do long search -- O(n) behavior
#     #         for member in cls._member_map_.values():
#     #             if member._value_ == value:
#     #                 return member
#     #     # still not found -- try _missing_ hook
#     #     try:
#     #         exc = None
#     #         result = cls._missing_(value)
#     #     except Exception as e:
#     #         exc = e
#     #         result = None
#     #     try:
#     #         if isinstance(result, cls):
#     #             return result
#     #         else:
#     #             ve_exc = ValueError("%r is not a valid %s" % (value, cls.__name__))
#     #             if result is None and exc is None:
#     #                 raise ve_exc
#     #             elif exc is None:
#     #                 exc = TypeError(
#     #                         'error in %s._missing_: returned %r instead of None or a valid member'
#     #                         % (cls.__name__, result)
#     #                         )
#     #             exc.__context__ = ve_exc
#     #             raise exc
#     #     finally:
#     #         # ensure all variables that could hold an exception are destroyed
#     #         exc = None
#     #         ve_exc = None

#     def __setattr__(cls, name, value):
#         """
#         Block attempts to reassign Enum members.

#         A simple assignment to the class namespace only changes one of the
#         several possible ways to get an Enum member from the Enum class,
#         resulting in an inconsistent Enumeration.
#         """
#         member_map = cls.__dict__.get('_member_map_', {})
#         super().__setattr__(name, value)
#         # if name in member_map:
#         #     raise AttributeError('Cannot reassign members.')
#         # if name in member_map:
#         #     super().__setattr__(name, value)
#         # else:
#         #     raise AttributeError('Cannot assign new member.')

#     SUCCESS = 1
#     FAIL = -1
#     UNDEFINED_ERROR = 9999
