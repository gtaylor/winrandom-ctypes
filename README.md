winrandom-ctypes
================

This package is meant to be a functional equivalent to Pawel Krawczyk's excellent 
[.winrandom](http://ipsec.pl/winrandom) module. However, this version (as the
name implies) uses ctypes instead of a C extension module. This is attractive in
cases where compiling such a module would be difficult or impossible.

Usage
-----

Usage is the same as the original [.winrandom](http://ipsec.pl/winrandom) module:

    >>> import winrandom
    >>> print winrandom.long()
    2141228967
    >>> print repr(winrandom.bytes(10))
    '\xe6C\xfe\xbeRA\xfck"f'
