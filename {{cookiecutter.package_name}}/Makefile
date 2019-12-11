test:
	pytest -vv --show-capture=all

ci:
	pytest --show-capture=all --cov={{cookiecutter.directory_name}} --no-cov-on-fail --cov-report term-missing
	$(MAKE) lint typing

format:
#	pip install -e .[dev]
	black {{cookiecutter.directory_name}} setup.py

lint:
#	pip install -e .[dev]
	flake8 {{cookiecutter.directory_name}} --ignore W503,E203,E501

typing:
#	pip install -e .[dev]
	mypy --strict --strict-equality --ignore-missing-imports {{cookiecutter.directory_name}}
mypy: typing

build:
#	pip install wheel
	python setup.py bdist_wheel

upload:
#	pip install twine
	twine check dist/{{cookiecutter.package_name}}-$(shell cat VERSION)*
	twine upload dist/{{cookiecutter.package_name}}-$(shell cat VERSION)*

.PHONY: test ci format lint typing mypy build upload
