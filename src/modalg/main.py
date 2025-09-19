from modalg.cayley import U, Z
from modalg.cayley import Cartesian, CartesianMatrix

def main():
    print("Hello from modalg!")


if __name__ == "__main__":

U(8).cayley_table().to_df()

    tt = U(12)
    tt.unit_group()
    tt.order()
    print(tt.cayley_df())

