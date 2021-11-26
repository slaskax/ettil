#!/usr/bin/env python3
import ettil
from setuptools import setup, find_packages


def long_description():
    with open('README.md', encoding='utf-8') as f:
        return f.read()


setup(
    name='ettil',
    author=ettil.__author__,
    description=ettil.__description__,
    license=ettil.__license__,
    url=ettil.__url__,
    version=ettil.__version__,
    long_description=long_description(),
    long_description_content_type='text/markdown',
    packages=find_packages(include=['ettil']),
    python_requires='>=3.6',
    install_requires=[
        "requests"
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