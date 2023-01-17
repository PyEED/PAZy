# PyEED Data Model

PyEED is a Python-encoded data model of an Enzyme Engineering Database. It supports the scalable and reproducible analysis of sequence and structure data of protein families, and makes data and processes findable, accessible, interoperable, and reusable according to the FAIR data principles.

### ProteinSequence

- __name*__
  - Type: string
  - Description: Systematic name of the protein.
- __amino_acid_sequence*__
  - Type: string
  - Description: The amino acid sequence of the protein sequence object.
- __ncbi_id__
  - Type: string
  - Description: Identifier for the NCBI NR database
- __uniprot_id__
  - Type: string
  - Description: Identifier for the UniProt database
- __pdb_id__
  - Type: string
  - Description: Identifier for the PDB database
  - Multiple: True
- __organism_id__
  - Type: [Organism](#Organism)
  - Description: Corresponding organism 
- __domain__
  - Type: [Domain](#Domain)
  - Description: Domain specification
  - Multiple: True
- __annotation__
  - Type: [Annotation](#Annotation)
  - Description: Position-wise annotation of the amino acid sequence
  - Multiple: True
- __substrate__
  - Type: [Substrate](#Substrate)
  - Description: Substrate that protein is active on
  - Multiple: True
- __reference__
  - Type: [Reference](#Reference)
  - Description: Corresponding publication
  - Multiple: True



### Organism

- __scientific_name*__
  - Type: string
  - Description: Systematic name of the organism.
- __ncbi_taxonomy_id__
  - Type: integer
  - Description: NCBI Taxonomy ID to identify the organism

### Domain

- __name*__
  - Type: string
  - Description: Name of the annotated domain
- __start_position*__
  - Type: integer
  - Description: Position in the sequence where the domain starts
- __end_position*__
  - Type: integer
  - Description: Position in the sequence where the domain ends

  
### Annotation

- __start_position*__
  - Type: integer
  - Description: Start position of the annotation. A single start position without an end corresponds to a single amino acid
- __end_position__
  - Type: integer
  - Description: Optional end position if the annoation contains more than a single amino acid.
- __function*__
  - Type: string
  - Description: Function that is found in the annotated amino acid or sub-sequence

### DNASequence

- __protein_sequence_id*__
  - Type: [ProteinSequence](#proteinsequence)
  - Description: Reference to the corresponding protein sequence to which this DNA sequence translates 


### Substrate

- __substrate*__
  - Type: string
  - Description: Name of substrate
- __source__
  - Type: string
  - Description: Fossil-fuel or renewable resource based polymer
- __abbreviation*__
  - Type: string
  - Description: Abbreviation of substrate


### Reference

- __author*__
  - Type: string
  - Description: First author of publication 
- __year__
  - Type: integer
  - Description: Year of publication
- __doi__
  - Type: string
  - Description: DOI of publication