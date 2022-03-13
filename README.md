# Identifying Logic

This is a small project of unit-test based exercises for the 3 _Identifying Logic_ activity blocks:

* Identifying If Statements
* Identifying Loops
* Identifying Functions

## Getting started

Do the standard python pre-amble...

This is not complete at the moment, don't follow it blindly

```bash
python -m venv .venv
activate the venv
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Run the tests

```bash
# to run all of the tests
python -m pytest

# to run the tests for one section
python -m pytest tests/test_ifs.py
python -m pytest tests/test_loops.py
python -m pytest tests/test_functions.py
```

## To add test cases

Each block has 3 problems and 3 sets of unit=tests. The problems
live in the problems and the unit-tests live tests directory and
all are named after the content-block they are for.
