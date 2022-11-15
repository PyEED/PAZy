import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Domain(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("domainINDEX"),
        xml="@id",
    )

    name: str = Field(..., description="Name of the annotated domain")

    start_position: int = Field(
        ..., description="Position in the sequence where the domain starts"
    )

    end_position: int = Field(
        ..., description="Position in the sequence where the domain ends"
    )

    __repo__: Optional[str] = PrivateAttr(default="git://github.com/PyEED/PAZy.git")

    __commit__: Optional[str] = PrivateAttr(
        default="da1bbbaef7476b8666789f8a8731b6fb932541a0"
    )
