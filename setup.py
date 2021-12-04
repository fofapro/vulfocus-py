#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/11/28 11:02
# @Author : x98zy


import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vulfocus",
    version="0.0.2",
    author="x98zy",
    author_email="xu1580987871@163.com",
    description="The Api for vulfocus",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fofapro/vulfocus-py",
    project_urls={
        "Bug Tracker": "https://github.com/fofapro/vulfocus-py/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)