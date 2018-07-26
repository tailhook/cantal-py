#!/usr/bin/env python

from setuptools import setup

setup(name='cantal',
      version='0.2.2',
      description='The library that submits metrics to cantal',
      author='Paul Colomiets',
      author_email='paul@colomiets.name',
      url='http://github.com/tailhook/cantal-py',
      packages=['cantal'],
      package_data={"cantal": ["py.typed"]},
      classifiers=[
          'Development Status :: 4 - Beta',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
      ],
      )
