# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages
setup(
    name = 'keplerapp_tbcheck',
    version = '0.1', # release version (based on how far along this library's development is
    download_url = "#", # prehaps a tar.gz we store in SVN
    platforms = ['any'],
    packages = find_packages(),
    zip_safe = False,
    include_package_data=True
)
