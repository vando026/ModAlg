from modalg.groups import U, Z
from modalg.groups import Cartesian, CartesianMatrix

from math import gcd
from sage.all import euler_phi

U10 = U(10)

Z6 = Z(6) 
Z6.generators()


Z8 = Z(8) 
Z8.generators()

## sage 

# Note that in Sage, permutations are applied from left to right.
G = SymmetricGroup (5)
sigma = G ( " (1 ,3) (2 ,5 ,4) " )
sigma * sigma

S = SymmetricGroup(5)
A = G('(1,2)(4,5)')
B = G('(1,5,3)(2,4)')
# Apply B first if you want to do A* B. Start from right to left.
B * A

def rl(a, b):
    # Do right to left composition
    return b * a  # reverse order

# pg 150 ex 1
S3 = SymmetricGroup(3)
S12 = S3((1, 2))
S13 = S3((1, 3))
S23 = S3((2, 3))
S12 * S13
S123 = S3((1, 2, 3))
rl(S12, S13)

# (23)H = (123)H
rl(S123, S13)
rl(S23, S13)



# 3)
U15 = U(15) 
U15.group()
U15.order()


Z8 = Z(8)
Z8.generators()

Zx = Z(3) 
Zx.group()
Zx.cayley_df()
Zx.generators()
Zx.cyclic(2)
Zx.cyclic(1)
Zx.cyclic(0)

[print(U(i).order()) for i in range(1, 21)]

U(10).group()

[U(8).cyclic(i) for i in U(8).group()]

[U(10).cyclic(i) for i in U(10).group()]
