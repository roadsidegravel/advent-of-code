import unittest

from Nanofactory import Production, Nanofactory, CargoHoldToFuel

class TestsProductionClass(unittest.TestCase):
    def test_Manual10OREgives10A(self):
        outcomeDict = {'A':10}
        reagentiaDict = {'ORE': 10}
        prod = Production(outcomeDict,reagentiaDict)
        cost5A = prod.costToProduce('5 A')
        self.assertEqual('10 ORE',cost5A)
        cost12A = prod.costToProduce('12 A')
        self.assertEqual('20 ORE',cost12A)
        cost423A = prod.costToProduce('423 A')
        self.assertEqual('430 ORE',cost423A)
    def test_Manual1A2B3Cgives2D(self):
        outcomeDict = {'D':2}
        reagentiaDict = {'A':1,'B':2,'C':3}
        prod = Production(outcomeDict,reagentiaDict)
        cost1D =prod.costToProduce('1 D')
        self.assertEqual('1 A, 2 B, 3 C',cost1D)
        cost7D = prod.costToProduce('7 D')
        self.assertEqual('4 A, 8 B, 12 C',cost7D)
    def test_repr(self):
        outcomeDict = {'D': 2}
        reagentiaDict = {'A': 1, 'B': 2, 'C': 3}
        prod = Production(outcomeDict,reagentiaDict)
        prodString = str(prod)
        compareString = f'{reagentiaDict} => {outcomeDict}'
        self.assertEqual(compareString,prodString)

class TestsNanofactoryClassExample1(unittest.TestCase):
    def setUp(self):
        self.path = 'Example1'
        self.nanofactory = Nanofactory(self.path)
    def tearDown(self):
        self.nanofactory = None
    def test_Example1Repr(self):
        #print(self.nanofactory)
        self.assertTrue(True)
    def test_Example1Produce5A(self):
        cost = self.nanofactory.costToProduce('7 A')
        self.assertEqual(10,cost,f'{self.path}')
    def test_Example1Produce3B(self):
        cost = self.nanofactory.costToProduce('1 B')
        self.assertEqual(1,cost,f'{self.path}')
    def test_Example1Produce1C(self):
        cost = self.nanofactory.costToProduce('1 C')
        self.assertEqual(11,cost,f'{self.path}')
    def test_Example1Produce1D(self):
        cost = self.nanofactory.costToProduce('1 D')
        self.assertEqual(21,cost,f'{self.path}')
    def test_Example1Produce1E(self):
        cost = self.nanofactory.costToProduce('1 E')
        self.assertEqual(31,cost,f'{self.path}')
    def test_Example1Produce1FUEL(self):
        cost = self.nanofactory.costToProduce('1 FUEL')
        self.assertEqual(31,cost,f'{self.path}')

class TestsNanofactoryClassExample2(unittest.TestCase):
    def setUp(self):
        self.path = 'Example2'
        self.nanofactory = Nanofactory(self.path)
    def tearDown(self):
        self.nanofactory = None
    def test_Example2Produce1FUEL(self):
        cost1FUEL = self.nanofactory.costToProduce('1 FUEL')
        self.assertEqual(165,cost1FUEL,f'{self.path}')

class TestsNanofactoryClassExample3(unittest.TestCase):
    def setUp(self):
        self.path = 'Example3'
        self.nanofactory = Nanofactory(self.path)
    def tearDown(self):
        self.nanofactory = None
    def test_Example3Produce1FUEL(self):
        cost1FUEL = self.nanofactory.costToProduce('1 FUEL')
        self.assertEqual(13312,cost1FUEL,f'{self.path}')
    def test_Example3CargoHoldToFuel(self):
        cargoHold = CargoHoldToFuel(self.nanofactory)
        fuel = cargoHold.fuel
        self.assertEqual(82892753,fuel,f'{self.path}')

class TestsNanofactoryClassExample4(unittest.TestCase):
    def setUp(self):
        self.path = 'Example4'
        self.nanofactory = Nanofactory(self.path)
    def tearDown(self):
        self.nanofactory = None
    def test_Example4Produce1FUEL(self):
        cost1FUEL = self.nanofactory.costToProduce('1 FUEL')
        self.assertEqual(180697,cost1FUEL,f'{self.path}')
    def test_Example4CargoHoldToFuel(self):
        cargoHold = CargoHoldToFuel(self.nanofactory)
        fuel = cargoHold.fuel
        self.assertEqual(5586022,fuel,f'{self.path}')

class TestsNanofactoryClassExample5(unittest.TestCase):
    def setUp(self):
        self.path = 'Example5'
        self.nanofactory = Nanofactory(self.path)
    def tearDown(self):
        self.nanofactory = None
    def test_Example5Produce1FUEL(self):
        cost1FUEL = self.nanofactory.costToProduce('1 FUEL')
        self.assertEqual(2210736,cost1FUEL,f'{self.path}')
    def test_Example5CargoHoldToFuel(self):
        cargoHold = CargoHoldToFuel(self.nanofactory)
        fuel = cargoHold.fuel
        self.assertEqual(460664,fuel,f'{self.path}')


if __name__ == '__main__':
    unittest.main()
