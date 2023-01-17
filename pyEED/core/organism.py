import sdRDM

from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Organism(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("organismINDEX"),
        xml="@id",
    )

    ncbi_taxonomy_id: Optional[int] = Field(
        description="NCBI Taxonomy ID to identify the organism", default=None
    )

    scientific_name: str = Field(..., description="Systematic name of the organism.")

    __repo__: Optional[str] = PrivateAttr(default="git://github.com/PyEED/PAZy.git")

    __commit__: Optional[str] = PrivateAttr(
        default="80098c279c240bde2b6713b7880b8627c1aad571"
    )
