# pypackage

setup

```console
$ pip install kamidana cookiecutter
```

generate project from this project template.

```console
$ cookiecutter --no-input gh:podhmo/pypackage name=foo

$ tree foo
foo
├── foo
│   ├── __init__.py
│   └── tests
│       └── __init__.py
├── Makefile
├── README.md
├── setup.cfg
├── setup.py
└── VERSION

2 directories, 7 files

```
