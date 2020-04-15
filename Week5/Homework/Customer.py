import Productcheck as P
def buy(product, num, price):
    if P.check(product,num) is True:
        print("You bought %s and spent %d" %(product,num*price))
    else:
        print("Sorry! We are out of this product.")
def main():
    product = input()
    num = int(input())
    price = int(input())
    buy(product, num, price)
if __name__ == "__main__":
    main()