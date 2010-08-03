#!/usr/bin/env python
from distutils.core import setup
import winrandom

LONG_DESCRIPTION = \
"""An implementation of the winrandom module using ctypes instead of a
compiled extension module."""

CLASSIFIERS = [
                'Development Status :: 4 - Beta',
                'Intended Audience :: Developers',
                'License :: OSI Approved :: BSD License',
                'Natural Language :: English',
                'Operating System :: Microsoft :: Windows',
                'Programming Language :: Python',
                'Topic :: Scientific/Engineering :: Mathematics',
                'Topic :: Software Development :: Libraries :: Python Modules' 
              ]

KEYWORDS = 'random windows winrandom'

setup(name='winrandom-ctypes',
      version=winrandom.VERSION,
      description='Winrandom equivalent using ctypes.',
      long_description = LONG_DESCRIPTION,
      author='Gregory Taylor',
      author_email='gtaylor@duointeractive.com',
      url='http://github.com/duointeractive/winrandom-ctypes',
      download_url='http://pypi.python.org/pypi?:action=display&name=winrandom-ctypes',
      packages=['winrandom'],
      platforms = ['Windows'],
      license = 'BSD',
      classifiers = CLASSIFIERS,
      keywords = KEYWORDS,
      provides = ['winrandom']
     )
