"""
GERG-88 Virial Equation for Natural Gas Compression Factors

This module implements the GERG-88 standard for calculating the compression factors
of natural gases using a simplified gas analysis.

The calculations are based on the following four input parameters for the gas analysis:
    - x3: mole fraction CO2 (0.0 -> 0.3)
    - hs: calorific value in MJ/m^3 (20 -> 48)
    - rm: relative density (0.55 -> 0.9)
    - x5: mole fraction H2 (0.0 -> 0.1)

Note: metering at T = 0.0 C, P = 1.01325 bar
      combustion at T = 25.0 C

Further input parameters used are:
    - p: pressure in bar (0 -> 120)
    - tc: temperature in degrees Celsius (-23 -> 65)

The calculated values are:
    - z: compression factor
    - d: molar density in mol/m^3
    - x2: calculated molar fraction of nitrogen

Original FORTRAN implementation by J.P.J. Michels & J.A. Schouten, August 16, 1991
Python conversion by Tijs van der Velden, April 2nd, 2025
"""

import math
from typing import Tuple, Union, Optional


class GERG88:
    """
    GERG-88 implementation for calculating the compression factors of natural gases.
    
    This class implements the GERG-88 standard for natural gas compression factors
    using a simplified gas analysis based on four key parameters.
    """
    
    def __init__(self):
        """Initialize the GERG-88 calculator with its constants."""
        # Initialize constants
        self._init_constants()
        
    def _init_constants(self):
        """Initialize all constants needed for the GERG-88 calculation."""
        # Constants from BLOCK DATA
        self.BR11H0 = [-0.425468, 0.286500e-2, -0.462073e-5]
        self.BR11H1 = [0.877118e-3, -0.556281e-5, 0.881510e-8]
        self.BR11H2 = [-0.824747e-6, 0.431436e-8, -0.608319e-11]
        self.BR22 = [-0.144600, 0.740910e-3, -0.911950e-6]
        self.BR23 = [-0.339693, 0.161176e-2, -0.204429e-5]
        self.BR33 = [-0.868340, 0.403760e-2, -0.516570e-5]
        self.BR15 = [-0.521280e-1, 0.271570e-3, -0.25e-6]
        self.BR17 = [-0.687290e-1, -0.239381e-5, 0.518195e-6]
        self.BR55 = [-0.110596e-2, 0.813385e-4, -0.987220e-7]
        self.BR77 = [-0.130820, 0.602540e-3, -0.644300e-6]
        self.B25 = 0.012
        
        self.CR111H0 = [-0.302488, 0.195861e-2, -0.316302e-5]
        self.CR111H1 = [0.646422e-3, -0.422876e-5, 0.688157e-8]
        self.CR111H2 = [-0.332805e-6, 0.223160e-8, -0.367713e-11]
        self.CR222 = [0.784980e-2, -0.398950e-4, 0.611870e-7]
        self.CR223 = [0.552066e-2, -0.168609e-4, 0.157169e-7]
        self.CR233 = [0.358783e-2, 0.806674e-5, -0.325798e-7]
        self.CR333 = [0.205130e-2, 0.348880e-4, -0.837030e-7]
        self.CR555 = [0.104711e-2, -0.364887e-5, 0.467095e-8]
        self.CR117 = [0.736748e-2, -0.276578e-4, 0.343051e-7]
        
        self.Z12 = 0.72
        self.Z13 = -0.865
        self.Y12 = 0.92
        self.Y13 = 0.92
        self.Y123 = 1.10
        self.Y115 = 1.2
        
        self.GM1R0 = -2.709328
        self.GM1R1 = 0.021062199
        self.GM2 = 28.0135
        self.GM3 = 44.010
        self.GM5 = 2.0159
        self.GM7 = 28.010
        self.FA = 22.414097
        self.FB = 22.710811
        self.RL = 1.292923
        self.T0 = 273.15
        self.H5 = 285.83
        self.H7 = 282.98
        self.R = 0.0831451
        
    def sgerg(self, x3: float, hs: float, rm: float, x5: float, p: float, tc: float) -> Tuple[float, float, float]:
        """
        Calculate the compression factors of natural gases using a simplified gas analysis.
        
        Args:
            x3: Mole fraction CO2 (0.0 -> 0.3)
            hs: Calorific value in MJ/m^3 (20 -> 48)
            rm: Relative density (0.55 -> 0.9)
            x5: Mole fraction H2 (0.0 -> 0.1)
            p: Pressure in bar (0 -> 120)
            tc: Temperature in degrees Celsius (-23 -> 65)
            
        Returns:
            tuple: (x2, z, d) where:
                x2: Calculated molar fraction of nitrogen
                z: Compression factor
                d: Molar density in mol/m^3
                
        Raises:
            ValueError: If input parameters are out of range or results are invalid
            RuntimeError: If convergence fails
        """
        # Check if inputs are within valid ranges
        if p < 0.0 or p > 120.0:
            raise ValueError("Pressure out of range (0-120 bar)")
        if tc < -23.0 or tc > 65.0:
            raise ValueError("Temperature out of range (-23-65 °C)")
            
        # Call the main calculation routine
        x2, z, d = self._sgerg1(p, tc, x3, x5, hs, rm)
        return x2, z, d
        
    def _sgerg1(self, p: float, tc: float, q3: float, q5: float, qm: float, rm: float) -> Tuple[float, float, float]:
        """
        Internal implementation of the SGERG algorithm.
        
        Args:
            p: Pressure in bar
            tc: Temperature in degrees Celsius
            q3: Mole fraction CO2
            q5: Mole fraction H2
            qm: Calorific value in MJ/m^3
            rm: Relative density
            
        Returns:
            tuple: (x2, z, d) where:
                x2: Calculated molar fraction of nitrogen
                z: Compression factor
                d: Molar density in mol/m^3
        """
        # Assign values to instance variables
        self.hs = qm
        self.x3 = q3
        self.x5 = q5
        
        # Check inputs
        if rm < 0.55 or rm > 0.90:
            raise ValueError("Relative density out of range (0.55-0.90)")
        if self.x3 < 0.0 or self.x3 > 0.30:
            raise ValueError("CO2 fraction out of range (0.0-0.30)")
        if self.hs < 20.0 or self.hs > 48.0:
            raise ValueError("Calorific value out of range (20-48 MJ/m^3)")
        if self.x5 < 0.0 or self.x5 > 0.10:
            raise ValueError("H2 fraction out of range (0.0-0.10)")
            
        if (0.55 + 0.97 * self.x3 - 0.45 * self.x5) > rm:
            raise ValueError("Conflicting input parameters")
            
        sm = rm * self.RL
        self.x7 = self.x5 * 0.0964
        self.x33 = self.x3 * self.x3
        self.x55 = self.x5 * self.x5
        self.x77 = self.x7 * self.x7
        
        beff = -0.065
        h = 1000.0
        self.amol = 1.0 / (self.FA + beff)
        k = 0
        kk = 0
        
        # Iterative calculation to determine composition
        while True:
            smt1 = self._smber(h)
            
            if abs(sm - smt1) > 1.0e-6:
                smt2 = self._smber(h + 1.0)
                dh = (sm - smt1) / (smt2 - smt1)
                h = h + dh
                kk += 1
                if kk > 20:
                    raise RuntimeError("No convergence in composition calculation")
                continue
                
            self.x11 = self.x1 * self.x1
            self.x12 = self.x1 * self.x2
            self.x13 = self.x1 * self.x3
            self.x22 = self.x2 * self.x2
            self.x23 = self.x2 * self.x3
            self.x25 = self.x2 * self.x5
            self.x15 = self.x1 * self.x5
            self.x17 = self.x1 * self.x7
            
            b11 = self._b11ber(self.T0, h)
            beff = self._bber(self.T0, b11)
            self.amol = 1.0 / (self.FA + beff)
            hsber = self.x1 * h * self.amol + (self.x5 * self.H5 + self.x7 * self.H7) * self.amol
            
            if abs(self.hs - hsber) > 1.0e-4:
                k += 1
                if k > 20:
                    raise RuntimeError("No convergence in heat value calculation")
                continue
            break
        
        # Check calculated nitrogen content
        if self.x2 < -0.01 or self.x2 > 0.5:
            raise ValueError("Calculated N2 fraction out of range")
        if self.x2 + self.x3 > 0.5:
            raise ValueError("Sum of N2 and CO2 fractions out of range")
        if (0.55 + 0.4 * self.x2 + 0.97 * self.x3 - 0.45 * self.x5) > rm:
            raise ValueError("Conflicting result for N2 fraction")
            
        q2 = self.x2
        t = tc + self.T0
        b11 = self._b11ber(t, h)
        b = self._bber(t, b11)
        c = self._cber(t, h)
        v, z = self._iter(p, t, b, c)
        d = 1.0 / v
        
        return q2, z, d
        
    def _smber(self, h: float) -> float:
        """
        Calculate molar mass based on composition and heat value.
        
        Args:
            h: Heat value parameter
            
        Returns:
            float: Calculated molar mass
        """
        gm1 = self.GM1R0 + self.GM1R1 * h
        self.x1 = (self.hs - (self.x5 * self.H5 + self.x7 * self.H7) * self.amol) / h / self.amol
        self.x2 = 1.0 - self.x1 - self.x3 - self.x5 - self.x7
        sm = (self.x1 * gm1 + self.x2 * self.GM2 + self.x3 * self.GM3 + 
              self.x5 * self.GM5 + self.x7 * self.GM7) * self.amol
        return sm
        
    def _b11ber(self, t: float, h: float) -> float:
        """
        Calculate B11 coefficient for given temperature and heat value.
        
        Args:
            t: Temperature in Kelvin
            h: Heat value parameter
            
        Returns:
            float: B11 coefficient
        """
        t2 = t * t
        b11 = (self.BR11H0[0] + self.BR11H0[1] * t + self.BR11H0[2] * t2 +
              (self.BR11H1[0] + self.BR11H1[1] * t + self.BR11H1[2] * t2) * h +
              (self.BR11H2[0] + self.BR11H2[1] * t + self.BR11H2[2] * t2) * h * h)
        return b11
        
    def _bber(self, t: float, b11: float) -> float:
        """
        Calculate the effective B coefficient for virial equation.
        
        Args:
            t: Temperature in Kelvin
            b11: B11 coefficient
            
        Returns:
            float: Effective B coefficient
            
        Raises:
            ValueError: If no solution exists
        """
        t2 = t * t
        b22 = self.BR22[0] + self.BR22[1] * t + self.BR22[2] * t2
        b23 = self.BR23[0] + self.BR23[1] * t + self.BR23[2] * t2
        b33 = self.BR33[0] + self.BR33[1] * t + self.BR33[2] * t2
        b15 = self.BR15[0] + self.BR15[1] * t + self.BR15[2] * t2
        b55 = self.BR55[0] + self.BR55[1] * t + self.BR55[2] * t2
        b17 = self.BR17[0] + self.BR17[1] * t + self.BR17[2] * t2
        b77 = self.BR77[0] + self.BR77[1] * t + self.BR77[2] * t2
        
        ba13 = b11 * b33
        if ba13 < 0.0:
            raise ValueError("No viable solution for B coefficient")
            
        zzz = self.Z12 + (320.0 - t)**2 * 1.875e-5
        
        beff = (self.x11 * b11 + 
               self.x12 * zzz * (b11 + b22) + 
               2.0 * self.x13 * self.Z13 * math.sqrt(ba13) +
               self.x22 * b22 + 
               2.0 * self.x23 * b23 + 
               self.x33 * b33 + 
               self.x55 * b55 +
               2.0 * self.x15 * b15 + 
               2.0 * self.x25 * self.B25 + 
               2.0 * self.x17 * b17 + 
               self.x77 * b77)
        return beff
        
    def _cber(self, t: float, h: float) -> float:
        """
        Calculate the effective C coefficient for virial equation.
        
        Args:
            t: Temperature in Kelvin
            h: Heat value parameter
            
        Returns:
            float: Effective C coefficient
            
        Raises:
            ValueError: If no solution exists
        """
        t2 = t * t
        c111 = (self.CR111H0[0] + self.CR111H0[1] * t + self.CR111H0[2] * t2 +
               (self.CR111H1[0] + self.CR111H1[1] * t + self.CR111H1[2] * t2) * h +
               (self.CR111H2[0] + self.CR111H2[1] * t + self.CR111H2[2] * t2) * h * h)
               
        c222 = self.CR222[0] + self.CR222[1] * t + self.CR222[2] * t2
        c223 = self.CR223[0] + self.CR223[1] * t + self.CR223[2] * t2
        c233 = self.CR233[0] + self.CR233[1] * t + self.CR233[2] * t2
        c333 = self.CR333[0] + self.CR333[1] * t + self.CR333[2] * t2
        c555 = self.CR555[0] + self.CR555[1] * t + self.CR555[2] * t2
        c117 = self.CR117[0] + self.CR117[1] * t + self.CR117[2] * t2
        
        ca112 = c111 * c111 * c222
        ca113 = c111 * c111 * c333
        ca122 = c111 * c222 * c222
        ca123 = c111 * c222 * c333
        ca133 = c111 * c333 * c333
        ca115 = c111 * c111 * c555
        
        if (ca112 < 0.0 or ca113 < 0.0 or ca122 < 0.0 or
            ca123 < 0.0 or ca133 < 0.0 or ca115 < 0.0):
            raise ValueError("No viable solution for C coefficient")
            
        d3rep = 1.0 / 3.0
        
        ceff = (self.x1 * self.x11 * c111 +
               3.0 * self.x11 * self.x2 * (ca112)**d3rep * (self.Y12 + (t - 270.0) * 0.0013) +
               3.0 * self.x11 * self.x3 * (ca113)**d3rep * self.Y13 +
               3.0 * self.x1 * self.x15 * (ca115)**d3rep * self.Y115 +
               3.0 * self.x1 * self.x22 * (ca122)**d3rep * (self.Y12 + (t - 270.0) * 0.0013) +
               6.0 * self.x1 * self.x2 * self.x3 * (ca123)**d3rep * self.Y123 +
               3.0 * self.x1 * self.x33 * (ca133)**d3rep * self.Y13 +
               self.x22 * self.x2 * c222 + 
               3.0 * self.x22 * self.x3 * c223 + 
               3.0 * self.x2 * self.x33 * c233 +
               self.x3 * self.x33 * c333 + 
               self.x5 * self.x55 * c555 + 
               3.0 * self.x11 * self.x7 * c117)
        return ceff
        
    def _iter(self, p: float, t: float, b: float, c: float) -> Tuple[float, float]:
        """
        Iterative calculation of compressibility factor and molar volume.
        
        Args:
            p: Pressure in bar
            t: Temperature in Kelvin
            b: Effective B coefficient
            c: Effective C coefficient
            
        Returns:
            tuple: (v, z) where:
                v: Molar volume
                z: Compressibility factor
                
        Raises:
            RuntimeError: If convergence fails
        """
        rt = self.R * t
        rtp = rt / p
        v = rtp + b
        kk = 0
        
        while True:
            v_old = v
            v = rtp * (1.0 + b/v + c/(v**2))
            kk += 1
            
            if kk > 20:
                raise RuntimeError("No convergence in compressibility calculation")
                
            z = 1.0 + b/v + c/(v**2)
            pa = rt/v * z
            
            if abs(pa - p) < 1.0e-5:
                break
                
        return v, z


