#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='flavue',
    version='0.0.1',
    description='Flask + VueJS',
    author='darless',
    author_email='darless1000@gmail.com',
    packages=find_packages(exclude=('tests')),
    python_requires='>=3.8',
    install_requires=[
        'colorama'
    ],
    entry_points={
        'console_scripts': [
            'flavue = flavue.__main__:main'
        ]
    }
)
