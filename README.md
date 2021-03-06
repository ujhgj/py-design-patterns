[![Build Status](https://travis-ci.com/ujhgj/py-design-patterns.svg?branch=master)](https://travis-ci.com/ujhgj/py-design-patterns)

# Python-Flavored Design Patterns

## Patterns Collection

- Creational:
  - [Singleton](patterns/creational/singleton.py) ([tests](tests/patterns/creational/test_singleton.py))
  - [Builder and Director](patterns/creational/builder.py) ([tests](tests/patterns/creational/test_builder.py))

## Tests

Best to use venv to run a dedicated environment for tests:
1. Create environment:
    ```bash
    python3 -m venv venv
    ```
1. Activate:
    ```bash
    source venv/bin/activate
    ```
1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

1. Run the tests
    ```bash
    python -m pytest
    ```

## TODO
1. Documentation
