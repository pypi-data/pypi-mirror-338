# pycsv2sqlite

> 🗄️ A fast Python utility for converting CSV/TSV files to SQLite databases with automatic schema detection

[![Python Support](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/github/license/fxyzbtc/pycsv2sqlite.svg)](LICENSE)

## ✨ Features

- 🚀 Fast CSV/TSV import using Pandas
- 📁 Process single files or entire directories
- 🗄️ Automatic SQLite schema creation
- 🔄 Smart type mapping from Pandas to SQLite
- 📊 Detailed import statistics
- 🗜️ Support for gzipped files
- 🎯 Simple CLI interface with Typer

## 📦 Installation

### Using pip
```bash
pip install pycsv2sqlite
```

### Using uv (Recommended)
[uv](https://github.com/astral-sh/uv) is a blazing-fast Python package installer:

```bash
# Install uv
pip install uv

# Install pycsv2sqlite using uv
uv pip install pycsv2sqlite
```

## 🚀 Quick Start

### Command Line Usage
```bash
# Basic usage
pycsv2sqlite import-data data.csv

# Import TSV file
pycsv2sqlite import-data data.tsv --delimiter="\t"

# Import directory of CSVs
pycsv2sqlite import-data ./data/
```

### Python Module Usage
```bash
python -m pycsv2sqlite import-data [options] INPUT_PATH
```

## 🎛️ Configuration Options

| Option | Description | Default |
|--------|-------------|---------|
| `--delimiter` | Field delimiter in input files | `,` |
| `--no-has-headers` | Files don't have headers | `False` |
| `--db-file` | Output SQLite database name | `YYYYMMDD_HHMMSS.sqlite3` |

## 🛠️ Development

### Setup Development Environment

1. Clone the repository
```bash
git clone https://github.com/fxyzbtc/pycsv2sqlite.git
cd pycsv2sqlite
```

2. Create and activate virtual environment
```bash
uv venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Unix
```

3. Install development dependencies
```bash
uv pip install -r requirements-dev.txt
```

### Running Tests
```bash
pytest
pytest --cov=pycsv2sqlite tests/
```

### Code Style
```bash
# Format code
black .
# Lint code
ruff check .
# Type checking
mypy .
```

## 📝 Example Output

```sql
SQLite Table Schema for data:
CREATE TABLE "data" (
    "id" INTEGER,
    "name" TEXT,
    "value" REAL,
    "timestamp" TIMESTAMP
)

Statistics:
- Records added to table: 1000
- Total records in table: 1000
- Columns: 4
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- [Pandas](https://github.com/pandas-dev/pandas) for data processing
- [Typer](https://github.com/tiangolo/typer) for the CLI interface
- [SQLite](https://www.sqlite.org/) for database operations

## 📞 Support

- 📫 Report issues on [GitHub Issues](https://github.com/fxyzbtc/pycsv2sqlite/issues)
- 💬 Ask questions in [Discussions](https://github.com/fxyzbtc/pycsv2sqlite/discussions)
- 📚 Read the [documentation](https://github.com/fxyzbtc/pycsv2sqlite/wiki)

---
Made with ❤️ using Python

