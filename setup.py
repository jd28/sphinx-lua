#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = 'sphinx-lua',
    version = "0.1",
    package_dir = {'': 'src'},
    packages = [
      'sphinx_lua'
    ],
    install_requires = ['Sphinx'],
)
