a = int(input("Enter a number : "))
i = 2

found = False
while i <= a:
    j = 2
    while (i**j <= a):
        if i**j == a:
            found = True
            break
        j += 1
    
    if found:
        break
    i += 1

if found:
    print(i, j)
else: 
    print("None")
        