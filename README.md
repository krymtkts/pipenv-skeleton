Pipenv simple skeleton
======================

A simple skeleton of pipenv project.

This project includes some dev settings below.

- Python 3.7
- autopep8
- Pylint
- YAPF
    - Google style format
- mypy

Usage
-----

Clone or copy this project.

### Commands

```sh
# Install dev dependencies.
pipenv install --dev

# Static type check wiht mypy strict mode.
pipenv run type

# Lint module wih pylint.
pipenv run lint
```

Links
-----

- [Pipenv: Python Dev Workflow for Humans — pipenv 2018.11.27.dev0 documentation](https://docs.pipenv.org/en/latest/)
- [hhatto/autopep8: A tool that automatically formats Python code to conform to the PEP 8 style guide.](https://github.com/hhatto/autopep8)
- [Pylint - code analysis for Python | www.pylint.org](https://www.pylint.org/)
- [google/yapf: A formatter for Python files](https://github.com/google/yapf)
- [mypy - Optional Static Typing for Python](http://mypy-lang.org/)