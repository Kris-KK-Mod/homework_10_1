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

##### Installation

To install dependencies, run:

```bash
poetry install
```

###### License
```
This project is licensed under the MIT License.
```