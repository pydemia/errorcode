from typing import Union
from enum import Enum, unique
import json

__all__ = [
    "BaseEnum",
    "use_enum_values",
    "values_callable",
]


@unique
class BaseEnum(str, Enum):

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


def use_enum_values(x: Union[Enum, BaseEnum]):
    # (cls._member_map_[name] for name in cls._member_names_)
    return [e.value for e in x]


def values_callable(x: Union[Enum, BaseEnum]):
    # (cls._member_map_[name] for name in cls._member_names_)
    return [e.value for e in x]


class ActionStatus(BaseEnum):
    ADDED = "ADDED"
    MODIFIED = "MODIFIED"
    DELETED = "DELETED"
    ERROR = "ERROR"
