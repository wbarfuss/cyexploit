#!/usr/bin/env python

from distutils.core import setup
from distutils.extension import Extension

import numpy as np

try:
    from Cython.Build import cythonize
    CYTHON = True
except ImportError:
    CYTHON = False

extensions = [
    Extension('*', ['cyexploit/*.%s' % ('pyx' if CYTHON else 'c')],
              include_dirs=[np.get_include()])]

if CYTHON:
    extensions = cythonize(extensions, compiler_directives={
        'language_level': 2, 'embedsignature': True,
        'boundscheck': False, 'wraparound': False, 'initializedcheck': False,
        'nonecheck': False})

setup(
    name='cyexploit',
    version='0.0.3',
    description="The COPAN:Exploit model",
    long_description="The Exploit model studies conceptual social-ecological\
 coevolution with an multi-agent framework on an adaptive network.",
    keywords="agent based model adaptive network social ecological system\
 coevolution planetary boundaries safe and just operating space",
    author="Wolfram Barfuss",
    author_email="barfuss@pik-potsdam.de",
    # url="",
    platforms=['all'],
    packages=["cyexploit"],
    ext_modules=extensions,
    requires=['numpy (>=1.9.2)', 'networkx(>=1.9.1)'],
    provides=['cyexploit'],
    scripts=[],
    license='BSD',
)
