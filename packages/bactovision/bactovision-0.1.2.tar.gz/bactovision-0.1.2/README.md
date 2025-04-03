# BactoVision
## A jupyter widget for annotating and visualizing bacterial growth data

[![Documentation](https://img.shields.io/badge/docs-mkdocs-blue)](https://StarostinV.github.io/bactovision/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![PyPI version](https://badge.fury.io/py/bactovision.svg)](https://badge.fury.io/py/bactovision)
[![Tests](https://github.com/StarostinV/bactovision/actions/workflows/test.yml/badge.svg)](https://github.com/StarostinV/bactovision/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/StarostinV/bactovision/branch/main/graph/badge.svg)](https://codecov.io/gh/StarostinV/bactovision)


<p align="center">
  <img src="docs/images/bactovision-logo.png" width="300" alt="BactoVision">
</p>


Bactovision provides a widget for jupyter notebook for fast semi-automated annotation of bacterial growth images. It is used in the following paper:

_Tyrosine auxotrophy shapes Staphylococcus aureus nasal colonization and interactions with commensal communities_ L. Camus et al. 2025 (submitted)


## Installation

Use pip to install the package:

```bash
pip install bactovision
```

or install from source:

```bash
git clone git@github.com:StarostinV/bactovision.git
cd bactovision
pip install .
```

## Documentation

Please see the full documentation [here](https://StarostinV.github.io/bactovision/).

## Basic usage

Start a jupyter notebook:

```bash
jupyter notebook
```

In the notebook, create a widget:

```python
from bactovision import BactoWidget

# Create a widget with an image
widget = BactoWidget('path/to/image.png')

# Display the widget
widget
```

<p align="center">
  <img src="docs/images/widget-cut.png" width="700" alt="BactoVision">
</p>


To get the mask and the metrics after the annotation is completed, run:

```python
annotation_mask = widget.get_annotation_mask()
metrics = widget.get_metrics()
```
