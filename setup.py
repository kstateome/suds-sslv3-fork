#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
    name='suds',
    version='0.4.1',
    description='Fork of Suds for use with SSLv3 ',
    author="Jeff Ortel",
    author_email="jortel@redhat.com",
    url='https://github.com/kstateome/suds-sslv3-fork',
    packages=find_packages(),
    include_package_data=True,
    license="GPL",
    zip_safe=False,
    keywords='suds',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries',
    ],
)