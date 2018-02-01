# SNAP-IT: Spliced Neoantigen Pipeline for Immunotherapy #

SNAP-IT is used to annotate exon-level splicing events detected in large RNA-sequencing datasets and identify splicing-derived candidates for immunotherapy. Rather than describing known antigens, SNAP-IT is optimized to efficiently process enormous amounts of data to uncover new immunotherapeutic targets. Candidates are topologically annotated for localization of the cassette exon to the extracellular domain such that the epitope is targetable by antibodies.


Requirements
------------

1. Install Python 3.x

2. Add Python to $PATH environment variable

3. Run setup.py to automatically install dependencies


Installation
------------

Install the SNAP-IT package from PyPI with command:

```shell
pip3 install snapit -–user
```

or download the source code from github and decompress the package.


Usage
-----

### Input ###

The input file for SNAP-IT is the output file from rMATS-turbo, which can be downloaded from:

http://rnaseq-mats.sourceforge.net/

#### Input file format: ####

Each row represents a single splicing event.

Each column represents information about the splicing event.


##### Columns #####

Column Name | Value
--- | ---
AC | Ensembl gene ID as [ENSG#]  
GeneName | gene symbol as [HGNC Symbol]  
chr | chromosome number as [chr#] 
strand | forward or reverse strand as [+] or [-]
exonStart | cassette exon start position as [#]
exonEnd | cassette exon end position as [#]
upstreamES | upstream exon start position as [#]
upstreamEE | upstream exon end position as [#]
downstreamES | downstream exon start position as [#]
downstreamEE | downstream exon end position as [#]
Sample 1 | PSI (percent spliced in) value as [#]
Sample 2 | PSI (percent spliced in) value as [#]
Sample 3 | PSI (percent spliced in) value as [#]
...  | PSI (percent spliced in) value as [#]
Sample n | PSI (percent spliced in) value as [#]


Example:

AC | GeneName | chr | strand | exonStart | exonEnd | upstreamES | upstreamEE | downstreamES | downstreamEE | SRR1919599 | SRR1919600 | SRR1919601 | SRR1919602 | SRR1919603 | SRR1919604 | G20502.22Rv1.2 | G20506.DU_145.2 | G27214.PC3.1 | G28030.MDA_PCa_2b.1 | G28033.LNCaP_clone_FGC.1 | G41666.VCaP.5 | Constitutive.AD1 | Constitutive.AD2 | Constitutive.AD3 | Constitutive.CA | Inducible.7106ICA_off | Inducible.7106ICA_on | Inducible.7242ICA_off | Inducible.7242ICA_on | Inducible.7600ICA_off | Inducible.7600ICA_on | WT_BS9139 | WT_BS9155 | WT_BS9237
:---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---:
ENSG00000000003.14_2 | TSPAN6 | chrX | - | 99885755 | 99885863 | 99882105 | 99884983 | 99887481 | 99887565 | 0.9662 | 0.957 | 0.9582 | 0.9507 | 0.975 | 0.9444 | 0.8904 | 0.964 | 0.9856 | 1 | 1 | 0.9897 | 0.9847 | 0.9882 | 0.9649 | 0.9565 | 0.9954 | 0.9531 | 0.9952 | 0.9401 | 0.9812 | 0.9754 | 0.9071 | 0.9734 | 0.9617 |
| ENSG00000000419.12_2 | DPM1 | chr20 | - | 49557401 | 49557470 | 49552684 | 49552799 | 49558567 | 49558663 | 0.9579 | 0.9589 | 0.936 | 0.9639 | 0.9392 | 0.9369 | 0.9354 | 0.9637 | 0.9392 | 0.9258 | 0.9471 | 0.9609 | 0.9553 | 0.9645 | 0.9325 | 0.9493 | 0.966 | 0.9347 | 0.9366 | 0.9459 | 0.965 | 0.941 | 0.9633 | 0.9676 | 0.9623

