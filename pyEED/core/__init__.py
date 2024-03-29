from .annotation import Annotation
from .dnasequence import DNASequence
from .domain import Domain
from .organism import Organism
from .proteinsequence import ProteinSequence
from .reference import Reference
from .substrate import Substrate

__doc__ = "PyEED is a Python-encoded data model of an Enzyme Engineering Database. It supports the scalable and reproducible analysis of sequence and structure data of protein families, and makes data and processes findable, accessible, interoperable, and reusable according to the FAIR data principles."

__all__ = [
    "Annotation",
    "DNASequence",
    "Domain",
    "Organism",
    "ProteinSequence",
    "Reference",
    "Substrate",
]
