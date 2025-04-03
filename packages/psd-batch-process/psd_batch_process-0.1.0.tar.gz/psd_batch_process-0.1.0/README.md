# PSD Batch Process

A Python tool for batch updating text layers in Adobe Photoshop files using CSV data.

## Features

- Batch update text layers in multiple PSD files
- CSV-driven updates with flexible column mapping
- Automatic text layer detection and matching
- Comprehensive error handling and logging
- Support for multiple character encodings

## Installation

```bash
pip install psd-batch-process
```

## Usage

### Command Line

```bash
psd-batch-process path/to/your/data.csv
```

### Python API

```python
from psd_batch_process import PsdBatchProcessor

processor = PsdBatchProcessor()
processor.process_csv("path/to/your/data.csv")
```

## CSV Format

Your CSV file should contain:
- A `PhotoshopFile` column with paths to PSD files
- Additional columns matching the names of text layers you want to update

Example:
```csv
PhotoshopFile,Name,Cost,Effect
path/to/card1.psd,Card Name,5,Card Effect Text
```

## Requirements

- Windows OS
- Adobe Photoshop installed
- Python 3.7 or higher

## Development

To set up the development environment:

```bash
git clone https://github.com/yourusername/psd-batch-process
cd psd-batch-process
pip install -e .
pip install -r requirements-dev.txt
```

To run tests:

```bash
pytest tests/
```

## License

MIT License
