#!/usr/bin/env python
# -*- coding: utf-8 -*-

#%%
"""
# Sample Script/Notebook
"""

#%%
# from __future__ imports must come at the beginning of the file
from __future__ import absolute_import, print_function, division

#%%
"""
Triple-quoted comments like this one are converted to
[Markdown](https://daringfireball.net/projects/markdown/) cells,
which support basic typography when the _Jupyter notebook_ is rendered. You
can create lists:
1. like
1. this
1. one.
"""

#%%
import os

"""
## A `Hello, World` Function
"""

"""
This is a *hello, world* function.
"""

#%%
def hello(who='World'):
    """ This is a docstring.
    """
    return "Hello, " + who


#%%
"""
I have added some helper functions to round out the conventional structure of
a Python script. This example is trivial, making the helper functions seem
pedantic.
"""

#%%
def main():
    return hello()


#%%
if __name__ == '__main__':
    print(main())

""" With the [Python
Markdown](http://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/python-markdown/readme.html)
extension enabled, the combination of VSCode, the Jupyter extension for Code,
and the Jupyter Notebook stack amount to a literate programming
environment for Python. For example, you can write expressions like
`hello('Jim')` in Markdown cells and the notebook will resolve them within the
Python REPL: {{hello('Jim')}}.

Using the Python Markdown extension in this manner comes with two gotchas:
1. If you want the Python expressions within your Markdown cells to be resolved
in, say, the HTML version of your notebook, you must execute and save the
notebook file (`*.ipynb`) before using `nbconvert` to transform the notebook.
1. You must *trust* the notebook (i.e., by clicking `File` -> `Trust Notebook`
within the notebook interface) before the Python Markdown extension will be
able to resolve Python expressions within your Markdown cells.
"""
