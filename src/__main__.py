from typing import Dict
from yaml import load, Loader
import enum
from .error_code import CodeEnum, ErrorCode, Code
from pydantic import create_model

with open("code.yaml", "r") as f:
    config = load(f, Loader=Loader)
print(config)

# Method 1. Dynamic Enum
DynamicEnum = enum.Enum("DynamicEnum", config)


def config2code(config: Dict):
    return {k: Code(**v) for k, v in config.items()}

def validate_codes(code_enum: ErrorCode, config: Dict):
    # names = code_enum._member_names_
    members = ErrorCode._member_map_  # {'SUCCESS': 1, 'FAIL': -1, 'UNDEFINED_ERROR': 9999}
    config2code(config)

    config.keys()

code_config = create_model("Codes", **config)
code_config = create_model("Codes", **config, __base__=Code)

DynamicEnum = enum.Enum("DynamicEnum", config)
print(DynamicEnum)

# Method 2. Add codes for linting = validation
print(DynamicEnum)
ErrorCode(1)
enum.Enum._convert_("DynamicEnum", config)
ErrorCode("tt", "test")
ErrorCode(3, "test")
ErrorCode((3, "test"))
ErrorCode(config)
# CodeEnum(config)