import sdRDM

from typing import Optional, Union
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Annotation(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("annotationINDEX"),
        xml="@id",
    )

    start_position: int = Field(
        ...,
        description=(
            "Start position of the annotation. A single start position without an end"
            " corresponds to a single amino acid"
        ),
    )

    function: str = Field(
        ...,
        description=(
            "Function that is found in the annotated amino acid or sub-sequence"
        ),
    )

    end_position: Optional[int] = Field(
        description=(
            "Optional end position if the annoation contains more than a single amino"
            " acid."
        ),
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(default="git://github.com/PyEED/PAZy.git")

    __commit__: Optional[str] = PrivateAttr(
        default="30cee84303c1a827fca1090199237a6ea2be0e08"
    )