def sgerg(x3: float, hs: float, rm: float, x5: float, p: float, tc: float) -> Tuple[float, float, float]:
    """
    Calculate the compression factors of natural gases using a simplified gas analysis.
    
    This is a convenience function that creates a GERG88 instance and calls its
    sgerg method with the provided parameters.
    
    Args:
        x3: Mole fraction CO2 (0.0 -> 0.3)
        hs: Calorific value in MJ/m^3 (20 -> 48)
        rm: Relative density (0.55 -> 0.9)
        x5: Mole fraction H2 (0.0 -> 0.1)
        p: Pressure in bar (0 -> 120)
        tc: Temperature in degrees Celsius (-23 -> 65)
        
    Returns:
        tuple: (x2, z, d) where:
            x2: Calculated molar fraction of nitrogen
            z: Compression factor
            d: Molar density in mol/m^3
            
    Examples:
        >>> import pygerg
        >>> x3 = 0.01  # % CO2
        >>> hs = 37.0  # Calorific value (MJ/m^3)
        >>> rm = 0.7443  # Relative density
        >>> x5 = 0.00  # 0% H2
        >>> p = 8.0  # bar
        >>> tc = 15.0  # °C
        >>> x2, z, d = pygerg.sgerg(x3, hs, rm, x5, p, tc)
        >>> print(f"N2 fraction: {x2:.4f}")
        N2 fraction: 0.0214
        >>> print(f"Compression factor: {z:.6f}")
        Compression factor: 0.970283
        >>> print(f"Molar density: {d:.6f} mol/m^3")
        Molar density: 321.222528 mol/m^3
    """
    calculator = GERG88()
    return calculator.sgerg(x3, hs, rm, x5, p, tc)