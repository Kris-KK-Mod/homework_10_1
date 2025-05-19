# Homework Project

This is a Python project for handling banking operations and transaction processing.

## Features

- Masking of bank card numbers
- Masking of account numbers
- Transaction filtering and sorting
- Generator-based data processing
- Easily configurable for future updates

## Functions

### 1. `filter_by_state`

This function filters a list of dictionaries and returns only those entries whose `state` key matches a specified value.

#### Signature:
```python
filter_by_state(data: List[Dict], state: str = 'EXECUTED') -> List[Dict]
```
###### Example
```python
from src.processing import filter_by_state
executed_transactions = filter_by_state(transactions, "EXECUTED")
```

### 2. `sort_by_date`

Sorts transactions by date in ascending or descending order.

#### Signature:
```python
sort_by_date(data: List[Dict], ascending: bool = True) -> List[Dict]
```

## Generators Module

New module for efficient processing of transaction data using generators.

### 1. `filter_by_currency`

Filters transactions by currency code.

```python
from src.generators import filter_by_currency

usd_transactions = filter_by_currency(transactions, "USD")
print(next(usd_transactions))
```

### 2. `transaction_descriptions`

Extracts transaction descriptions.

```python
from src.generators import transaction_descriptions

for desc in transaction_descriptions(transactions):
    print(desc)
```

### 3. `card_number_generator`

Generates formatted card numbers.

```python
from src.generators import card_number_generator

for card in card_number_generator(1, 5):
    print(card)  # 0000 0000 0000 0001 to 0000 0000 0000 0005
```

#### Installation

To install dependencies, run:

```bash
poetry install
```

## Development

##### Testing

This project uses pytest and pytest-cov for testing and coverage.

```bash
pytest
```
##### Running tests with coverage

```bash
pytest --cov=src --cov-report=html
```
Coverage report will be generated in htmlcov/ directory. Open it in browser:

```bash
open htmlcov/index.html
```

##### Code style check

```bash
flake8 src/ test/
```

##### Type checking

```bash
mypy src/
```

##### Import sorting

```bash
isort
```

##### Code formatting

```bash
black
```

##### License
```
This project is licensed under the MIT License.
```

##### Project Structure

homework/
├── src/                    # Source code
│   ├── __init__.py
│   ├── generators/         # Generator module
│   │   ├── __init__.py
│   │   └── core.py
│   ├── mask/               # Masking module
│   └── processing.py       # Operations processing
├── test/                   # Tests
│   ├── test_generators.py
│   ├── test_masks.py
│   ├── test_processing.py
│   └── test_widget.py
├── pyproject.toml          # Project configuration
└── README.md               # This file
