# Homework Project

This is a Python project for handling banking operations.

## Features

- Masking of bank card numbers
- Masking of account numbers
- Easily configurable for future updates
- Filtering and sorting of transactions based on their state and date

## Functions

### 1. `filter_by_state`

This function filters a list of dictionaries and returns only those entries whose `state` key matches a specified value.

#### Signature:
```python
filter_by_state(data: List[Dict], state: str = 'EXECUTED') -> List[Dict]
```

#### Installation

To install dependencies, run:

```bash
poetry install
```
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
│   ├── mask/               # Masking module
│   └── processing.py       # Operations processing
├── test/                   # Tests
│   ├── test_masks.py
│   ├── test_processing.py
│   └── test_widget.py
├── pyproject.toml          # Project configuration
└── README.md               # This file
