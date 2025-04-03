# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='litepolis-middleware-rate-limiter',
    version="0.0.1",
    description='The rate limit middleware module for LitePolis',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='NewJerseyStyle',
    # author_email='Optional',
    url='https://github.com/NewJerseyStyle/LitePolis-middleware-rate-limiter',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=['litepolis'],
)
