# fraction reducer
import HCFFinder as hcf

numerator = int(input("Enter numerator: "))
denominator = int(input("Enter denominator: "))

print(f"The Fraction is {numerator}/{denominator}")
numFactors = hcf.findingFactors(numerator)
denFactors = hcf.findingFactors(denominator)
FractionHCF = hcf.findingHCF(numFactors, denFactors)
print(f"The hcf of the numerator and denominator is {FractionHCF}")
reducedNum = int(numerator/FractionHCF)
reducedDen = int(denominator/FractionHCF)
print(f"Therefore the reduced fraction is {reducedNum}/{reducedDen}")
