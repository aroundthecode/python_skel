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

# read build number from build.info
conf_dict = read_configuration('setup.cfg')
build = open(path.join(here, 'build.info')).read().strip()

# read main requirements from requirements.txt
with open('requirements.txt') as f:
    reqs = f.read().splitlines()

requirements = [x for x in reqs if not x.startswith("#")]


setup(
    version=(conf_dict['metadata']['version'] + "." + str(build)),
    install_requires=requirements
)
