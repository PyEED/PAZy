import sdRDM

from typing import Optional, Union
from typing import List
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .annotation import Annotation
from .domain import Domain
from .organism import Organism
from .reference import Reference
from .substrate import Substrate


@forge_signature
class ProteinSequence(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("proteinsequenceINDEX"),
        xml="@id",
    )

    name: str = Field(..., description="Systematic name of the protein.")

    amino_acid_sequence: str = Field(
        ..., description="The amino acid sequence of the protein sequence object."
    )

    uniprot_id: Optional[str] = Field(
        description="Identifier for the UniProt database", default=None
    )

    pdb_id: List[str] = Field(
        description="Identifier for the PDB database", default_factory=ListPlus
    )

    domain: List[Domain] = Field(
        description="Domain specification", default_factory=ListPlus
    )

    ncbi_id: Optional[str] = Field(
        description="Identifier for the NCBI NR database", default=None
    )

    annotation: List[Annotation] = Field(
        description="Position-wise annotation of the amino acid sequence",
        default_factory=ListPlus,
    )

    organism_id: Optional[Organism] = Field(
        description="Corresponding organism", default=None
    )

    substrate: List[Substrate] = Field(
        description="Substrate that protein is active on", default_factory=ListPlus
    )

    reference: List[Reference] = Field(
        description="Corresponding publication", default_factory=ListPlus
    )

    __repo__: Optional[str] = PrivateAttr(default="git://github.com/PyEED/PAZy.git")

    __commit__: Optional[str] = PrivateAttr(
        default="80098c279c240bde2b6713b7880b8627c1aad571"
    )

    def add_to_domain(
        self,
        name: str,
        start_position: int,
        end_position: int,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Domain' to the attribute 'domain'.

        Args:


            id (str): Unique identifier of the 'Domain' object. Defaults to 'None'.


            name (str): Name of the annotated domain.


            start_position (int): Position in the sequence where the domain starts.


            end_position (int): Position in the sequence where the domain ends.
        """

        params = {
            "name": name,
            "start_position": start_position,
            "end_position": end_position,
        }
        if id is not None:
            params["id"] = id
        domain = [Domain(**params)]
        self.domain = self.domain + domain

    def add_to_annotation(
        self,
        start_position: int,
        function: str,
        end_position: Optional[int] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Annotation' to the attribute 'annotation'.

        Args:


            id (str): Unique identifier of the 'Annotation' object. Defaults to 'None'.


            start_position (int): Start position of the annotation. A single start position without an end corresponds to a single amino acid.


            function (str): Function that is found in the annotated amino acid or sub-sequence.


            end_position (Optional[int]): Optional end position if the annoation contains more than a single amino acid. Defaults to None
        """

        params = {
            "start_position": start_position,
            "function": function,
            "end_position": end_position,
        }
        if id is not None:
            params["id"] = id
        annotation = [Annotation(**params)]
        self.annotation = self.annotation + annotation

    def add_to_substrate(
        self,
        substrate: str,
        abbreviation: str,
        source: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Substrate' to the attribute 'substrate'.

        Args:


            id (str): Unique identifier of the 'Substrate' object. Defaults to 'None'.


            substrate (str): Name of substrate.


            abbreviation (str): Abbreviation of substrate.


            source (Optional[str]): Fossil-fuel or renewable resource based polymer. Defaults to None
        """

        params = {
            "substrate": substrate,
            "abbreviation": abbreviation,
            "source": source,
        }
        if id is not None:
            params["id"] = id
        substrate = [Substrate(**params)]
        self.substrate = self.substrate + substrate

    def add_to_reference(
        self,
        author: str,
        year: Optional[int] = None,
        doi: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Reference' to the attribute 'reference'.

        Args:


            id (str): Unique identifier of the 'Reference' object. Defaults to 'None'.


            author (str): First author of publication.


            year (Optional[int]): Year of publication. Defaults to None


            doi (Optional[str]): DOI of publication. Defaults to None
        """

        params = {"author": author, "year": year, "doi": doi}
        if id is not None:
            params["id"] = id
        reference = [Reference(**params)]
        self.reference = self.reference + reference
