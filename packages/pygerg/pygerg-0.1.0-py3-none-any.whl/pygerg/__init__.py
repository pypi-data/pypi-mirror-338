"""
PyGERG: Python implementation of the GERG-88 standard for natural gas properties

This package provides tools for calculating compression factors and other
properties of natural gases using the GERG-88 standard.

The main function, sgerg(), calculates compression factors of natural gases 
using a simplified gas analysis with just four parameters.
"""

from .gerg88 import sgerg, GERG88

__version__ = "0.1.0"
__author__ = "Tijs van der Velden"
__all__ = ["sgerg", "GERG88"]