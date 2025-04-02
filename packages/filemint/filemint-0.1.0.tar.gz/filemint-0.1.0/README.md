# FileMint

A Python utility for generating test files in various formats. FileMint makes it easy to create test datasets for development, testing, and demonstrations.

## Features

- Generate structured CSV files with consistent columns
- Generate unstructured text files with random content
- Generate binary files of specified sizes
- Generate intentionally malformed CSV files for testing error handling
- Command-line interface for easy file generation

## Installation

```bash
pip install filemint
```

## Usage

### Command Line

Generate test files using the command-line interface:

```bash
# Generate default set of test files (10 of each type)
filemint

# Specify output directory
filemint --output-dir my_test_files

# Specify number of each file type
filemint --csv 5 --txt 10 --bin 3 --invalid 2
```

### Python API

```python
from filemint.generators import generate_test_files

# Generate test files with default settings
files = generate_test_files(output_dir="test_files")

# Customize the number of each file type
files = generate_test_files(
    output_dir="test_files",
    num_csv=5,
    num_txt=10,
    num_binary=3,
    num_invalid=2
)

# Generate individual files
from filemint.generators import generate_csv, generate_txt, generate_binary, generate_invalid_csv

# Generate a CSV file with 20 rows
csv_file = generate_csv("output_dir", "data.csv", num_rows=20)

# Generate a text file with 50 lines
text_file = generate_txt("output_dir", "notes.txt", num_lines=50)

# Generate a 1MB binary file
binary_file = generate_binary("output_dir", "data.bin", size_in_kb=1024)

# Generate an invalid CSV file with 15 rows
invalid_file = generate_invalid_csv("output_dir", "bad_data.csv", num_rows=15)
```

## Development

### Setup

1. Clone the repository
2. Create and activate a virtual environment
3. Install development dependencies

```bash
git clone https://github.com/yourusername/filemint.git
cd filemint
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e ".[dev]"
```

### Testing

Run tests using pytest:

```bash
pytest
```

## License

This project is licensed under the MIT License - see the LICENSE file for details. 