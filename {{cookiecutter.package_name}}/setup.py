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
tests_requires = []

setup(
    name="{{cookiecutter.package_name}}",
    version="0.0.0",
    description="{{cookiecutter.description}}",
    long_description=README + "\n\n" + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    keywords="",
    author="",
    author_email="",
    url="",
    packages=find_packages(exclude=["{{cookiecutter.directory_name}}.tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    extras_require={"testing": tests_requires},
    tests_require=tests_requires,
    test_suite="{{cookiecutter.directory_name}}.tests",
    entry_points="""
""",
)
