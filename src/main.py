from cayley import U


def main():
    print("Hello from modalg!")


if __name__ == "__main__":

    tt = U(4)
    tt.unit_group()
    tt.order()
    print(tt.cayley_df())

    u10 = U(10)
    print(u10.cayley_df())
