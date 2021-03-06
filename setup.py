#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

description = "Bottle authentication, for Personal, Google, Twitter and "\
    "facebook."

setup(
    name='bottle-auth',
    version="0.3.3",
    description=description,
    author="Thiago Avelino",
    author_email="thiago@avelino.xxx",
    url='https://github.com/avelino/bottle-auth',
    packages=find_packages(),
    package_dir={'bottle_auth': 'bottle_auth'},

    install_requires=['webob', 'bottle', 'bottle-mongo', 'bottle-beaker'],
    classifiers=[
        'Environment :: Web Environment',
        'Environment :: Plugins',
        'Framework :: Bottle',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
