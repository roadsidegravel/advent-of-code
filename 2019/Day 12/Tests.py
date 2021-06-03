import unittest
from MoonMovementSimulator import Vector,Moon, Simulator,constructMoonListFromPath,constructSimulatorFromPath
from unittest.mock import  patch

#https://www.techbeamers.com/python-code-optimization-tips-tricks/

class GeneralTests(unittest.TestCase):
    def test_Vector456(self):
        vector = Vector(4,5,6)
        self.assertEqual(4,vector.x)
        self.assertEqual(5,vector.y)
        self.assertEqual(6,vector.z)
    def test_Vector673repr(self):
        vector = Vector(6,7,3)
        self.assertEqual('6x,7y,3z',str(vector))
    def test_Moon123(self):
        moon = Moon(1,2,3)
        self.assertEqual(1,moon.positionVector.x)
        self.assertEqual(2,moon.positionVector.y)
        self.assertEqual(3,moon.positionVector.z)
        self.assertEqual(0,moon.velocityVector.x)
        self.assertEqual(0,moon.velocityVector.y)
        self.assertEqual(0,moon.velocityVector.z)
    def test_Mooon932repr(self):
        moon = Moon(9,3,2)
        self.assertEqual('moon with position 9x,3y,2z and velocity 0x,0y,0z',str(moon))
    def test_Example1ConstructMoonListFromPath(self):
        path = 'Examples/Example1'
        referenceString = '[moon with position -1x,0y,2z and velocity 0x,0y,0z, moon with position 2x,-10y,-7z and velocity 0x,0y,0z, moon with position 4x,-8y,8z and velocity 0x,0y,0z, moon with position 3x,5y,-1z and velocity 0x,0y,0z]'
        moonList = constructMoonListFromPath(path)
        reprString = str(moonList)
        self.assertEqual(referenceString,reprString)

class SimulatorTests(unittest.TestCase):
    def test_OneMoonRaisesException(self):
        moonList = [Moon(3,2,1)]
        with self.assertRaises(Exception) as e:
            sim = Simulator(moonList)
        self.assertEqual('Please provide the Simulator with at least two moons',str(e.exception))


class Example1FromPathTests(unittest.TestCase):
    def setUp(self):
        path = 'Examples/Example1'
        self.sim = constructSimulatorFromPath(path)
    def tearDown(self):
        self.sim = None
    def test_Example1Step0(self):
        printOut = self.sim.currentSimDataPrintOut(printInLog=False)
        referenceString0 = 'Simulator state at time step 0'
        referenceString1 = 'moon with position -1x,0y,2z and velocity 0x,0y,0z'
        referenceString2 = 'moon with position 2x,-10y,-7z and velocity 0x,0y,0z'
        referenceString3 = 'moon with position 4x,-8y,8z and velocity 0x,0y,0z'
        referenceString4 = 'moon with position 3x,5y,-1z and velocity 0x,0y,0z'
        self.assertEqual(referenceString0,printOut[0])
        self.assertEqual(referenceString1,printOut[1])
        self.assertEqual(referenceString2,printOut[2])
        self.assertEqual(referenceString3,printOut[3])
        self.assertEqual(referenceString4,printOut[4])
    def test_Example1Step1(self):
        self.sim.takeOneTimeStep()
        printOut = self.sim.currentSimDataPrintOut(printInLog=False)
        referenceString0 = 'Simulator state at time step 1'
        referenceString1 = 'moon with position 2x,-1y,1z and velocity 3x,-1y,-1z'
        referenceString2 = 'moon with position 3x,-7y,-4z and velocity 1x,3y,3z'
        referenceString3 = 'moon with position 1x,-7y,5z and velocity -3x,1y,-3z'
        referenceString4 = 'moon with position 2x,2y,0z and velocity -1x,-3y,1z'
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
        referenceString1 = 'moon with position 5x,-3y,-1z and velocity 3x,-2y,-2z'
        referenceString2 = 'moon with position 1x,-2y,2z and velocity -2x,5y,6z'
        referenceString3 = 'moon with position 1x,-4y,-1z and velocity 0x,3y,-6z'
        referenceString4 = 'moon with position 1x,-4y,2z and velocity -1x,-6y,2z'
        self.assertEqual(referenceString0, printOut[0])
        self.assertEqual(referenceString1, printOut[1])
        self.assertEqual(referenceString2, printOut[2])
        self.assertEqual(referenceString3, printOut[3])
        self.assertEqual(referenceString4, printOut[4])
    def test_Example1Step10(self):
        self.sim.skipToTimeStep(10)
        printOut = self.sim.currentSimDataPrintOut(printInLog=False)
        referenceString0 = 'Simulator state at time step 10'
        referenceString1 = 'moon with position 2x,1y,-3z and velocity -3x,-2y,1z'
        referenceString2 = 'moon with position 1x,-8y,0z and velocity -1x,1y,3z'
        referenceString3 = 'moon with position 3x,-6y,1z and velocity 3x,2y,-3z'
        referenceString4 = 'moon with position 2x,0y,4z and velocity 1x,-1y,-1z'
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
        self.sim.takeStepsTillSimRepeats()
        stepCount = self.sim.currentTimeStep
        self.assertEqual(2772,stepCount)

class Example2FromPathTests(unittest.TestCase):
    def setUp(self):
        path = 'Examples/Example2'
        self.sim = constructSimulatorFromPath(path)
    def tearDown(self):
        self.sim = None
    def test_Example2TotalEnergyStep100(self):
        self.sim.skipToTimeStep(100)
        totalEnergy = self.sim.calculateCurrentTotalEnergy()
        self.assertEqual(1940,totalEnergy)
    def test_Example2RunTillRepeats(self):
        #self.sim.takeStepsTillSimRepeats()
        print(self.sim.currentTimeStep)


if __name__ == '__main__':
    unittest.main()
