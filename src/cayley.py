from math import gcd
import operator
import numpy as np
import pandas as pd


def cayley_table_generic(units: list, op, modulus: int = None) -> np.ndarray:
    """ Generic Cayley table as a numpy array """
    n = len(units)
    mat = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            result = op(units[i], units[j])
            if modulus:
                result = result % modulus
            mat[i, j] = result
    return mat

class U:
    """ Multiplicative group of integers modulo n """
    def __init__(self, n: int):
        self.n = n
    #
    def unit_group(self) -> list[int]:
        """ List of relatively prime elements in the group """
        units = [k for k in range(1, self.n) if gcd(k, self.n) == 1]
        return units
    #
    def order(self) -> int:
        """ Order of the group """
        return len(self.unit_group())
    #
    def cayley_table(self) -> np.ndarray:
        """ Cayley table as a numpy array """
        units = self.unit_group()
        return cayley_table_generic(units, operator.mul, self.n)
    #
    def cayley_df(self) -> pd.DataFrame: 
        """ Cayley table as a pandas DataFrame """
        units = self.unit_group()
        mat = self.cayley_table() 
        print(f"\nUnits mod {self.n}: {units}\n")
        df = pd.DataFrame(mat, 
            index=units, 
            columns=units
        )
        return df

