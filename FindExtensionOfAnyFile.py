def SplitFile():
    name = str(input("Enter a filename: "))
    ListAfterDot = name.split(".")
    print("The extension is: ", ListAfterDot[-1])

SplitFile()


