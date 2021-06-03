def roundDown(number):
    return int(number)

def divideByThree(number):
    return float(number)/3

def subtractTwo(number):
    result = number-2
    if result < 0:
        result = 0
    return result


def calculateModuleFuelRequirement(mass):
    dividedByThree = divideByThree(mass)
    roundedDown = roundDown(dividedByThree)
    subtractedTwo =subtractTwo(roundedDown)
    result = subtractedTwo
    return result


def calculateFuelSum(moduleMasses):
    #https://www.geeksforgeeks.org/python-check-if-a-given-object-is-list-or-not/
    if not isinstance(moduleMasses,list):
        exit(f'Input for calculateFuelSum should be a list')
    else:
        result = 0
        for e in moduleMasses:
            result += calculateModuleFuelRequirement(e)
        return result


def calculateFuelForMassAndFuelMass(mass):
    result = calculateModuleFuelRequirement(mass)
    if result > 0:
        result += calculateFuelForMassAndFuelMass(result)
    return result


def calculateFuelSumIncludingFuelMass(masses):
    # https://www.geeksforgeeks.org/python-check-if-a-given-object-is-list-or-not/
    if not isinstance(masses, list):
        exit(f'Input for calculateFuelSumIncludingFuelMass should be a list')
    else:
        result = 0
        for e in masses:
            result += calculateFuelForMassAndFuelMass(e)
        return result