#!/usr/bin/env python3
from setuptools import setup, find_packages


def long_description():
    with open('README.md', encoding='utf-8') as f:
        return f.read()


setup(
    name='ettl',
    version="0.1.0a0",
    description="Edit the Text Interface Library",
    long_description=long_description(),
    long_description_content_type='text/markdown',
    url='https://github.com/tlras/ettil',
    author='tlras',
    license='Apache-2.0',
    packages=find_packages(include=['ettli']),
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