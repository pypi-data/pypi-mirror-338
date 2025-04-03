"""
Tests for the PyGERG package.
"""

import unittest
import pytest
from pygerg import sgerg, GERG88


class TestGERG88(unittest.TestCase):
    """Test cases for the GERG-88 implementation."""
    
    def test_basic_calculation(self):
        """Test that the basic calculation works with standard parameters."""
        x3 = 0.01   # % CO2
        hs = 37.0   # Calorific value (MJ/m^3)
        rm = 0.7443  # Relative density
        x5 = 0.00   # 0% H2
        p = 8.0     # bar
        tc = 15.0   # °C
        
        x2, z, d = sgerg(x3, hs, rm, x5, p, tc)
        
        # Check results against expected values
        self.assertAlmostEqual(x2, 0.2061, delta=0.001)
        self.assertAlmostEqual(z, 0.981100, delta=0.0001)
        self.assertAlmostEqual(d, 0.340347, delta=0.1)
    
    def test_input_validation(self):
        """Test that the function validates input parameters correctly."""
        x3 = 0.01   # % CO2
        hs = 37.0   # Calorific value (MJ/m^3)
        rm = 0.7443  # Relative density
        x5 = 0.00   # 0% H2
        p = 8.0     # bar
        tc = 15.0   # °C
        
        # Test pressure out of range
        with self.assertRaises(ValueError):
            sgerg(x3, hs, rm, x5, 150.0, tc)
        
        # Test temperature out of range
        with self.assertRaises(ValueError):
            sgerg(x3, hs, rm, x5, p, 70.0)
        
        # Test CO2 fraction out of range
        with self.assertRaises(ValueError):
            sgerg(0.35, hs, rm, x5, p, tc)
        
        # Test calorific value out of range
        with self.assertRaises(ValueError):
            sgerg(x3, 50.0, rm, x5, p, tc)
        
        # Test relative density out of range
        with self.assertRaises(ValueError):
            sgerg(x3, hs, 0.5, x5, p, tc)
        
        # Test H2 fraction out of range
        with self.assertRaises(ValueError):
            sgerg(x3, hs, rm, 0.15, p, tc)
    
    def test_direct_class_usage(self):
        """Test direct usage of the GERG88 class."""
        calculator = GERG88()
        
        x3 = 0.01   # % CO2
        hs = 37.0   # Calorific value (MJ/m^3)
        rm = 0.7443  # Relative density
        x5 = 0.00   # 0% H2
        p = 8.0     # bar
        tc = 15.0   # °C
        
        x2, z, d = calculator.sgerg(x3, hs, rm, x5, p, tc)
        
        # Check results against expected values
        self.assertAlmostEqual(x2, 0.2061, delta=0.001)
        self.assertAlmostEqual(z,  0.981100, delta=0.0001)
        self.assertAlmostEqual(d, 0.340347, delta=0.1)

if __name__ == "__main__":
    unittest.main()