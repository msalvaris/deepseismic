#!/usr/bin/env python
import os
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages
# import sys
# import warnings
import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.INFO)
log = logging.getLogger()

NAME = 'deepseismic'
DESCRIPTION = 'When violating best practices is your thing :)'
URL = ''
EMAIL = ''
AUTHOR = ''
LICENSE = ''
LONG_DESCRIPTION = DESCRIPTION


with open('imaging_requirements.txt') as f:
    imaging_requirements = f.read().splitlines()

with open('interpretation_requirements.txt') as f:
    interpretation_requirements = f.read().splitlines()

setup(name=NAME,
    version=0.01,
    url=URL,
    license=LICENSE,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=['deepseismic.imaging',
                'deepseismic.interpretation'],
    install_requires=['toolz'],
    extras_require={
        'imaging':[imaging_requirements],
        'interpretation':[interpretation_requirements]
    },
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 1 - Alpha",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy"])

