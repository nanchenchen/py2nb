#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_py2nb
----------------------------------

Tests for `py2nb` module.
"""

import pytest
import py2nb
import os


@pytest.fixture
def samplepy(fname='hello.py'):
    return os.path.join('tests', fname)


@pytest.fixture
def sampleipynb(fname='hello.ipynb'):
    return os.path.join('tests', fname)


def test_py2nb(samplepy, sampleipynb):
    py2nb.python_to_notebook(input_filename=samplepy,
                             output_filename=os.path.join('tests',
                                                          'test_py2nb.ipynb'))
    with open(os.path.join('tests', 'test_py2nb.ipynb'), 'r') as outfileobj:
        outfile = outfileobj.read()
    with open(sampleipynb, 'r') as reffileobj:
        refile = reffileobj.read()
    assert outfile == refile
    os.remove(os.path.join('tests', 'test_py2nb.ipynb'))
