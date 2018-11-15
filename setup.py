#!/usr/bin/env python
#
# Copyright (c) 2016, 2016 Timothy Savannah under terms of GPLv3. You should have received a copy of this with this distribution as "LICENSE"


#vim: set ts=4 sw=4 st=4 expandtab

import os
import sys

from setuptools import setup


if __name__ == '__main__':
 

    dirName = os.path.dirname(__file__)
    if dirName and os.getcwd() != dirName:
        os.chdir(dirName)

    summary = 'Powerful commandline tool to extract and manipulate strings using regular exressions'

    try:
        with open('README.rst', 'rt') as f:
            long_description = f.read()
    except Exception as e:
        sys.stderr.write('Exception when reading long description: %s\n' %(str(e),))
        long_description = summary

    setup(name='rextract',
            version='1.1.1',
            scripts=['rextract'],
            author='Tim Savannah',
            author_email='kata198@gmail.com',
            maintainer='Tim Savannah',
            url='https://github.com/kata198/rextract',
            maintainer_email='kata198@gmail.com',
            description=summary,
            long_description=long_description,
            license='GPLv3',
            keywords=['rextract', 'regex', 'extract', 're', 'sed', 'grep', 'format', 'reformat', 'text', 'manipulate', 'strings', 'input', 'output', 'io', 'cli', 'commandline'],
            classifiers=['Development Status :: 5 - Production/Stable',
                         'Environment :: Console',
                         'Topic :: Text Processing',
                         'Topic :: Text Processing :: General',
                         'Topic :: Text Processing :: Filters',
                         'Topic :: Utilities',
                         'Programming Language :: Python',
                         'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                         'Programming Language :: Python :: 2',
                         'Programming Language :: Python :: 2',
                         'Programming Language :: Python :: 2.7',
                         'Programming Language :: Python :: 3',
                         'Programming Language :: Python :: 3.4',
                         'Programming Language :: Python :: 3.5',
                         'Programming Language :: Python :: 3.6',
                         'Programming Language :: Python :: 3.7',
            ]
    )

