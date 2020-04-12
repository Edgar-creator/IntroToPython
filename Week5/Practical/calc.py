#Problem7
import pretty_print
def calculate_cube(x):
    return x ** 3
def calculate_square(x):
    return x ** 2
def main():
    x = int(input())
    result = calculate_square(x)
    pretty_print.simple_print(result)
    result = calculate_cube(x)
    pretty_print.pro_print(result)
if __name__ == "__main__":
    main()