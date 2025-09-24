from modalg.cayley import U, Z
from modalg.cayley import Cartesian, CartesianMatrix

def main():
    print("Hello from modalg!")


if __name__ == "__main__":

    # U(8).cayley_table().to_latex()
    # Z(8).cayley_table()

    # for i in range(1, 8): 
    #     print(i)
    #     print(Z(8).cyclic_subgroup(i))
    
    print(U(49).unit_group())
    print(U(49).cyclic(1))

