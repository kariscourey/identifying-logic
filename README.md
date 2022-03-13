# Identifying Logic

This is a small project of unit-test based exercises for the 3 _Identifying Logic_ activity blocks:

* Identifying If Statements
* Identifying Loops
* Identifying Functions





## Getting started

Do the standard python pre-amble...

```bash
python -m venv .venv
...
python -m pip install --upgrade pip
pip install -r requirements.txt

# to run all of the tests
pytest

# I'm sure there is a better solution, but I had to do this
# to get the tests to load the code under test
export PYTHONPATH='.'

# to run the tests for one section
pytest tests/test_ifs.py
pytest tests/test_loops.py
pytest tests/test_functions.py
```

## To add test cases

Each block should have 3 problems and 3 unit tests. The problems
should each have their own file in the problems directory. Each
block currently has a single file in the tests directory which
has the 3 tests for the block. If it works better to have a
separate test file for each test, then do that!

