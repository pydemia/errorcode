from yaml import load, Loader
import enum

with open("code.yaml", "r") as f:
    config = load(f, Loader=Loader)
print(config)

# Method 1. Dynamic Enum
DynamicEnum = enum.Enum('DynamicEnum', config)
print(DynamicEnum)

# Method 2. Add codes for linting