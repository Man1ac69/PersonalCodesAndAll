
# finding the factors
def findingFactors(x): 
    i = 1 
    factors = []
    while i <= x: 
        if x % i == 0: 
            factors.append(i)
            i+=1 
            continue 
        else: 
            i+= 1 
    
    return factors

def findingHCF(factorListA, factorListB): 
    i = 0
    j = 0

    while i < len(factorListA):
        currentVarA = factorListA[i]
        j = 0
        while j < len(factorListB):
            if currentVarA == factorListB[j]: 
                hcf = currentVarA
            j += 1
        i += 1
        
    return hcf





