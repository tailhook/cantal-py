#!/usr/bin/env python

from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.rst'), 'rt') as f:
    long_description = f.read()


setup(name='cantal',
      version='0.2.2',
      description='The library that submits metrics to cantal',
      author='Paul Colomiets',
      author_email='paul@colomiets.name',
      url='http://github.com/tailhook/cantal-py',
      packages=['cantal'],
      package_data={"cantal": ["py.typed", "*.pyi"]},
      classifiers=[
          'Development Status :: 4 - Beta',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
      ],
      long_description=long_description,
      )
