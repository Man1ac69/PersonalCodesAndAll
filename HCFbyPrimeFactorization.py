import PrimeNumber as primeFinder


def MakingPrimeNumberList(x):
    primeNumList = []
    i = 2
    while i < x:
        if primeFinder.findPrime(i) == "prime":
            primeNumList.append(i)
        i += 1

    return primeNumList


a = int(input("Enter a number A: "))
b = int(input("Enter a number B: "))

primeNumList = MakingPrimeNumberList(max(a, b))


print(primeNumList)
# i have the prime number list for gradual division
# i need to program the actual prime division loop.




