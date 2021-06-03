import unittest
#unittest most used asserts:
#self.assertEqual(a,b)
#self.assertFalse(bool)
#self.assertTrue(bool)
#self.assertRaises(error)
#https://docs.python.org/3/library/unittest.html
#def setUp(self):
#def tearDown(self):
#def suite for custom test suite building (which tests to run)

import fuelCalculation
class testFuelCalculation(unittest.TestCase):
    def test_roundDown2p4(self):
        number = 2.4
        result= fuelCalculation.roundDown(number)
        self.assertEqual(2,result,f'rounding down {number} should give 2, not {result}')
    def test_rounddown4p2(self):
        number = 4.9
        result = fuelCalculation.roundDown(number)
        self.assertEqual(4, result, f'rounding down {number} should give 4, not {result}')
    def test_divideByThree9(self):
        number = 12
        result = fuelCalculation.divideByThree(number)
        self.assertEqual(4, result, f'{number} divided by 3 should be 4, not {result}')
    def test_divideByThree6p3(self):
        number = 6.3
        result = fuelCalculation.divideByThree(number)
        self.assertEqual(2.1, result, f'{number} divided by 3 should be 2.1, not {result}')
    def test_subtractTwo7(self):
        number = 7
        result = fuelCalculation.subtractTwo(number)
        self.assertEqual(5, result, f'{number} minus 2 should be 5, not {result}')
    def test_subtractTwo1(self):
        number = 1
        result = fuelCalculation.subtractTwo(number)
        self.assertEqual(0, result, f'{number} minus 2 should be 0, not {result}')
    #example given in day 1
    def test_CalculateModuleFuelRequirement12(self):
        mass = 12
        result = fuelCalculation.calculateModuleFuelRequirement(mass)
        self.assertEqual(2, result, f'fuel cost for {mass} should be 2, not {result}')
    # example given in day 1
    def test_CalculateModuleFuelRequirement14(self):
        mass = 14
        result = fuelCalculation.calculateModuleFuelRequirement(mass)
        self.assertEqual(2, result, f'fuel cost for {mass} should be 2, not {result}')
    # example given in day 1
    def test_CalculateModuleFuelRequirement1969(self):
        mass = 1969
        result = fuelCalculation.calculateModuleFuelRequirement(mass)
        self.assertEqual(654, result, f'fuel cost for {mass} should be 654, not {result}')
    # example given in day 1
    def test_CalculateModuleFuelRequirement100756(self):
        mass = 100756
        result = fuelCalculation.calculateModuleFuelRequirement(mass)
        self.assertEqual(33583, result, f'fuel cost for {mass} should be 33583, not {result}')
    def test_CalculateFuelSum12and14(self):
        moduleMasses = [12,14]
        result = fuelCalculation.calculateFuelSum(moduleMasses)
        cost12 = 2
        cost14 = 2
        cost12and14 = cost12+cost14
        self.assertEqual(cost12and14,result,f'fuel cost for 12 and 14 should be 4, not {result}')
    def test_CalculateFuelSumAllFourExamples(self):
        moduleMasses = [12,14,1969,100756]
        result = fuelCalculation.calculateFuelSum(moduleMasses)
        cost12 = 2
        cost14 = 2
        cost1969 = 654
        cost100756 = 33583
        costTotal = cost12+cost14+cost1969+cost100756
        self.assertEqual(costTotal,result,f'fuel cost for all four examples combined should be {costTotal}, not {result}')
    #problem encountered, divide by three cant handle string input
    def test_DivideByThreeString3(self):
        number = '3'
        result = fuelCalculation.divideByThree(number)
        self.assertEqual(1, result, f'divideByThree should be able to handle string input')
    #example given in part 2
    def test_CalculateFuelForMassAndFuelMass14(self):
        mass = 14
        result = fuelCalculation.calculateFuelForMassAndFuelMass(mass)
        self.assertEqual(2, result, f'The total fuel cost, including the fuel itself for {mass} should be 2')
    #example given in part 2
    def test_CalculateFuelForMassAndFuelMass1969(self):
        mass = 1969
        result = fuelCalculation.calculateFuelForMassAndFuelMass(mass)
        self.assertEqual(966, result, f'The total fuel cost, including the fuel itself for {mass} should be 966')
    #example given in part 2
    def test_CalculateFuelForMassAndFuelMass100756(self):
        mass = 100756
        result = fuelCalculation.calculateFuelForMassAndFuelMass(mass)
        self.assertEqual(50346, result, f'The total fuel cost, including the fuel itself for {mass} should be 50346')
    def test_CalculateFuelSumIncludingFuelMass14and1969(self):
        mass1 = 14
        mass2 = 1969
        masses = [mass1,mass2]
        totalFuel1 = 2
        totalFuel2 = 966
        total = totalFuel1+totalFuel2
        result = fuelCalculation.calculateFuelSumIncludingFuelMass(masses)
        self.assertEqual(total,result,f'The sum, including the fuel mass, for {mass1} and {mass2} should be {total}, not {result}')
    def test_CalculateFuelSumIncludingFuelMass14and1969and100756(self):
        mass1 = 14
        mass2 = 1969
        mass3 = 100756
        masses = [mass1,mass2, mass3]
        totalFuel1 = 2
        totalFuel2 = 966
        totalFuel3 = 50346
        total = totalFuel1+totalFuel2+totalFuel3
        result = fuelCalculation.calculateFuelSumIncludingFuelMass(masses)
        self.assertEqual(total,result,f'The sum, including the fuel mass, for {mass1}, {mass2} and {mass3} should be {total}, not {result}')



