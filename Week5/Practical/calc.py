import pretty_print as p
def calculate_cube(x):
    return x ** 3
def calculate_square(x):
    return x ** 2
def main():
    a = calculate_square(2)
    p.simple_print(a)
    a = calculate_cube(4)
    p.pro_print(a)
if __name__ == "__main__":
    main()