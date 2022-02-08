# attempting to find LCM
def MultipleList(x, y):
    i = 1
    multipleList = []
    while i < y:
        multipleList.append(x*i)
        i += 1

    return multipleList

def findLCM(multipleListA, multipleListB):
    lcmFound = False
    i = 0
    while i < len(multipleListA):
        currentVar = multipleListA[i]
        j = 0
        while j < len(multipleListB):
            if currentVar == multipleListB[j]:
                lcm = currentVar
                lcmFound = True
            j+= 1
        if lcmFound:
            break
        i +=1


    if lcmFound:
        return "LCM is : ", lcm
    else:
        return "LCM is: ", multipleListA[0] * multipleListB[0]














