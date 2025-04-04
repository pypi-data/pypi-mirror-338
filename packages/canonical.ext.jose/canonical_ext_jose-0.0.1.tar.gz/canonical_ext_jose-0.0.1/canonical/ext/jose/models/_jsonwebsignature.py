from typing import Union

import pydantic

from canonical.ext.jose.types import JWSCompactEncoded
from ._signedjws import SignedJWS


JSONWebSignatureType = Union[
    JWSCompactEncoded,
    SignedJWS,
]


class JSONWebSignature(pydantic.RootModel[JSONWebSignatureType]):
    pass