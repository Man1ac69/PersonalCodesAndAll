a = 0
b = 1
c = 0
i = 2

d = int(input("Enter the number of elements you want in you fibonacci sequence: "))
print(a)
print(b)
while (i < d):
    c = a+b
    print(c)
    a = b
    b = c
    i+=1
print("hit the ceiling for max inputs")
