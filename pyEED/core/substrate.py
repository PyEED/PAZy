import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import Optional


@forge_signature
class Substrate(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("substrateINDEX"),
        xml="@id",
    )
    substrate: str = Field(
        ...,
        description="Name of substrate",
    )

    abbreviation: str = Field(
        ...,
        description="Abbreviation of substrate",
    )

    source: Optional[str] = Field(
        description="Fossil-fuel or renewable resource based polymer",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(default="git://github.com/PyEED/PAZy.git")
    __commit__: Optional[str] = PrivateAttr(
        default="80098c279c240bde2b6713b7880b8627c1aad571"
    )
