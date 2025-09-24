from math import gcd
import operator
import numpy as np
import pandas as pd
from typing import Callable
from dataclasses import dataclass

@dataclass
class CartesianMatrix:
    matrix: np.ndarray
    labels: list[int]

    def to_df(self) -> pd.DataFrame:
        return pd.DataFrame(self.matrix, index=self.labels, columns=self.labels)

    def to_latex(self) -> None:
        mat =  self.matrix
        labels = np.array(self.labels).reshape(-1, 1)
        hmat = np.hstack([labels, mat])
        print("\\begin{tabular}{c|" + "c"*len(self.labels) + "}")
        print(" & " + " & ".join(str(x) for x in self.labels), r"\\")
        print("\\hline")
        for irow in hmat: 
            print(" & ".join(str(x) for x in irow), r"\\")
        print("\\hline")
        print("\\end{tabular}")
        

class Cartesian:

    def __init__(self, x: list[int]):
        self.x = x

    def matrix(
            self,
            op: Callable[[int, int], int]
        ) -> CartesianMatrix:
        n = len(self.x)
        mat = np.zeros((n, n), dtype=int)
        for i, v in enumerate(self.x):
            for j, w in enumerate(self.x):
                mat[i, j] = op(v, w)
        return CartesianMatrix(mat, self.x)

class U(Cartesian):
    """ Multiplicative group of integers modulo n """
    def __init__(self, n: int):
        self.n = n
        super().__init__(self.unit_group())
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
    def cayley_table(self) -> CartesianMatrix:
        """ Cayley table as a CartesianMatrix """
        return self.matrix(lambda a, b: (a * b) % self.n)
    #
    def cayley_df(self) -> pd.DataFrame:
        """ Cayley table as a pandas DataFrame """
        units = self.unit_group()
        cayley_matrix = self.cayley_table()
        print(f"\nUnits mod {self.n}: {units}\n")
        return cayley_matrix.to_df()

    def cyclic(self, a, length: int = 10) -> list[int]:
        """ Generate the cyclic subgroup"""
        if a not in self.unit_group():
            raise Exception("element <a> not in unit group.")
        sub = [a**i for i in range(self.order() + length)]
        return  list(set([k % self.n for k in sub]))


class Z(Cartesian):
    """ Additive group of integers modulo n """
    def __init__(self, n: int):
        self.n = n
        self.elements = list(range(self.n))
        super().__init__(self.elements)
    #
    def unit_group(self) -> list[int]:
        """ List of elements in the group """
        return self.elements

    def order(self) -> int:
        """ Order of the group """
        return self.n

    def cayley_table(self) -> np.ndarray:
        """ Cayley table as a numpy array """
        return self.matrix(lambda a, b: (a + b) % self.n)
    #
    def cayley_df(self) -> pd.DataFrame: 
        """ Cayley table as a pandas DataFrame """
        cayley_matrix = self.cayley_table()
        print(f"\nElements mod {self.n}: {self.elements}\n")
        return cayley_matrix.to_df()

    def cyclic(self, k: int) -> list[int]:
        """ Generate the cyclic subgroup of order k """
        if k <= 0 or k > self.n:
            raise ValueError("k must be in the range 1 to n")
        return list(set([(i * k) % self.n for i in range(self.n)]))
    
    def generators(self) -> list[int]:
        """ List of generators of the group """
        print(f"The generators:")
        gs = [k for k in range(1, self.n) if gcd(k, self.n) == 1]
        return gs

