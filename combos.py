import math

def main():
    print('Welcome. Please enter the values for total items and items in the set.')
    print('----------------------------------------------------------------------')

    N = getItem("enter a positive integer for total items: ")
    R = getItem("enter a positive integer for items to be chosen: ")

    print("The number of permutations is", math.perm(N,R))
    print("The number of combinations is", math.comb(N,R))


def getItem(message):
    N = '-1'

    # if no items are entered prompt again
    while ((not N.isdigit())):
        print(message)
        N = input()

    while ((int(N) <= 0) ):
        print(message)
        N = input()

    return int(N)

 

if __name__ == '__main__':  
    main()