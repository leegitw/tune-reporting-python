#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Copyright (c) 2016 TUNE, Inc.
#    All rights reserved.
#

from __future__ import with_statement

# To install the tune-reporting-python library, open a Terminal shell, then run this
# file by typing:
#
# python setup.py install
#

import sys
import re
from setuptools import setup

REQUIREMENTS = [
    req for req in open('requirements.txt')
    .read().split('\n')
    if req != ''
]

PACKAGES = [
    'tune_reporting',
    'tune_reporting.errors',
    'tune_reporting.readers',
    'tune_reporting.support',
    'tune_reporting.tmc',
    'tune_reporting.tmc.v2.management',
    'tune_reporting.tmc.v2.reporting',
    'tune_reporting.tmc.v3.reporting'
]

with open('tune_reporting/__init__.py', 'r') as fd:
    __sdk_version__ = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)

if not __sdk_version__:
    raise RuntimeError('Cannot find version information')

if len(sys.argv) < 2 or sys.argv[1] == 'version':
    print(__sdk_version__)
    sys.exit()

CLASSIFIERS = [
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    'Topic :: Software Development :: Libraries :: Python Modules'
]

setup(
    name='tune-reporting',
    version=__sdk_version__,
    description='TUNE Reporting API client library.',
    author='TUNE',
    author_email='jefft@tune.com',
    url='https://github.com/MobileAppTracking/tune-reporting-python',
    keywords=["tune", "tune reporting", "mobileapptracking"],
    install_requires=REQUIREMENTS,
    packages=PACKAGES,
    package_dir={'tune_reporting': 'tune_reporting'},
    license='MIT License',
    zip_safe=False,
    classifiers=CLASSIFIERS,
    long_description="""\
    TUNE Reporting API client library for Python.
    ---------------------------------------------

    DESCRIPTION
    TUNE Reporting API client library simplifies the process of
    making calls using the TUNE Reporting API.

    TUNE Reporting API is for advertisers to export data.

    See https://github.com/MobileAppTracking/tune-reporting-python for
    more information.

    LICENSE TUNE Reporting Python SDK is distributed under the MIT
    License """
)
