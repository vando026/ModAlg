from math import gcd
import numpy as np
import pandas as pd

class U:
    """ Multiplicative group of integers modulo n """
    def __init__(self, n: int):
        self.n = n
    #
    def unit_group(self) -> list[int]:
        """ List of relatively prime elemets in the group """
        units = [k for k in range(1, self.n) if gcd(k, self.n) == 1]
        return units
    #
    def order(self) -> int:
        """ Order of the group """
        return len(self.unit_group())
    #
    def cayley_table(self) -> np.ndarray:
        """ Cayley table as a numpy array """
        rown = coln = self.order()
        units = self.unit_group()
        mat = np.empty((rown, coln))
        for i, x in enumerate(units):
            for j, y in enumerate(units):   
                mat[i, j] = (x * y) % self.n
        return mat
    #
    def cayley_df(self) -> pd.DataFrame: 
        """ Cayley table as a pandas DataFrame """
        mat = self.cayley_table() 
        df = pd.DataFrame(mat, 
            index=self.unit_group(), 
            columns=self.unit_group()
        )
        return df

tt = U(4)
tt.unit_group()
tt.order()
tt.cayley_df()
print(tt.cayley_table().astype(int))

u10 = U(10)
u10.cayley_df()


