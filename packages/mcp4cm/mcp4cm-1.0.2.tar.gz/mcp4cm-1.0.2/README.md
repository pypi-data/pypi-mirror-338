# MCP4CM - Model Cleansing Package for Conceptual Models

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive library for cleaning and preprocessing conceptual model datasets, with a focus on UML models.

## Overview

MCP4CM is a Python package designed to facilitate the cleaning, filtering, and analysis of conceptual model datasets. Currently focused on UML models, the library provides tools for:

- Loading and parsing UML model datasets
- Cleaning models by filtering out empty or invalid files
- Detecting and removing duplicate models
- Filtering models based on naming patterns and quality metrics
- Language detection for model content
- Extracting metadata and statistical information from models

## Installation

```bash
pip install mcp4cm
```

## Quick Start

```python
from mcp4cm import load_dataset

# Load a UML model dataset
dataset = load_dataset("modelset", path="path/to/modelset", uml_type="genmymodel")

# Filter empty or invalid files
from mcp4cm import uml_filter_empty_or_invalid_files
filtered_dataset = uml_filter_empty_or_invalid_files(dataset)

# Filter models with generic class patterns
from mcp4cm import uml_filter_classes_by_generic_pattern
filtered_dataset = uml_filter_classes_by_generic_pattern(filtered_dataset)

# Get duplicate models based on hash
from mcp4cm.uml.duplicate_detection import detect_duplicates_by_hash
unique_models, duplicate_groups = detect_duplicates_by_hash(filtered_dataset)
```

## Main Components

### Base Models

- `Model`: Base class for all model objects with common attributes
- `Dataset`: Container class for collections of models
- `DatasetType`: Enum for different dataset types

### UML-Specific Components

- `UMLModel`: Extended model class with UML-specific properties
- `UMLDataset`: Container for UML models with specialized methods

### Data Filtering

MCP4CM provides various filtering methods to clean datasets:

- Filter empty or invalid files
- Filter models without proper names
- Filter models with dummy class names
- Filter models with generic patterns
- Filter by name length or frequency
- Filter models with sequential naming patterns

### Duplicate Detection

- Hash-based duplicate detection
- TF-IDF based near-duplicate detection

### Language Detection

- Detect languages used in model text
- Extract non-English models

## Examples

### Loading and Basic Filtering

```python
from mcp4cm import load_dataset, uml_filter_empty_or_invalid_files, uml_filter_models_without_names

# Load dataset
dataset = load_dataset("modelset", path="path/to/modelset")
print(f"Original dataset size: {len(dataset.models)} models")

# Apply basic filters
filtered_dataset = uml_filter_empty_or_invalid_files(dataset)
filtered_dataset = uml_filter_models_without_names(filtered_dataset)
print(f"Filtered dataset size: {len(filtered_dataset.models)} models")
```

### Analyzing Name Statistics

```python
from mcp4cm.uml.data_extraction import get_word_counts_from_dataset, get_name_length_distribution

# Get word frequency statistics
most_common_names = get_word_counts_from_dataset(dataset, plt_fig=True)

# Get name length distribution
name_lengths = get_name_length_distribution(dataset, plt_fig=True)
```

### Detecting and Removing Duplicates

```python
from mcp4cm.uml.duplicate_detection import detect_duplicates_by_hash, tfidf_near_duplicate_detector

# Hash-based duplicates
unique_models, duplicate_groups = detect_duplicates_by_hash(dataset, inplace=True)

# Near-duplicates using TF-IDF
unique_models, near_duplicate_groups = tfidf_near_duplicate_detector(dataset, threshold=0.85, inplace=True)
```

## Documentation

Each module and function includes detailed documentation and usage examples. For more information on specific functions, please refer to the docstrings in the code.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Authors

- Andjela Djelic - [andjela.djelic@tuwien.ac.at](mailto:andjela.djelic@tuwien.ac.at)
- Syed Juned Ali - [syed.juned.ali@tuwien.ac.at](mailto:syed.juned.ali@tuwien.ac.at)

## Citation

If you use MCP4CM in your research, please cite:

```
@software{mcp4cm2025,
  author = {Djelic, Andjela and Ali, Syed Juned},
  title = {MCP4CM: Model Cleansing Package for Conceptual Models},
  url = {https://github.com/borkdominik/model-cleansing},
  version = {1.0.1},
  year = {2025}
}
```