import pydantic
from libcanonical.types import Base64

from ._signature import Signature


class SignedJWS(pydantic.BaseModel):
    signatures: list[Signature] = pydantic.Field(
        default=...
    )

    payload: Base64 = pydantic.Field(
        default=...
    )