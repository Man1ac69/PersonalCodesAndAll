# program to find the length of a list, without using len() 
List = input("Enter a variety of info, seperated by space: ").split()
i = 1

isInRange = True
while isInRange: 
	i += 1
	try: 
		List[i]
	except IndexError:
		isInRange = False

if isInRange == False:
	print("Total number of elements are ", i)


		

