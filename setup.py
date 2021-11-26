#!/usr/bin/env python3
import os
from setuptools import setup, find_packages

def long_description():
    with open('README.md', encoding='utf-8') as f:
        return f.read()


here = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(here, 'ettil', '__version__.py'),
          encoding='utf-8') as f:
    exec(f.read(), about)

setup(
    name='ettil',
    author=about['__author__'],
    description=about['__description__'],
    license=about['__license__'],
    url=about['__url__'],
    version=about['__version__'],
    long_description=long_description(),
    long_description_content_type='text/markdown',
    packages=find_packages(include=['ettil']),
    python_requires='>=3.6',
    install_requires=[
        'requests'
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha'
        'Intended Audience :: Developers'
        'License :: OSI Approved :: Apache Software License'
        'Operating System :: OS Independent'
        'Programming Language :: Python'
        'Topic :: Internet :: WWW/HTTP'
    ]
)
