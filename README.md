# SNAP-IT: Spliced Neoantigen Pipeline for Immunotherapy #

SNAP-IT is used to annotate exon-level splicing events detected in large RNA-sequencing datasets and identify splicing-derived candidates for immunotherapy. Rather than describing known antigens, SNAP-IT is optimized to efficiently process enormous amounts of data to uncover new immunotherapeutic targets. Candidates are topologically annotated for localization of the cassette exon to the extracellular domain such that the epitope is targetable by antibodies.


Table of Contents
-----------------

- [Requirements](https://github.com/b1tsai/snapit/blob/README-edits/README.md#requirements)
- [Installation](https://github.com/b1tsai/snapit/blob/README-edits/README.md#installation)
- [Usage](https://github.com/b1tsai/snapit/blob/README-edits/README.md#usage) 
  - [Input](https://github.com/b1tsai/snapit/blob/README-edits/README.md#input)
    - [Input file format](https://github.com/b1tsai/snapit/blob/README-edits/README.md#input-file-format)
    - [Columns](https://github.com/b1tsai/snapit/blob/README-edits/README.md#columns)
    - [Example input](https://github.com/b1tsai/snapit/blob/README-edits/README.md#example-input)
  - [Output](https://github.com/b1tsai/snapit/blob/README-edits/README.md#output)
    - [Output file format](https://github.com/b1tsai/snapit/blob/README-edits/README.md#output-file-format)
    - [Columns](https://github.com/b1tsai/snapit/blob/README-edits/README.md#columns-1)
    - [Example output](https://github.com/b1tsai/snapit/blob/README-edits/README.md#example-output)


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

Each _row_ represents a single splicing event.

Each _column_ represents information about the splicing event.


#### Columns: ####

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


#### Example input: ####

AC | GeneName | chr | strand | exonStart | exonEnd | upstreamES | upstreamEE | downstreamES | downstreamEE | SRR1919599 | SRR1919600 | SRR1919601 | SRR1919602 | SRR1919603 | SRR1919604 | G20502.22Rv1.2 | G20506.DU_145.2 | G27214.PC3.1 | G28030.MDA_PCa_2b.1 | G28033.LNCaP_clone_FGC.1 | G41666.VCaP.5 | Constitutive.AD1 | Constitutive.AD2 | Constitutive.AD3 | Constitutive.CA | Inducible.7106ICA_off | Inducible.7106ICA_on | Inducible.7242ICA_off | Inducible.7242ICA_on | Inducible.7600ICA_off | Inducible.7600ICA_on | WT_BS9139 | WT_BS9155 | WT_BS9237
:---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---:
ENSG00000000003.14_2 | TSPAN6 | chrX | - | 99885755 | 99885863 | 99882105 | 99884983 | 99887481 | 99887565 | 0.9662 | 0.957 | 0.9582 | 0.9507 | 0.975 | 0.9444 | 0.8904 | 0.964 | 0.9856 | 1 | 1 | 0.9897 | 0.9847 | 0.9882 | 0.9649 | 0.9565 | 0.9954 | 0.9531 | 0.9952 | 0.9401 | 0.9812 | 0.9754 | 0.9071 | 0.9734 | 0.9617 |
| ENSG00000000419.12_2 | DPM1 | chr20 | - | 49557401 | 49557470 | 49552684 | 49552799 | 49558567 | 49558663 | 0.9579 | 0.9589 | 0.936 | 0.9639 | 0.9392 | 0.9369 | 0.9354 | 0.9637 | 0.9392 | 0.9258 | 0.9471 | 0.9609 | 0.9553 | 0.9645 | 0.9325 | 0.9493 | 0.966 | 0.9347 | 0.9366 | 0.9459 | 0.965 | 0.941 | 0.9633 | 0.9676 | 0.9623

### Output ###

#### Output file format: ####

Each _row_ represents a single splicing event.

Each _column_ represents information about the splicing event.


#### Columns: ####

Column Name | Value
--- | ---
ID | index number of splicing event as [#]
ENSG | Ensembl gene ID as [ENSG#]
GeneName | gene symbol as [HGNC Symbol]
description | description of gene
UniProtKb | UniProtKb protein ID as [Entry]
strand | forward or reverse strand as [+] or [-]
exonCoords | upstream, cassette, and downstream exon coordinates as [chromosome#: upstream exon start position - upstream exon end position, chromosome#: cassette exon start position - cassette exon end position, chromosome#: downstream exon start position - downstream exon end position]
upstreamES | upstream exon start position as [#]
upstreamEE | upstream exon end position as [#]
exonStart | cassette exon start position as [#]
exonEnd | cassette exon end position as [#]
downstreamES | downstream exon start position as [#]
downstreamEE | downstream exon end position as [#]
exonLengths | upstream, cassette, and downstream exon lengths as [# of bases in upstream exon, # of bases in cassette exon, # of bases in downstream exon]
subcell | subcellular localization of protein as [list of subcellular localizations]
exon1FrameShift | [TRUE] if cassette exon length is not divisible by 3, thus will cause a frameshift when included or skipped, [FALSE] if cassette exon length is divisible by 3
topoSrcUP | [TRUE] if protein has topological annotation in UniProtKb, [FALSE] if protein does not have topological annotation in UniProtKb
topoSrcTMHMM | [TRUE] if protein topology can be predicted by TMHMM, [FALSE] if protein topology cannot be predicted by TMHMM
aaPositions | mapped positions of cassette exon start and end residue on protein as [residue # of start position of cassette exon, residue # of end position of cassette exon]
extracellDomains | list of extracellular domains of protein as annotated in UniProtKb as [residue # of start position of extracellular domain, residue # of end position of extracellular domain]
extramemDomains | list of extramembrane domains of protein as predicted by TMHMM as [residue # of start position of extramembrane domain, residue # of end position of extramembrane domain]
alignmentScores | score from 0 to 1 for alignment of upstream and downstream exons to the CDS of gene as [alignment score # of upstream exon, alignment score # of downstream exon]
matchedExonUP | matched exons are mapped to topological annotation from UniProtKb to determine localization of the cassette exon, [Upstream] if upstream exon passed threshold for alignment to gene CDS, [Downstream] if downstream exon passed threshold for alignment to gene CDS, [Both] if both upstream and downstream exons passed threshold for alignment to gene CDS, or [N/A] if neither exons passed threshold for alignment to gene CDS
matchedExonTMHMM | matched exons are mapped to topology predictions from TMHMM to determine localization of the cassette exon, [Upstream] if upstream exon passed threshold for alignment to gene CDS, [Downstream] if downstream exon passed threshold for alignment to gene CDS, [Both] if both upstream and downstream exons passed threshold for alignment to gene CDS, or [N/A] if neither exons passed threshold for alignment to gene CDS
extracellular | [TRUE] if cassette exon has been determined to localize to an extracellular domain of the protein, [FALSE] if cassette exon has not been determined to localize to an extracellular domain of the protein
manual | [TRUE] if splicing event has been flagged for additional manual annotation because SNAP-IT cannot confidently declare the cassette as extracellular, nor can it confidently discard the event is non-extracellular, [FALSE] if splicing event has not been flagged for additional manual annotation
isoforms | lists of refSeq isoforms that have passed the score threshold during NBCI protein BLAST of the neoantigenic region including and excluding the cassette exon as [[refSeq ID \| protein name and species, included exon aligned peptide sequence), e-score], [refSeq ID \| protein name and species, excluded exon aligned peptide sequence), e-score]]
Sample 1 | PSI (percent spliced in) value as [#]
Sample 2 | PSI (percent spliced in) value as [#]
Sample 3 | PSI (percent spliced in) value as [#]
... | PSI (percent spliced in) value as [#]
Sample n | PSI (percent spliced in) value as [#]


#### Example output: ####

ID | ENSG | GeneName | description | UniProtKb | strand | exonCoords | upstreamES | upstreamEE | exonStart | exonEnd | downstreamES | downstreamEE | exonLengths | subcell | exon1FrameShift | topoSrcUP | topoSrcTMHMM | aaPositions | extracellDomains | extramemDomains | alignmentScores | matchedExonUP | matchedExonTMHMM | extracellular | manual | isoforms | Constitutive.AD1 | Constitutive.AD2 | Constitutive.AD3 | Constitutive.CA | G20502.22Rv1.2 | G20506.DU_145.2 | G27214.PC3.1 | G28030.MDA_PCa_2b.1 | G28033.LNCaP_clone_FGC.1 | G41666.VCaP.5 | Inducible.7106ICA_off | Inducible.7106ICA_on | Inducible.7242ICA_off | Inducible.7242ICA_on | Inducible.7600ICA_off | Inducible.7600ICA_on | SRR1919599 | SRR1919600 | SRR1919601 | SRR1919602 | SRR1919603 | SRR1919604 | WT_BS9139 | WT_BS9155 | WT_BS9237
:---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---:
0 | ENSG00000000003 | TSPAN6 | tetraspanin 6 | O43657 | - | ['chrX:99882105-99884983', 'chrX:99885755-99885863', 'chrX:99887481-99887565'] | 99882105 | 99884983 | 99885755 | 99885863 | 99887481 | 99887565 | [2879, 109, 85] | ['Membrane', 'Multi-pass membrane protein'] | FALSE | TRUE | TRUE | ['N/A', 195.0] | [[41, 59], [115, 208]] | [[43, 56], [115, 210]] | [0, 1] | Downstream | Downstream | TRUE | FALSE | [[[('ref\|NP_004606.2\| tetraspanin-7 [Homo sapiens]', 'GISFGVACFQLIGIFLAYCLSRAITNNQYEIV'), 9.17003e-07], [('ref\|NP_001265672.1\| tetraspanin-6 isoform d precursor [Homo sapiens]', 'QLIGIFLAYCLSRAITNNQYEIV'), 9.68798e-09], [('ref\|XP_011529320.1\| PREDICTED: tetraspanin-6 isoform X1 [Homo sapiens]', 'GISFGVACFQLIGIFLAYCLSRAITNNQYEIV'), 5.99408e-16], [('ref\|NP_001265669.1\| tetraspanin-6 isoform b precursor [Homo sapiens]', 'GISFGVACFQLIGIFLAYCLSRAITNNQYEIV'), 5.99408e-16], [('ref\|NP_001265670.1\| tetraspanin-6 isoform b precursor [Homo sapiens]', 'GISFGVACFQLIGIFLAYCLSRAITNNQYEIV'), 5.99408e-16], [('ref\|NP_003261.1\| tetraspanin-6 isoform a [Homo sapiens]', 'GISFGVACFQLIGIFLAYCLSRAITNNQYEIV'), 2.47816e-15]], []] | 0.9847 | 0.9882 | 0.9649 | 0.9565 | 0.8904 | 0.964 | 0.9856 | 1 | 1 | 0.9897 | 0.9954 | 0.9531 | 0.9952 | 0.9401 | 0.9812 | 0.9754 | 0.9662 | 0.957 | 0.9582 | 0.9507 | 0.975 | 0.9444 | 0.9071 | 0.9734	 | 0.9617
13 | ENSG00000000419 | DPM1 | dolichyl-phosphate mannosyltransferase subunit 1, catalytic | O60762 | - | ['chr20:49552684-49552799', 'chr20:49557401-49557470', 'chr20:49558567-49558663'] | 49552684 | 49552799 | 49557401 | 49557470 | 49558567 | 49558663 | [116, 70, 97] | ['Endoplasmic reticulum'] | TRUE | FALSE | FALSE | [225.7, 132.7] | [] | [] | [1, 1] | N/A | N/A | FALSE | FALSE | [] | 0.9553 | 0.9645 | 0.9325 | 0.9493 | 0.9354 | 0.9637 | 0.9392 | 0.9258 | 0.9471 | 0.9609 | 0.966 | 0.9347 | 0.9366 | 0.9459 | 0.965 | 0.941 | 0.9579 | 0.9589 | 0.936 | 0.9639 | 0.9392 | 0.9369 | 0.9633 | 0.9676 | 0.9623

