#!/usr/bin/env python

from setuptools import setup

# read version info from project code
exec(open('src/plotter/version.py').read())

setup_cmdclass = {}

setup(
    version=__version__,
    # cmdclass = setup_cmdclass,
)
