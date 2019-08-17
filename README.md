PCM4psikit
===========

An input file maker for PCMSolver

## Description

This script makes psi4 input file for PCMSolver.  
User can make input file just selecting several options from prompt.

## Requirements

### For making file

- jinja2
- prompt_toolkit

### For calculation

- psi4
- psikit
- rdkit

## Usage

Input molfile must have 3D coordinations and hydrogens.
```
usage: makeinput4pcm.py [-h] [--filepath FILEPATH] molfile

ex) python makeinput4pcm.py yourfile.mol

positional arguments:
  molfile              molfile for PCM caculation the file must have hydrogen

optional arguments:
  -h, --help           show this help message and exit
  --filepath FILEPATH  path where is input template file default ./
```


## Licence

[BSD]https://opensource.org/licenses/BSD-3-Clause
