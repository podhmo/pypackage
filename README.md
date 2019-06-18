# pypackage

setup

```console
$ pip install kamidana cookiecutter
```

generate project from this project template.

```console
$ cookiecutter --no-input . name=foo

$ tree foo
foo
├── CHANGES.md
├── foo
│   ├── __init__.py
│   └── tests
│       └── __init__.py
├── README.md
├── setup.cfg
└── setup.py

2 directories, 6 files

```
