import pretty_print
def calculate_cube(x):
    return x **3
def calculate_square(x):
    return x ** 2
def main():
    a = calculate_square(2)
    pretty_print.simple_print(a)
    a = calculate_cube(4)
    pretty_print.pro_print(a)
if __name__ == "__main__":
    main()