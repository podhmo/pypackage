test:
	python setup.py test

format:
#	pip install -e .[dev]
	black {{cookiecutter.directory_name}} setup.py

build:
#	pip install wheel
	python setup.py bdist_wheel

upload:
#	pip install twine
	twine check dist/{{cookiecutter.package_name}}-$(shell cat VERSION)*
	twine upload dist/{{cookiecutter.package_name}}-$(shell cat VERSION)*

.PHONY: test format build upload
