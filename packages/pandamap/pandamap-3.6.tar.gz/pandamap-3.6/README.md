# PandaMap: A Python package for visualizing protein-ligand interactions with 2D ligand structure representation. 

**P**rotein **AND** lig**A**nd interaction **MAP**per: A Python package for visualizing protein-ligand interactions with 2D ligand structure representation

<p align="center">
  <img src="https://raw.githubusercontent.com/pritampanda15/PandaMap/main/logo/pandamap-logo.svg" alt="PandaMap Logo" width="400">
</p>

## Overview

PandaMap is a lightweight tool for visualizing protein-ligand interactions from PDB files. It generates intuitive 2D interaction diagrams that display both the ligand structure and its interactions with protein residues.

Key features:
- Multiple structure format support e.g., pdb, mmcif, cif, pdbqt
- Visualization of protein-ligand interactions with minimal dependencies
- 2D representation of ligand structure without requiring RDKit
- Detection of multiple interaction types (hydrogen bonds, π-stacking, hydrophobic)
- Command-line interface for quick analysis
- Python API for integration into computational workflows

## Installation

```bash
pip install pandamap
```

## Dependencies
- dssp #It can be installed externally
```bash
brew install dssp #mac users
sudo apt-get install dssp #linux users
Windows: Download from https://swift.cmbi.umcn.nl/gv/dssp/ 
```
- NumPy
- Matplotlib
- BioPython

## Basic Usage
```bash
usage: pandamap [-h] [--output OUTPUT] [--ligand LIGAND] [--dpi DPI]
                [--title TITLE] [--version] [--report]
                [--report-file REPORT_FILE]
                structure_file


PandaMap: Visualize protein-ligand interactions from structure files

positional arguments:
  structure_file        Path to structure file (PDB, mmCIF/CIF, or PDBQT
                        format)

options:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        Output image file path
  --ligand LIGAND, -l LIGAND
                        Specific ligand residue name to analyze
  --dpi DPI             Image resolution (default: 300 dpi)
  --title TITLE, -t TITLE
                        Custom title for the visualization
  --version, -v         Show version information
  --report, -r          Generate text report
  --report-file REPORT_FILE
                        Output file for the text report (default: based on
                        structure filename)

```

### Command Line Interface

```bash
# Basic usage
pandamap protein_ligand.pdb --output interactions.png
pandamap complex.cif --output cif_interaction.png


# Specify a particular ligand by residue name
pandamap protein_ligand.pdb --ligand LIG

#Add report
pandamap complex.pdb --report-file complex.txt --report  --lig PFL
pandamap 4jmz.pdb --ligand HEM --report-file HEM.txt --report
pandamap 1m17.pdb --ligand AQ4 --report-file 1m17.txt --report
```

### Python API

```python
from pandamap import HybridProtLigMapper

# Initialize with PDB file
mapper = HybridProtLigMapper("protein_ligand.pdb", ligand_resname="LIG")

# Run analysis and generate visualization
output_file = mapper.run_analysis(output_file="interactions.png")

# Or run steps separately
mapper.detect_interactions()
mapper.estimate_solvent_accessibility()
mapper.visualize(output_file="interactions.png")
```
# Using external DSSP (recommended)
mapper = HybridProtLigMapper("protein_ligand.pdb")
mapper.run_analysis(use_dssp=True)

# Using pure Python implementation
mapper.run_analysis(use_dssp=False)
## Example Output

# Generate report

```python
from improved_interaction_detection import ImprovedInteractionDetection

# After you've created and run your mapper
mapper = HybridProtLigMapper(...)
mapper.run_analysis()

# Apply improved filtering as a post-processing step
detector = ImprovedInteractionDetection()
filtered_interactions = detector.refine_interactions(mapper.interactions)

# Generate a report
report = detector.generate_report(
    {
        'hetid': mapper.ligand_residue.resname,
        'chain': mapper.ligand_residue.parent.id,
        'position': mapper.ligand_residue.id[1],
        'longname': mapper.ligand_residue.resname,
        'type': 'LIGAND'
    },
    filtered_interactions,
    "interaction_report.txt"
)
```

![PandaMap](https://raw.githubusercontent.com/pritampanda15/PandaMap/main/test/1els_interactions.png)
![PandaMap](https://raw.githubusercontent.com/pritampanda15/PandaMap/main/test/complex_interactions.png)
![PandaMap](https://raw.githubusercontent.com/pritampanda15/PandaMap/main/test/1m17_interactions.png)

# Text Report
```
=============================================================================
PandaMap Interaction Report
=============================================================================

Ligand: AQ4:A:999
Name: AQ4
Type: LIGAND

------------------------------

Interacting Chains: A
Interacting Residues: 11

------------------------------

Interaction Summary:
  Hydrophobic Interactions: 6
  π-π Stacking: 1
  Carbon-π Interactions: 1
  Donor-π Interactions: 2
  Amide-π Interactions: 1

------------------------------

Hydrophobic Interactions:
  1. LEU764A  -- 3.43Å -- AQ4
  2. LEU820A  -- 3.52Å -- AQ4
  3. LEU694A  -- 3.56Å -- AQ4
  4. MET769A  -- 3.78Å -- AQ4
  5. LEU768A  -- 3.75Å -- AQ4
  6. ALA719A  -- 3.31Å -- AQ4

------------------------------

π-π Stacking:
  1. PHE771A  -- 4.54Å -- AQ4

------------------------------

Carbon-π Interactions:
  1. PHE771A  -- 4.28Å -- AQ4

------------------------------

Donor-π Interactions:
  1. GLU738A  -- 3.81Å -- AQ4
  2. ASP831A  -- 3.11Å -- AQ4

------------------------------

Amide-π Interactions:
  1. GLN767A  -- 3.15Å -- AQ4

=============================================================================
```
## Citation

If you use PandaMap in your research, please cite:

```
Pritam Kumar Panda. (2025). Protein AND ligAnd interaction MAPper: A Python package for visualizing protein-ligand interactions with 2D ligand structure representation. GitHub repository. https://github.com/pritampanda15/PandaMap
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
