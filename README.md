# PyVAT with Checksums

[![PyPI](https://img.shields.io/pypi/v/pyvat-with-checksums.svg)](https://pypi.org/project/pyvat-with-checksums/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A robust and accurate VAT number validation library for Python.

## Why PyVAT with Checksums?

Most VAT validation libraries check if the string starts with the correct country code and has the correct length. **That is not enough.**

**PyVAT with Checksums** goes deeper to ensure data integrity:

- 🧮 **Real Checksum Validation**: We don't just count digits. We implement the official algorithms defined in the European Commission's [VIES VAT Validation Routines](https://taxation-customs.ec.europa.eu/document/download/d416448b-e055-472d-b0e0-4ffc07a7a407_en) specifications (Modulus 11, Modulus 97, etc.) to verify the number is genuinely valid.
- 🛡️ **Stop Bad Data**: Prevent typos and fake numbers from entering your system. A number can look right but be mathematically impossible—we catch that.
- ⚡ **Zero External Dependencies**: Lightweight and fast, perfect for high-throughput applications.

## Features

- ✅ **Mathematical Verification**: Implements complex checksum algorithms for supported countries.
- 🌐 **Multi-Country Support**: Validates VAT numbers for all EU countries and many others (UK, Switzerland, Norway, Russia, etc.).
- 🔍 **Format Checking**: Validates structure, length, and allowed characters (numeric vs alphanumeric).
- 📦 **Modern Python**: Fully typed and compatible with modern Python versions.

## Installation

```bash
pip install pyvat-with-checksums
```

Or using uv:

```bash
uv add pyvat-with-checksums
```

## Usage

Import the validator and the countries you want to check against.

```python
from pyvat_with_checksums import check_vat, belgium, austria

# 1. Valid VAT number (Belgium)
result = check_vat('BE0411905847', [belgium])
print(result.is_valid)
# Output: True
print(result.country.name)
# Output: 'Belgium'

# 2. Invalid Checksum (Looks like a valid format, but fails math check)
# This would pass a simple regex check, but fails here!
result = check_vat('BE0411905848', [belgium])
print(result.is_valid)
# Output: False

# 3. Check against multiple countries
result = check_vat('ATU12345678', [belgium, austria])
if result.is_valid:
    print(f"Valid VAT for {result.country.name}")
```

## Supported Countries

Supports a wide range of countries, including but not limited to:

- 🇪🇺 **European Union**: Austria, Belgium, Bulgaria, Croatia, Cyprus, Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Ireland, Italy, Latvia, Lithuania, Luxembourg, Malta, Netherlands, Poland, Portugal, Romania, Slovakia, Slovenia, Spain, Sweden.
- 🌍 **Non-EU**: United Kingdom, Switzerland, Norway, Russia, Serbia, Brazil.

## Development

To run tests locally:

```bash
make test
```

To run linting checks:

```bash
make lint
```

### Pre-commit Hooks

To automatically run checks before every commit, install the pre-commit hooks:

```bash
uv run pre-commit install
```

You can also run the hooks manually against all files:

```bash
uv run pre-commit run --all-files
```
