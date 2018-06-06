#!/usr/bin/env python3

from setuptools import setup, find_packages


with open('requirements.txt') as requirements:
    required = requirements.read().splitlines()

setup(
    name='crawltwitter',
    version='1.0',
    description='Tool for crawling twitter for tweets regarding particular interest',
    author=['Akshay Mittal'],
    author_email='it158040@mnnit.ac.in',
    license='Pyenoma',
    packages=find_packages(exclude=["build.*", "tests", "tests.*"]),
    install_requires=required,
    entry_points={
        "console_scripts": [
            "crawltwitter = crawltwitter.main:main"
        ]
    })
