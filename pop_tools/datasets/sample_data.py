"""
Functions to load sample data
"""

import os

import aletheia_data

DATASETS = aletheia_data.create(
    path=['~', '.aletheia', 'data'],
    version_dev='master',
    base_url='ftp://ftp.cgd.ucar.edu/archive/aletheia-data/cesm-data/ocn/',
)

DATASETS.load_registry(os.path.join(os.path.dirname(__file__), 'registry.txt'))
