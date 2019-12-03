"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup
from setuptools.config import read_configuration
from os import path

here = path.abspath(path.dirname(__file__))
conf_dict = read_configuration('setup.cfg')
setup()
