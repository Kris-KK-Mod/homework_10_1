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
def process_transaction(amount: float):
    # Transaction processing logic
    return amount * 1.1

# Outputs to file:
# 2023-11-15 14:30:00 | process_transaction ok | Execution time: 0.002s | Result: 110.0 | Inputs: (100.0,), {}
```

###### Features:

- Logs success/error cases

- Tracks execution time

- Records input parameters

- Supports both file and console output

- Preserves original function metadata

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
│   ├── __init__.py         # 79% coverage
│   ├── decorators/         # NEW 100% coverage
│   │   ├── __init__.py
│   │   └── log_decorator.py
│   ├── generators/         # 92% coverage
│   ├── mask/               # 88% coverage
│   └── processing.py       # 100% coverage
├── test/
│   ├── test_decorators.py  # NEW tests
│   ├── test_generators.py
│   ├── test_masks.py
│   ├── test_processing.py
│   └── test_widget.py
├── pyproject.toml
└── README.md
