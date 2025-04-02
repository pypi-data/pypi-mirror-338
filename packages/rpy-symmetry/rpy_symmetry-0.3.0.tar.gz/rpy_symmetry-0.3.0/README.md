# `Rpy_symmetry`
[![Coverage Status](https://coveralls.io/repos/github/JoranAngevaare/rpy_symmetry/badge.svg)](https://coveralls.io/github/JoranAngevaare/rpy_symmetry)
[![PyPI version shields.io](https://img.shields.io/pypi/v/orpy_symmetry.svg)](https://pypi.python.org/pypi/rpy_symmetry/)
[![Python Versions](https://img.shields.io/pypi/pyversions/rpy_symmetry.svg)](https://pypi.python.org/pypi/rpy_symmetry)
[![PyPI downloads](https://img.shields.io/pypi/dm/rpy_symmetry.svg)](https://pypistats.org/packages/rpy_symmetry)

Light weight bridge from `R` to `python` of the [`symmetry` R-module](https://cran.r-project.org/web/packages/symmetry).

By default, the Symmetry test uses the one from:

    Mira A (1999) Distribution-free test for symmetry based on Bonferroni's measure. J Appl Stat 26(8):959–972. https://doi.org/10.1080/02664769921963


## Installation \ Requirements
`R` needs to be, for example using conda
```
conda install -c conda-forge r-base
```
or mamba:
```
mamba install -c conda-forge r-base
```
Then, one can simply install using pipy:
```
pip install rpy_symmetry
```


The python interface is built on [`rpy2`](https://rpy2.github.io/), which will be automatically be installed as one of the requirements.

## Examples
See example notebook
