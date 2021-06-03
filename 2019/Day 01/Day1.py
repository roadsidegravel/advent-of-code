from fuelCalculation import calculateFuelSum, calculateFuelSumIncludingFuelMass
path = 'inputDay1'
#https://www.pythonforbeginners.com/files/with-statement-in-python
rawData = []
with open(path) as file:
    rawData = file.readlines()

result = calculateFuelSum(rawData)
print(f'The total fuel cost for day 1, part 1 is: {result}')
resultPart2 = calculateFuelSumIncludingFuelMass(rawData)
print(f'The total fuel cost for day 1, part 2 is: {resultPart2}')