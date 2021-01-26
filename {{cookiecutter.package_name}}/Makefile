test:
	pytest -vv --show-capture=all

ci:
	pytest --show-capture=all --cov={{cookiecutter.directory_name}} --no-cov-on-fail --cov-report term-missing
	$(MAKE) lint typing

format:
#	pip install -e .[dev]
	black {{cookiecutter.directory_name}} setup.py

# https://www.flake8rules.com/rules/W503.html
# https://www.flake8rules.com/rules/E203.html
# https://www.flake8rules.com/rules/E501.html
lint:
#	pip install -e .[dev]
	flake8 {{cookiecutter.directory_name}} --ignore W503,E203,E501

typing:
#	pip install -e .[dev]
	mypy --strict --strict-equality --ignore-missing-imports {{cookiecutter.directory_name}}
mypy: typing

#### for pypi ####################

get-version:
	python -c 'import {{cookiecutter.directory_name}} as m; print(m.__version__)'

build:
#	pip install wheel
	python setup.py sdist bdist_wheel

upload:
#	pip install twine
	twine check dist/{{cookiecutter.package_name}}-$(shell make -s get-version)*
	twine upload dist/{{cookiecutter.package_name}}-$(shell make -s get-version)*.tar.gz
	twine upload dist/{{cookiecutter.package_name}}-$(shell make -s get-version)*.whl

.PHONY: test ci format lint typing mypy build upload
