def Factorial(n):
    if n == 0:
        return 1
    else:
        return n * Factorial(n-1)


a = int(input("Enter a number to find factorial of: "))
print(Factorial(a))


