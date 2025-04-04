# Copyright (C) 2023-2025 Cochise Ruhulessin
#
# All rights reserved. No warranty, explicit or implicit, provided. In
# no event shall the author(s) be liable for any claim or damages.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from typing import Any

import pydantic

from libcanonical.types import Base64
from ._jwsheader import JWSHeader


class Signature(pydantic.BaseModel):

    claims: JWSHeader
    protected: Base64 | None = None
    header: dict[str, Any] = {}
    signature: Base64