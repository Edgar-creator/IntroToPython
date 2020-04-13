import Productcheck
def buy(product, num, price):
    if Productcheck.check(product,num) is True:
        print("You bought product and spent %d" %(num*price))
    else:
        print("Sorry! We are out of this product.")
def main():
    product = input()
    num = int(input())
    price = int(input())
    result = buy(product, num, price)
if __name__ == "__main__":
    main()