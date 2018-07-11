#!/usr/bin/env python

from os.path import exists
from setuptools import setup


long_description = open('README.md').read() if exists('README.md') else ''

setup(name='bcsd',
      version='0.0.1',
      description='',
      url='https://github.com/nmizukami/LOCA_Downscaling_Analysis',
      license='Apache',
      packages=['bcsd'],
      long_description=long_description,
      zip_safe=False)
