from .enums import BaseEnum
import pydantic

from pydantic import BaseModel, Field


class Code(BaseModel):
    code: int = Field(ge=-1, le=9999, multiple_of=1)
    message: str = Field(default="NotImplementedError")



