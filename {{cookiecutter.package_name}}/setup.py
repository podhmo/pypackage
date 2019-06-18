import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(here, "README.md")) as f:
        README = f.read()
    with open(os.path.join(here, "CHANGES.md")) as f:
        CHANGES = f.read()
except IOError:
    README = CHANGES = ""


install_requires = []
dev_requires = ["black", "flake8"]
tests_requires = []

setup(
    name="{{cookiecutter.package_name}}",
    version="{{cookiecutter.version}}",
    description="{{cookiecutter.description}}",
    long_description=README + "\n\n" + CHANGES,
    long_description_content_type="text/markdown",
    classifiers=[
        # "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
    ],
    python_requires=">3.5",
    keywords="",
    author="{{cookiecutter.user_name}}",
    author_email="",
    url="https://github.com/{{cookiecutter.user_name}}/{{cookiecutter.package_name}}",
    packages=find_packages(exclude=["{{cookiecutter.directory_name}}.tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    extras_require={"testing": tests_requires, "dev": dev_requires},
    tests_require=tests_requires,
    test_suite="{{cookiecutter.directory_name}}.tests",
    entry_points="""
""",
)
