# Identifying Logic

This is a small project of unit-test based exercises for the 3 _Identifying Logic_ activity blocks:

* Identifying If Statements
* Identifying Loops
* Identifying Functions

## Getting started

Do the standard python pre-amble...

```bash
python -m venv .venv
# you! activate your venv
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Run the tests

```bash
# to run all of the tests
python -m pytest

# to run the tests for one section
python -m pytest tests/test_ifs_1.py
python -m pytest tests/test_ifs_2.py
python -m pytest tests/test_loops_1.py
python -m pytest tests/test_functions_1.py
```

Slicker is the `-k` option:

```bash
python -m pytest -k ifs     # run all if related tests
python -m pytest -k loops_2 # run the 2nd group of loop tests
```

## To add test cases

Each block has 3 problems and 3 sets of unit=tests. The problems
live in the problems and the unit-tests live tests directory and
all are named after the content-block they are for.
