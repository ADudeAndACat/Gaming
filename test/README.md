# Gaming Package Tests

This directory contains tests for the Gaming package. The tests are written using pytest.

## Running the Tests

To run the tests, use the following command from the root directory of the project:

```bash
pytest
```

Or for more detailed output:

```bash
pytest -v
```

## Test Coverage

To generate a test coverage report, use:

```bash
pytest --cov=Gaming
```

## Test Structure

Each module in the Gaming package has a corresponding test file with the same name prefixed with "test_". For example, the module `diceroller.py` has a test file called `test_diceroller.py`.

The `conftest.py` file contains common fixtures and configuration for the tests.

The `test_time.py` file contains performance tests for the package.
