#!/usr/bin/python

import setuptools

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()
    
KEYWORDS = ('dnsdist console client')

setuptools.setup(
    name="dnsdist_console",
    version="1.6.0",
    author="Denis MACHARD",
    author_email="d.machard@gmail.com",
    description="Python client for dnsdist console",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/dmachard/dnsdist_console",
    packages=['dnsdist_console', 'tests'],
    include_package_data=True,
    platforms='any',
    keywords=KEYWORDS,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
    ],
    install_requires=[
        "libnacl",
        "scrypt",
    ]
)