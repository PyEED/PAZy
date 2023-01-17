import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import Optional


@forge_signature
class Reference(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("referenceINDEX"),
        xml="@id",
    )
    author: str = Field(
        ...,
        description="First author of publication",
    )

    year: Optional[int] = Field(
        description="Year of publication",
        default=None,
    )

    doi: Optional[str] = Field(
        description="DOI of publication",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(default="git://github.com/PyEED/PAZy.git")
    __commit__: Optional[str] = PrivateAttr(
        default="80098c279c240bde2b6713b7880b8627c1aad571"
    )
