# Homework Project

This is a Python project for handling banking operations and transaction processing.

## Features

- Masking of bank card numbers
- Masking of account numbers
- Transaction filtering and sorting
- Generator-based data processing
- Function execution logging
- 89% test coverage (see full report below)
- Easily configurable for future updates

## Functions

### 1. `filter_by_state`

Filters transactions by status.

###### Example
```python
from src.processing import filter_by_state
executed_transactions = filter_by_state(transactions, "EXECUTED")
```

### 2. `sort_by_date`

Sorts transactions by date.

###### Example
```python
from src.processing import sort_by_date
sorted_transactions = sort_by_date(transactions, ascending=False)
```

### 3. `process_bank_search`

Searches transactions by description using regular expressions (case insensitive).

```python
from src.processing import process_bank_search
result = process_bank_search(transactions, "перевод|payment")
```

### 4. `process_bank_operations`

Counts operations by specified categories.

```python
from src.processing import process_bank_operations
stats = process_bank_operations(transactions, ["перевод", "вклад"])
```

## Generators Module

New module for efficient processing of transaction data using generators.

### 1. `filter_by_currency`

Filters transactions by currency code (92% coverage).

```python
from src.generators import filter_by_currency

usd_transactions = filter_by_currency(transactions, "USD")
print(next(usd_transactions))
```

### 2. `transaction_descriptions`

Extracts transaction descriptions (100% coverage).

```python
from src.generators import transaction_descriptions

for desc in transaction_descriptions(transactions):
    print(desc)
```

### 3. `card_number_generator`

Generates card numbers (92% coverage).

```python
from src.generators import card_number_generator

for card in card_number_generator(1, 5):
    print(card)  # 0000 0000 0000 0001 to 0000 0000 0000 0005
```

## Decorators Module

### log decorator

Logs function execution details (100% coverage).

```python
from src.decorators import log

@log(filename="operations.log")
def process_data(data):
    return len(data)
```

###### Features:

- Logs success/error cases

- Tracks execution time

- Records input parameters

- Supports both file and console output

- Preserves original function metadata

## Data format support

The system now supports:

- JSON (`operation.json`)
- CSV (`transactions.csv`)
- Excel (`transactions_excel.xlsx`)


```python
from src.utils.file_operators import read_json_file
from src.utils.file_readers import read_csv_file, read_excel_file

json_data = read_json_file("data/operation.json")
csv_data = read_csv_file("data/transactions.csv")
excel_data = read_excel_file("data/transactions_excel.xlsx")
```

## CLI Interface

### The main program provides interactive menu:

- Load transactions (JSON/CSV/Excel)
- Filter by status
- Sort by date
- Search in descriptions 
- Get category statistics 

```bash
python main.py
```

## Test Coverage

Current test coverage: 89%

Detailed coverage by module:
src/__init__.py         79% (missing lines: 23, 28, 33)
src/decorators/        100% (new module)
src/generators/core.py  92% 
src/masks/masks.py      88%
src/processing.py      100%
src/widget.py           87%

To generate coverage report:

```bash
pytest --cov=src --cov-report=term-missing  # Console report
pytest --cov=src --cov-report=html          # HTML report (opens in browser)
open htmlcov/index.html
```

#### Installation

To install dependencies, run:

```bash
poetry install
```


```bash
poetry add pandas-stubs
```

## Development

##### Testing

```bash
pytest -v
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
├── src/
│   ├── processing.py       # Core processing functions
│   ├── masks/              # Masking utilities
│   ├── generators/         # Data generators
│   ├── decorators/         # Function decorators
│   └── utils/              # File operations
├── test/
│   ├── test_processing.py  # Updated with new tests
│   └── ...                 # Other test files
├── pyproject.toml
└── README.md
