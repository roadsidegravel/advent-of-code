import unittest
from MoonMovementSimulatorFast import MoonFast, SimulatorFast,constructMoonListFromPathFast,constructSimulatorFromPathFast
from unittest.mock import  patch


#https://www.techbeamers.com/python-code-optimization-tips-tricks/



class GeneralTests(unittest.TestCase):
    def test_Moon123(self):
        moon = MoonFast(1,2,3)
        self.assertEqual(1,moon.positionVector[0])
        self.assertEqual(2,moon.positionVector[1])
        self.assertEqual(3,moon.positionVector[2])
        self.assertEqual(0,moon.velocityVector[0])
        self.assertEqual(0,moon.velocityVector[1])
        self.assertEqual(0,moon.velocityVector[2])
    def test_Mooon932repr(self):
        moon = MoonFast(9,3,2)
        self.assertEqual('moon with position [9, 3, 2] and velocity [0, 0, 0]',str(moon))
    def test_Example1ConstructMoonListFromPath(self):
        path = 'Example1'
        referenceString = '[moon with position [-1, 0, 2] and velocity [0, 0, 0], moon with position [2, -10, -7] and velocity [0, 0, 0], moon with position [4, -8, 8] and velocity [0, 0, 0], moon with position [3, 5, -1] and velocity [0, 0, 0]]'
        moonList = constructMoonListFromPathFast(path)
        reprString = str(moonList)
        self.assertEqual(referenceString,reprString)

class SimulatorTests(unittest.TestCase):
    def test_OneMoonRaisesException(self):
        moonList = [MoonFast(3,2,1)]
        with self.assertRaises(Exception) as e:
            sim = SimulatorFast(moonList)
        self.assertEqual('Please provide the Simulator with at least two moons',str(e.exception))


class Example1FromPathTests(unittest.TestCase):
    def setUp(self):
        path = 'Example1'
        self.sim = constructSimulatorFromPathFast(path)
    def tearDown(self):
        self.sim = None
    def test_Example1Step0(self):
        printOut = self.sim.currentSimDataPrintOut(printInLog=False)
        referenceString0 = 'Simulator state at time step 0'
        referenceString1 = 'moon with position [-1, 0, 2] and velocity [0, 0, 0]'
        referenceString2 = 'moon with position [2, -10, -7] and velocity [0, 0, 0]'
        referenceString3 = 'moon with position [4, -8, 8] and velocity [0, 0, 0]'
        referenceString4 = 'moon with position [3, 5, -1] and velocity [0, 0, 0]'
        self.assertEqual(referenceString0,printOut[0])
        self.assertEqual(referenceString1,printOut[1])
        self.assertEqual(referenceString2,printOut[2])
        self.assertEqual(referenceString3,printOut[3])
        self.assertEqual(referenceString4,printOut[4])
    def test_Example1Step1(self):
        self.sim.takeOneTimeStep()
        printOut = self.sim.currentSimDataPrintOut(printInLog=False)
        referenceString0 = 'Simulator state at time step 1'
        referenceString1 = 'moon with position [2, -1, 1] and velocity [3, -1, -1]'
        referenceString2 = 'moon with position [3, -7, -4] and velocity [1, 3, 3]'
        referenceString3 = 'moon with position [1, -7, 5] and velocity [-3, 1, -3]'
        referenceString4 = 'moon with position [2, 2, 0] and velocity [-1, -3, 1]'
        self.assertEqual(referenceString0, printOut[0])
        self.assertEqual(referenceString1, printOut[1])
        self.assertEqual(referenceString2, printOut[2])
        self.assertEqual(referenceString3, printOut[3])
        self.assertEqual(referenceString4, printOut[4])
    def test_Example1Step2(self):
        self.sim.takeOneTimeStep()
        self.sim.takeOneTimeStep()
        printOut = self.sim.currentSimDataPrintOut(printInLog=False)
        referenceString0 = 'Simulator state at time step 2'
        referenceString1 = 'moon with position [5, -3, -1] and velocity [3, -2, -2]'
        referenceString2 = 'moon with position [1, -2, 2] and velocity [-2, 5, 6]'
        referenceString3 = 'moon with position [1, -4, -1] and velocity [0, 3, -6]'
        referenceString4 = 'moon with position [1, -4, 2] and velocity [-1, -6, 2]'
        self.assertEqual(referenceString0, printOut[0])
        self.assertEqual(referenceString1, printOut[1])
        self.assertEqual(referenceString2, printOut[2])
        self.assertEqual(referenceString3, printOut[3])
        self.assertEqual(referenceString4, printOut[4])
    def test_Example1Step10(self):
        self.sim.skipToTimeStep(10)
        printOut = self.sim.currentSimDataPrintOut(printInLog=False)
        referenceString0 = 'Simulator state at time step 10'
        referenceString1 = 'moon with position [2, 1, -3] and velocity [-3, -2, 1]'
        referenceString2 = 'moon with position [1, -8, 0] and velocity [-1, 1, 3]'
        referenceString3 = 'moon with position [3, -6, 1] and velocity [3, 2, -3]'
        referenceString4 = 'moon with position [2, 0, 4] and velocity [1, -1, -1]'
        self.assertEqual(referenceString0, printOut[0])
        self.assertEqual(referenceString1, printOut[1])
        self.assertEqual(referenceString2, printOut[2])
        self.assertEqual(referenceString3, printOut[3])
        self.assertEqual(referenceString4, printOut[4])
    def test_Example1SkipToMinus2RaisesValueError(self):
        with self.assertRaises(ValueError) as e:
            self.sim.skipToTimeStep(-2)
        self.assertEqual('time can only move forward, pick a later timeStep to skip to, current 0 skip to -2',str(e.exception))
    def test_Example1TotalEnergyStep10(self):
        self.sim.skipToTimeStep(10)
        totalEnergy = self.sim.calculateCurrentTotalEnergy()
        self.assertEqual(179,totalEnergy)
    def test_Example1RunTillRepeats(self):
        intervalTillrepeats = self.sim.takeStepsTillSimRepeats()
        self.assertEqual(2772,intervalTillrepeats)
        print('example 1 ok')

class Example2FromPathTests(unittest.TestCase):
    def setUp(self):
        path = 'Example2'
        self.sim = constructSimulatorFromPathFast(path)
    def tearDown(self):
        self.sim = None
    def test_Example2TotalEnergyStep100(self):
        self.sim.skipToTimeStep(100)
        totalEnergy = self.sim.calculateCurrentTotalEnergy()
        self.assertEqual(1940,totalEnergy)
    def test_Example2RunTillRepeats(self):
        intervalTillRepeats = self.sim.takeStepsTillSimRepeats()
        print(4686774924,intervalTillRepeats)


if __name__ == '__main__':
    unittest.main()
