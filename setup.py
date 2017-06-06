#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import os

from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='jinja2-passlib_hash',
    version='0.0.1',
    author='Oleksii Aleksieiev',
    author_email='alexzzman@gmail.com',
    maintainer='Oleksii Aleksieiev',
    maintainer_email='alexzzman@gmail.com',
    license='Apache 2.0',
    url='https://github.com/oleksiialeksieiev/jinja2-passlib_hash-filter',
    description='Jinja2 Extension for passlib_hash',
    long_description=read('README.md'),
    packages=[
        'jinja2_passlib_hash',
    ],
    package_dir={'jinja2_passlib_hash': 'jinja2_passlib_hash'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'jinja2',
        'passlib'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python',
    ],
    keywords=['jinja2', 'extension', 'passlib_hash'],
)
