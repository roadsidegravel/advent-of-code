import unittest
from unittest.mock import patch
# unittest most used asserts:
# self.assertEqual(a,b)
# self.assertFalse(bool)
# self.assertTrue(bool)
# self.assertRaises(error)
# https://docs.python.org/3/library/unittest.html
# def setUp(self): (er is ook setUpClass en setUpModule voor als er code gerund wordt voor een nieuwe class of nieuwe module getest wordt, te vermijden wel, ivm test isolation
# def tearDown(self):
# https://queirozf.com/entries/python-unittest-examples-mocking-and-patching
# def suite for custom test suite building (which tests to run)
# @unittest.skip, skipIf, skipUnless voor bv 'zitten we op windows, test dit', 'hebben we internet? test dit niet'
# with self.subTest voor meerdere testjes in één test
# https://dev.to/vergeev/how-to-test-input-processing-in-python-3
# https://stackoverflow.com/questions/21046717/python-mocking-raw-input-in-unittests
# https://stackoverflow.com/questions/18161330/using-unittest-mock-to-patch-input-in-python-3
# https://stackoverflow.com/questions/129507/how-do-you-test-that-a-python-function-throws-an-exception
# refactoring/code cleaning/restructuring
# @dinges, setter getter enzo (voorlopig nog niet gebruikt)
# kunt functies nesten, en classes

from Intcode import computer as IntcodeComputer
from Intcode import constructComputerFromFile
from Intcode import amplifier
from Intcode import amplifiersInSeries
from Intcode import constructAmplifiersInSeriesFromFile
from Intcode import FindMaxThrusterSignalFromPath
from Intcode import amplifiersInSeriesWithFeedbackLoop
from Intcode import constructAmplifiersInSeriesWithFeedbackLoopFromFile
from Intcode import FindMaxThrusterFeedbackLoopSignalFromPath

class Opcode1PositionMode(unittest.TestCase):
    def test_takingStepOpcode1with_1_1_1_1ReturnsMessage(self):
        intcode = [1,1,1,1]
        testComputer = IntcodeComputer(intcode)
        message = testComputer.takeStep()
        self.assertEqual('opcode 1 at position 0 processed',message)
    def test_takingStepOpcode1with_1_1_1_1ChangesIntcode(self):
        intcode = [1, 1, 1, 1]
        testComputer = IntcodeComputer(intcode)
        testComputer.takeStep()
        self.assertEqual([1,2,1,1],testComputer.intcode)
    def test_takingStepOpcode1with_1_0_0_3ReturnsMessage(self):
        intcode = [1,0,0,3]
        testComputer = IntcodeComputer(intcode)
        message = testComputer.takeStep()
        self.assertEqual('opcode 1 at position 0 processed',message)
    def test_takingStepOpcode1with_1_0_0_3ChangesIntcode(self):
        intcode = [1, 0, 0, 3]
        testComputer = IntcodeComputer(intcode)
        testComputer.takeStep()
        self.assertEqual([1,0,0,2],testComputer.intcode)

class Opcode1ImmediateMode(unittest.TestCase):
    def test_running1101_5_7_99ChangesIntcode(self):
        intcode = [1101,5,7,3,99]
        testComputer = IntcodeComputer(intcode)
        testComputer.run()
        self.assertEqual([1101, 5, 7, 12, 99],testComputer.intcode)
    def test_running1001_0_120_3_99ChangesIntcode(self):
        intcode = [1001, 0, 120, 3, 99]
        testComputer = IntcodeComputer(intcode)
        testComputer.run()
        self.assertEqual([1001, 0, 120, 1121, 99],testComputer.intcode)
    def test_immediateModeOpcode1ValueErrorParameter3(self):
        intcode = [10001, 0, 0, 99]
        testComputer = IntcodeComputer(intcode)
        with self.assertRaises(ValueError) as e:
            testComputer.run()
        self.assertEqual('Parameters that an instruction writes to will never be in immediate mode.', str(e.exception))

class Opcode1RelativeMode(unittest.TestCase):
    def test_step2201_1_1_1IntcodeChanges(self):
        intcode = [2201,1,1,1]
        testComputer = IntcodeComputer(intcode)
        testComputer.takeStep()
        self.assertEqual([2201, 2, 1, 1], testComputer.intcode)
    def test_step22201_2_2_1IntcodeChanges(self):
        intcode = [22201,2,2,1]
        testComputer = IntcodeComputer(intcode)
        testComputer.takeStep()
        self.assertEqual([22201, 4, 2, 1], testComputer.intcode)

class Opcode2PositionMode(unittest.TestCase):
    def test_takingStepOpcode2with_2_1_1_1ReturnsMessage(self):
        intcode = [2,1,1,1]
        testComputer = IntcodeComputer(intcode)
        message = testComputer.takeStep()
        self.assertEqual('opcode 2 at position 0 processed',message)
    def test_takingStepOpcode2with_2_1_1_1ChangesIntcode(self):
        intcode = [2,1,1,1]
        testComputer = IntcodeComputer(intcode)
        testComputer.takeStep()
        self.assertEqual([2,1,1,1],testComputer.intcode)
    def test_takingStepOpcode2with_2_0_0_3ReturnsMessage(self):
        intcode = [2,0,0,3]
        testComputer = IntcodeComputer(intcode)
        message = testComputer.takeStep()
        self.assertEqual('opcode 2 at position 0 processed',message)
    def test_takingStepOpcode2with_2_0_0_3ChangesIntcode(self):
        intcode = [2,0,0,3]
        testComputer = IntcodeComputer(intcode)
        testComputer.takeStep()
        self.assertEqual([2,0,0,4],testComputer.intcode)

class Opcode2ImmediateMode(unittest.TestCase):
    def test_immediateModeOpcode2(self):
        intcode = [1102, 5, 7, 3, 99]
        testComputer = IntcodeComputer(intcode)
        testComputer.run()
        self.assertEqual([1102, 5, 7, 35, 99], testComputer.intcode)
    def test_immediateModeOpcode2Mixed(self):
        intcode = [1002, 0, 2, 3, 99]
        testComputer = IntcodeComputer(intcode)
        testComputer.run()
        self.assertEqual([1002, 0, 2, 2004, 99], testComputer.intcode)
    def test_immediateModeOpcode2ValueErrorParamater3(self):
        intcode = [10002, 0, 0, 99]
        testComputer = IntcodeComputer(intcode)
        with self.assertRaises(ValueError) as e:
            testComputer.run()
        self.assertEqual('Parameters that an instruction writes to will never be in immediate mode.', str(e.exception))

class Opcode2RelativeMode(unittest.TestCase):
    def test_takingStep2202_0_0_3ChangesIntcode(self):
        intcode = [2202,0,0,3]
        testComputer = IntcodeComputer(intcode)
        testComputer.takeStep()
        self.assertEqual([2202,0,0,4848804],testComputer.intcode)

class Opcode3PositionMode(unittest.TestCase):
    def test_runningOpcode3WithInput5MessageLog(self):
        intcode = [3, 1, 99]
        userInput = 5
        testComputer = IntcodeComputer(intcode)
        with patch('builtins.input', lambda *args: userInput):
            testComputer.run()
        self.assertEqual(2, len(testComputer.log))
        self.assertEqual('opcode 3 at position 0 processed',testComputer.log[0])
        self.assertEqual('opcode 99, exiting',testComputer.log[1])
    def test_runningOpcode3WithInput5IntcodeChanges(self):
        intcode = [3, 1, 99]
        userInput = 5
        testComputer = IntcodeComputer(intcode)
        with patch('builtins.input', lambda *args: userInput):
            testComputer.run()
        self.assertEqual([3, 5, 99],testComputer.intcode)
    def test_runningOpcode3input5_opcode3input3InputList(self):
        intcode = [3, 0, 3, 1, 99]
        inputs = [5, 3]
        testComputer = IntcodeComputer(intcode)
        testComputer.inputs = inputs
        testComputer.run()
        self.assertEqual([],testComputer.inputs)
        self.assertEqual([5, 3, 3, 1, 99],testComputer.intcode)
    def test_opcode3AutomaticModePausesIntcomputerTillInputIsgiven(self):
        intcode = [3, 1, 99]
        automaticTestComputer = IntcodeComputer(intcode, True)
        automaticTestComputer.run()
        self.assertFalse(automaticTestComputer.running)
        automaticTestComputer.automaticModeTakeInputAndUnpauze(5)
        self.assertEqual([3, 5, 99], automaticTestComputer.intcode)
        self.assertEqual(3, len(automaticTestComputer.log))
        self.assertEqual('pausing for input at position 0', automaticTestComputer.log[0])
        self.assertEqual('opcode 3 at position 0 processed', automaticTestComputer.log[1])
        self.assertEqual('opcode 99, exiting', automaticTestComputer.log[2])

class Opcode3ImmediateMode(unittest.TestCase):
    def test_immediateModeOpcode3ValueErrorParameterA(self):
        intcode = [103, 1, 99]
        testComputer = IntcodeComputer(intcode)
        with self.assertRaises(ValueError) as e:
            userInput = 4
            with patch('builtins.input', lambda *args: userInput):
                testComputer.run()
        self.assertEqual('Parameters that an instruction writes to will never be in immediate mode.', str(e.exception))


class Opcode4PositionMode(unittest.TestCase):
    def test_running4_0_99OutputPrint(self):
        intcode = [4,0,99]
        testComputer = IntcodeComputer(intcode)
        with patch('builtins.print') as p:
            testComputer.run()
        p.assert_called_with(4)
    def test_running4_0_99OutputStored(self):
        intcode = [4,0,99]
        testComputer = IntcodeComputer(intcode)
        with patch('builtins.print') as p:
            testComputer.run()
        self.assertEqual(4, testComputer.outputs[0])

class Opcode4ImmediateMode(unittest.TestCase):
    def test_immediateModeOpcode4ParameterAprints(self):
        intcode = [104, 5, 99, 3, 4, 5]
        testComputer = IntcodeComputer(intcode)
        with patch('builtins.print') as p:
            testComputer.run()
        p.assert_called_with(5)
    def test_immediateModeOpcode4ParameterAStoresOutput(self):
        intcode = [104, 5, 99, 3, 4, 5]
        testComputer = IntcodeComputer(intcode)
        with patch('builtins.print') as p:
            testComputer.run()
        self.assertEqual(5, testComputer.outputs[0])

class Opcode5positionMode(unittest.TestCase):
    def test_opcode5OnZeroDoNothing(self):
        intcode = [5, 6, 7, 1, 4, 4, 0, 99]
        testComputer = IntcodeComputer(intcode)
        testComputer.run()
        self.assertEqual(len(testComputer.log), 3)
        self.assertEqual(testComputer.log[0], f'opcode 5 at position 0 processed')
        self.assertEqual(testComputer.log[1], f'opcode 1 at position 3 processed')
        self.assertEqual(testComputer.log[2], f'opcode 99, exiting')
    def test_opcode5OnNotZeroJump(self):
        intcode = [5, 7, 1, 1, 4, 4, 6, 99]
        testComputer = IntcodeComputer(intcode)
        testComputer.run()
        self.assertEqual(len(testComputer.log), 2)
        self.assertEqual(testComputer.log[0], f'opcode 5 at position 0 processed')
        self.assertEqual(testComputer.log[1], f'opcode 99, exiting')

class Opcode5immediateMode(unittest.TestCase):
    def test_opcode5ImediateModeJump(self):
        intcode = [1105, 1, 7, 4, 0, 4, 0, 99]
        testComputer = IntcodeComputer(intcode)
        testComputer.run()
        self.assertEqual(len(testComputer.log), 2)
        self.assertEqual(testComputer.log[0], f'opcode 5 at position 0 processed')
        self.assertEqual(testComputer.log[1], f'opcode 99, exiting')

    def test_opcode5ImediateModeDontJump(self):
        intcode = [1105, 0, 7, 3, 0, 3, 0, 99]
        testComputer = IntcodeComputer(intcode)
        testComputer.inputs = [1, 5]
        testComputer.run()
        self.assertEqual(len(testComputer.log), 4)
        self.assertEqual(testComputer.log[0], f'opcode 5 at position 0 processed')
        self.assertEqual(testComputer.log[1], f'opcode 3 at position 3 processed')
        self.assertEqual(testComputer.log[2], f'opcode 3 at position 5 processed')
        self.assertEqual(testComputer.log[3], f'opcode 99, exiting')

class Opcode6positionMode(unittest.TestCase):
    def test_opcode6OnNotZeroDoNothing(self):
        intcode = [6, 6, 7, 1, 4, 4, 1, 99]
        testComputer = IntcodeComputer(intcode)
        testComputer.run()
        self.assertEqual(len(testComputer.log), 3)
        self.assertEqual(testComputer.log[0], f'opcode 6 at position 0 processed')
        self.assertEqual(testComputer.log[1], f'opcode 1 at position 3 processed')
        self.assertEqual(testComputer.log[2], f'opcode 99, exiting')
    def test_opcode6OnZeroJump(self):
        intcode = [6, 6, 3, 7, 4, 4, 0, 99]
        testComputer = IntcodeComputer(intcode)
        testComputer.run()
        self.assertEqual(len(testComputer.log), 2)
        self.assertEqual(testComputer.log[0], f'opcode 6 at position 0 processed')
        self.assertEqual(testComputer.log[1], f'opcode 99, exiting')

class Opcode6immediateMode(unittest.TestCase):
    def test_opcode6ImediateModeJump(self):
        intcode = [1106, 0, 7, 4, 0, 4, 0, 99]
        testComputer = IntcodeComputer(intcode)
        testComputer.run()
        self.assertEqual(len(testComputer.log), 2)
        self.assertEqual(testComputer.log[0], f'opcode 6 at position 0 processed')
        self.assertEqual(testComputer.log[1], f'opcode 99, exiting')
    def test_opcode6ImediateModeDontJump(self):
        intcode = [1106, 1, 7, 3, 0, 3, 0, 99]
        testComputer = IntcodeComputer(intcode)
        testComputer.inputs = [1, 5]
        testComputer.run()
        self.assertEqual(len(testComputer.log), 4)
        self.assertEqual(testComputer.log[0], f'opcode 6 at position 0 processed')
        self.assertEqual(testComputer.log[1], f'opcode 3 at position 3 processed')
        self.assertEqual(testComputer.log[2], f'opcode 3 at position 5 processed')
        self.assertEqual(testComputer.log[3], f'opcode 99, exiting')

class Opcode7immediateMode(unittest.TestCase):
    def test_opcode7LessThanStore1ImmediateMode(self):
        intcode = [1107, 2, 4, 1, 99]
        testComputer = IntcodeComputer(intcode)
        testComputer.run()
        self.assertEqual([1107, 1, 4, 1, 99],testComputer.intcode)
    def test_opcode7LessThanStore1ImmediateMode(self):
        intcode = [1107, 6, 3, 5, 99, 5]
        testComputer = IntcodeComputer(intcode)
        testComputer.run()
        self.assertEqual([1107, 6, 3, 5, 99, 0],testComputer.intcode)
    def test_opcode7logsMessage(self):
        intcode = [1107, 2, 4, 1, 99]
        testComputer = IntcodeComputer(intcode)
        testComputer.run()
        self.assertEqual('opcode 7 at position 0 processed', testComputer.log[0])

class Opcode8immediateMode(unittest.TestCase):
    def test_opcode8EqualStore1Mixed(self):
        intcode = [108, 5, 1, 5, 99, 5]
        testComputer = IntcodeComputer(intcode)
        testComputer.run()
        self.assertEqual([108, 5, 1, 5, 99, 1],testComputer.intcode)
    def test_opcode8EqualStore0Mixed(self):
        intcode = [108, 5, 0, 5, 99, 5]
        testComputer = IntcodeComputer(intcode)
        testComputer.run()
        self.assertEqual([108, 5, 0, 5, 99, 0],testComputer.intcode)
    def test_opcode8logsMessage(self):
        intcode = [108, 5, 1, 5, 99, 5]
        testComputer = IntcodeComputer(intcode)
        testComputer.run()
        self.assertEqual('opcode 8 at position 0 processed',testComputer.log[0])

class Opcode9positionMode(unittest.TestCase):
    def test_increaseRelativeBaseBy99(self):
        intcode = [9,2,99]
        testComputer = IntcodeComputer(intcode)
        testComputer.run()
        self.assertEqual(99,testComputer.relativeBase)

class Opcode9immediateMode(unittest.TestCase):
    def test_increaseRelativeBaseBy50(self):
        intcode = [109,50,99]
        testComputer = IntcodeComputer(intcode)
        testComputer.run()
        self.assertEqual(50,testComputer.relativeBase)
    def test_opcode9LogsMessage(self):
        intcode = [109, 50, 99]
        testComputer = IntcodeComputer(intcode)
        testComputer.run()
        self.assertEqual('opcode 9 at position 0 processed', testComputer.log[0])


class Opcode99(unittest.TestCase):
    def setUp(self):
        intcode = [99, 99, 85]
        self.testComputer = IntcodeComputer(intcode)
        self.referenceMessage = 'opcode 99, exiting'
    def tearDown(self):
        self.testComputer = None
    def test_opcode99stopsTheComputer(self):
        self.testComputer.run()
        self.assertEqual(1,len(self.testComputer.log))
    def test_opcode99logsTheMessage(self):
        self.testComputer.run()
        self.assertEqual(self.referenceMessage,self.testComputer.log[0])


class OpcodeUnknown(unittest.TestCase):
    def setUp(self):
        intcode = [11145,91,85]
        self.testComputer = IntcodeComputer(intcode)
        self.referenceMessage = 'Uknown opcode encountered, 45 at position 0, exiting'
    def tearDown(self):
        self.testComputer = None
    def test_takingStepUnknownOpcodePrintsMessage(self):
        with patch('builtins.print') as p:
            self.testComputer.takeStep()
        p.assert_called_with('unknown opcode 45 encountered at position 0')
    def test_takingStepUnknownOpcodeLogsMessage(self):
        with patch('builtins.print') as p:
            logMessage = self.testComputer.takeStep()
        self.assertEqual(self.referenceMessage,logMessage)
    def test_runningUnknownOpcodeStopsTheIntcodeComputer(self):
        with patch('builtins.print') as p:
            self.testComputer.run()
        self.assertEqual(1, len(self.testComputer.log))
    def test_runningUnkownOpcodeLogsTheMessage(self):
        with patch('builtins.print') as p:
            self.testComputer.run()
        self.assertEqual(self.referenceMessage, self.testComputer.log[0])

class TestsGeneralStuff(unittest.TestCase):
    def test_takingStepLowerBoundPassedMessage(self):
        intcode = []
        testComputer = IntcodeComputer(intcode)
        message = testComputer.takeStep(-125)
        self.assertEqual('position too low, -125, exiting', message)
    def test_takingStepUpperBoundPassedMessage(self):
        intcode = []
        testComputer = IntcodeComputer(intcode)
        message = testComputer.takeStep(25)
        self.assertEqual('position too high, expanding memory to 25', message)
    def test_takingStepUpperBoundPassedChangesIntcode(self):
        intcode = []
        testComputer = IntcodeComputer(intcode)
        message = testComputer.takeStep(25)
        self.assertEqual(25,len(testComputer.intcode))
        for i in range(0,25):
            with self.subTest(intcodeIndex= i):
                self.assertEqual(0,testComputer.intcode[i])
    def test_runningOpcodes_1positionMode_and_99MessageLog(self):
        intcode = [1, 1, 1, 1, 99]
        testComputer = IntcodeComputer(intcode)
        testComputer.run()
        self.assertEqual(2, len(testComputer.log))
        self.assertEqual('opcode 1 at position 0 processed',testComputer.log[0])
        self.assertEqual('opcode 99, exiting',testComputer.log[1])
    def test_runningOpcodes_1positionMode_and_99IntcodeChanges(self):
        intcode = [1, 1, 1, 1, 99]
        testComputer = IntcodeComputer(intcode)
        testComputer.run()
        self.assertEqual([1, 2, 1, 1, 99],testComputer.intcode)
    def test_runningOpcodes_1positionMode_and_2positionMode_and_99MessageLog(self):
        intcode = [1, 1, 1, 1, 2, 4, 4, 3, 99]
        testComputer = IntcodeComputer(intcode)
        testComputer.run()
        self.assertEqual(3, len(testComputer.log))
        self.assertEqual('opcode 1 at position 0 processed', testComputer.log[0])
        self.assertEqual('opcode 2 at position 4 processed', testComputer.log[1])
        self.assertEqual('opcode 99, exiting', testComputer.log[2])
    def test_runningOpcodes_1positionMode_and_2positionMode_and_99IntcodeChanges(self):
        intcode = [1, 1, 1, 1, 2, 4, 4, 3, 99]
        testComputer = IntcodeComputer(intcode)
        testComputer.run()
        self.assertEqual([1, 2, 1, 4, 2, 4, 4, 3, 99],testComputer.intcode)
    def test_parameterAis0_1_2(self):
        intcode = [80001, 99]
        testComputer = IntcodeComputer(intcode)
        with self.assertRaises(ValueError) as e:
            testComputer.run()
        self.assertEqual(f'Parameter A should be 0, 1 or 2. Not 8', str(e.exception))
    def test_parameterBis0_1_2(self):
        intcode = [8001, 99]
        testComputer = IntcodeComputer(intcode)
        with self.assertRaises(ValueError) as e:
            testComputer.run()
        self.assertEqual(f'Parameter B should be 0, 1 or 2. Not 8', str(e.exception))
    def test_parameterCis0_1_2(self):
        intcode = [801, 99]
        testComputer = IntcodeComputer(intcode)
        with self.assertRaises(ValueError) as e:
            testComputer.run()
        self.assertEqual(f'Parameter C should be 0, 1 or 2. Not 8', str(e.exception))
    def test_IntcodeComputerHasARelativeBase(self):
        intcode = [99]
        testComputer = IntcodeComputer(intcode)
        self.assertTrue(hasattr(testComputer, 'relativeBase'),f'IntcodeComputer should have a relativeBase')
    def test_IntcodeComputerRelativeBaseDefaultZero(self):
        intcode = [99]
        testComputer = IntcodeComputer(intcode)
        self.assertEqual(0,testComputer.relativeBase,f'Default value for the relative base should be 0')
    def test_running109_10_22202_min9_min9_0_99IntcodeChanges(self):
        intcode = [109,10,22202,-9,-9,0,99]
        testComputer = IntcodeComputer(intcode)
        testComputer.run()
        self.assertEqual([109, 10, 22202, -9, -9, 0, 99, 0, 0, 0, 100],testComputer.intcode)



class testsAmplifier(unittest.TestCase):
    def test_SimpleAmpWithPhaseSetting(self):
        intcode = [3,1,99]
        phaseSetting = 3
        amp = amplifier(intcode,phaseSetting)
        self.assertEqual([3,3,99],amp.computer.intcode)
    def test_SimpleAmpOutput(self):
        intcode = [4,0,99]
        phaseSetting = 2
        amp = amplifier(intcode,phaseSetting)
        self.assertEqual(4,amp.takeOutput())

class testsAmplifiersInSeries(unittest.TestCase):
    def test_FirstHighestOutputExample(self):
        phaseSettings = '43210'
        intcode = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
        ampBank = amplifiersInSeries(intcode,phaseSettings)
        self.assertEqual(43210,ampBank.giveFinalOutput())
    def test_SecondHighestExample(self):
        phaseSettings = '01234'
        intcode = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
        ampBank = amplifiersInSeries(intcode,phaseSettings)
        self.assertEqual(54321,ampBank.giveFinalOutput())

class testsAmplifiersInSeries(unittest.TestCase):
    def test_FirstHighestOutputExample(self):
        phaseSettings = '43210'
        path = 'ExampleData\Day7Example1'
        ampBank = constructAmplifiersInSeriesFromFile(path,phaseSettings)
        self.assertEqual(43210, ampBank.giveFinalOutput())
    def test_SecondHighestOutputExample(self):
        phaseSettings = '01234'
        path = 'ExampleData\Day7Example2'
        ampBank = constructAmplifiersInSeriesFromFile(path,phaseSettings)
        self.assertEqual(54321, ampBank.giveFinalOutput())
    def test_ThirdHighestOutputExample(self):
        phaseSettings = '10432'
        path = 'ExampleData\Day7Example3'
        ampBank = constructAmplifiersInSeriesFromFile(path,phaseSettings)
        self.assertEqual(65210, ampBank.giveFinalOutput())

class testsFindMaxThrusterSignalFromPath(unittest.TestCase):
    def test_FirstExample(self):
        path = 'ExampleData\Day7Example1'
        testBank = FindMaxThrusterSignalFromPath(path)
        self.assertEqual(43210,testBank.highestThrusterSignal)
    def test_SecondExample(self):
        path = 'ExampleData\Day7Example2'
        testBank = FindMaxThrusterSignalFromPath(path)
        self.assertEqual(54321,testBank.highestThrusterSignal)
    def test_ThirdExample(self):
        path = 'ExampleData\Day7Example3'
        testBank = FindMaxThrusterSignalFromPath(path)
        self.assertEqual(65210,testBank.highestThrusterSignal)


class testsAmplifiersInSeriesWithFeedbackLoop(unittest.TestCase):
    def test_FourthHighestExample(self):
        testIntcode = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
        phaseSettings = '98765'
        ampBank = amplifiersInSeriesWithFeedbackLoop(testIntcode,phaseSettings)
        self.assertEqual(139629729,ampBank.giveFinalOutput())

class testsAmplifiersInSeriesWithFeedbackLoopFromFile(unittest.TestCase):
    def test_FourthHighestOutputExample(self):
        phaseSettings = '98765'
        path = 'ExampleData\Day7part2Example1'
        ampBank = constructAmplifiersInSeriesWithFeedbackLoopFromFile(path,phaseSettings)
        self.assertEqual(139629729, ampBank.giveFinalOutput())
    def test_FifthHighestOutputExample(self):
        phaseSettings = '97856'
        path = 'ExampleData\Day7part2Example2'
        ampBank = constructAmplifiersInSeriesWithFeedbackLoopFromFile(path,phaseSettings)
        self.assertEqual(18216, ampBank.giveFinalOutput())

class testsFindMaxThrusterFeedbackLoopSignalFromPath(unittest.TestCase):
    def test_FourthExample(self):
        path = 'ExampleData\Day7part2Example1'
        testBank = FindMaxThrusterFeedbackLoopSignalFromPath(path)
        self.assertEqual(139629729,testBank.highestThrusterSignal)
    def test_FifthExample(self):
        path = 'ExampleData\Day7part2Example2'
        testBank = FindMaxThrusterFeedbackLoopSignalFromPath(path)
        self.assertEqual(18216,testBank.highestThrusterSignal)



class Examples(unittest.TestCase):
    def test_day2Example1FromList(self):
        intcode = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        exampleComputer = IntcodeComputer(intcode)
        exampleComputer.run()
        self.assertEqual(70,exampleComputer.intcode[3],f'day 2 example 1 from list should have 70 at pos 3')
        self.assertEqual(3500,exampleComputer.intcode[0],f'day 2 example 1 from list should have 3500 at pos 0')
    def test_day2Example1FromFile(self):
        path = 'ExampleData\Day2Example1'
        exampleComputer = constructComputerFromFile(path)
        exampleComputer.run()
        self.assertEqual(70, exampleComputer.intcode[3], f'day 2 example 1 from file should have 70 at pos 3')
        self.assertEqual(3500, exampleComputer.intcode[0], f'day 2 example 1 from file should have 3500 at pos 0')
    def test_day5Example1FromList(self):
        intcode = [3, 0, 4, 0, 99]
        inputValue = 567
        exampleComputer = IntcodeComputer(intcode)
        with patch('builtins.print') as p:
            with patch('builtins.input', lambda *args: inputValue):
                exampleComputer.run()
        self.assertEqual(inputValue,exampleComputer.outputs[0],f'day 5 example 1 from list should take an input and output it')
    def test_day5Example1FromFile(self):
        path = 'ExampleData\Day5Example1'
        inputValue = 321
        exampleComputer = constructComputerFromFile(path)
        with patch('builtins.print') as p:
            with patch('builtins.input', lambda *args: inputValue):
                exampleComputer.run()
        self.assertEqual(inputValue, exampleComputer.outputs[0],f'day 5 example 1 from list should take an input and output it')
    def test_Day5Part2Example1Input8Output1FromFile(self):
        path = 'ExampleData\Day5part2Example1'
        exampleComputer = constructComputerFromFile(path)
        userInput8 = 8
        with patch('builtins.print') as p:
            with patch('builtins.input', lambda *args: userInput8):
                exampleComputer.run()
        self.assertEqual(1, exampleComputer.outputs[0])
    def test_Day5Part2Example1Input5Output0FromFile(self):
        path = 'ExampleData\Day5part2Example1'
        exampleComputer = constructComputerFromFile(path)
        userInput5 = 5
        with patch('builtins.print') as p:
            with patch('builtins.input', lambda *args: userInput5):
                exampleComputer.run()
        self.assertEqual(0, exampleComputer.outputs[0])
    def test_Day5Part2Example2Input8Output0FromList(self):
        intcode = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
        exampleComputer = IntcodeComputer(intcode)
        userInputEqual = 8
        with patch('builtins.print') as p:
            with patch('builtins.input', lambda *args: userInputEqual):
                exampleComputer.run()
        self.assertEqual(0, exampleComputer.outputs[0])
    def test_Day5Part2Example2Input5Output0FromList(self):
        intcode = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
        exampleComputer = IntcodeComputer(intcode)
        userInputLess = 5
        with patch('builtins.print') as p:
            with patch('builtins.input', lambda *args: userInputLess):
                exampleComputer.run()
            self.assertEqual(1, exampleComputer.outputs[0])
    def test_Day5Part2Example3Input8Output1FromList(self):
        intcode = [3,3,1108,-1,8,3,4,3,99]
        exampleComputer = IntcodeComputer(intcode)
        userInputEqual = 8
        with patch('builtins.print') as p:
            with patch('builtins.input', lambda *args: userInputEqual):
                exampleComputer.run()
        self.assertEqual(1, exampleComputer.outputs[0])
    def test_Day5Part2Example3Input5Output0FromList(self):
        intcode = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
        exampleComputer = IntcodeComputer(intcode)
        userInputLess = 5
        with patch('builtins.print') as p:
            with patch('builtins.input', lambda *args: userInputLess):
                exampleComputer.run()
        self.assertEqual(0, exampleComputer.outputs[0])
    def test_Day5Part2Example4Input8Output0FromList(self):
        intcode = [3,3,1107,-1,8,3,4,3,99]
        exampleComputer = IntcodeComputer(intcode)
        userInputEqual = 8
        with patch('builtins.print') as p:
            with patch('builtins.input', lambda *args: userInputEqual):
                exampleComputer.run()
        self.assertEqual(0, exampleComputer.outputs[0])
    def test_Day5Part2Example4Input8Output1FromList(self):
        intcode = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
        exampleComputer = IntcodeComputer(intcode)
        userInputLess = 5
        with patch('builtins.print') as p:
            with patch('builtins.input', lambda *args: userInputLess):
                exampleComputer.run()
        self.assertEqual(1, exampleComputer.outputs[0])
    def test_Day5Part2Example5Input0Output0FromList(self):
        intcode = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
        exampleComputer = IntcodeComputer(intcode)
        userInputZero = 0
        with patch('builtins.print') as p:
            with patch('builtins.input', lambda *args: userInputZero):
                exampleComputer.run()
        self.assertEqual(0, exampleComputer.outputs[0])
    def test_Day5Part2Example5Input1Output1FromList(self):
        intcode = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
        exampleComputer = IntcodeComputer(intcode)
        userInputNonZero = 1
        with patch('builtins.print') as p:
            with patch('builtins.input', lambda *args: userInputNonZero):
                exampleComputer.run()
        self.assertEqual(1, exampleComputer.outputs[0])
    def test_Day5Part2Example6Input0Output0FromList(self):
        intcode = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
        exampleComputer = IntcodeComputer(intcode)
        userInputZero = 0
        with patch('builtins.print') as p:
            with patch('builtins.input', lambda *args: userInputZero):
                exampleComputer.run()
        self.assertEqual(0, exampleComputer.outputs[0])
    def test_Day5Part2Example6Input1Output1FromList(self):
        intcode = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
        exampleComputer = IntcodeComputer(intcode)
        userInputNonZero = 1
        with patch('builtins.print') as p:
            with patch('builtins.input', lambda *args: userInputNonZero):
                exampleComputer.run()
        self.assertEqual(1, exampleComputer.outputs[0])
    def test_Day5Part2Example7Input8Output1000FromFile(self):
        path = 'ExampleData\Day5part2Example7'
        exampleComputer = constructComputerFromFile(path)
        userInputEqual = 8
        with patch('builtins.print') as p:
            with patch('builtins.input', lambda *args: userInputEqual):
                exampleComputer.run()
        self.assertEqual(1000, exampleComputer.outputs[0])
    def test_Day5Part2Example7Input5Output999FromFile(self):
        path = 'ExampleData\Day5part2Example7'
        exampleComputer = constructComputerFromFile(path)
        userInputLess = 5
        with patch('builtins.print') as p:
            with patch('builtins.input', lambda *args: userInputLess):
                exampleComputer.run()
        self.assertEqual(999, exampleComputer.outputs[0])
    def test_Day5Part2Example7Input11Output1001FromFile(self):
        path = 'ExampleData\Day5part2Example7'
        exampleComputer = constructComputerFromFile(path)
        userInputGreater = 11
        with patch('builtins.print') as p:
            with patch('builtins.input', lambda *args: userInputGreater):
                exampleComputer.run()
        self.assertEqual(1001, exampleComputer.outputs[0])
    def test_Day9Example1NoInputsOutputsCopyFromFile(self):
        path = 'ExampleData\Day9Example1'
        exampleComputer = constructComputerFromFile(path)
        referenceIntcode = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
        with patch('builtins.print') as p:
            exampleComputer.run()
        self.assertEqual(referenceIntcode,exampleComputer.outputs)
    def test_Day9Example2Outputs16digitNumber(self):
        intcode = [1102,34915192,34915192,7,4,7,99,0]
        exampleComputer = IntcodeComputer(intcode)
        with patch('builtins.print') as p:
            exampleComputer.run()
        p.assert_called_with(1219070632396864)
        self.assertEqual(16,len(str(exampleComputer.outputs[0])))
    def test_Day9Example3OutputsLargeMiddleNumber(self):
        intcode = [104,1125899906842624,99]
        exampleComputer = IntcodeComputer(intcode)
        with patch('builtins.print') as p:
            exampleComputer.run()
        p.assert_called_with(1125899906842624)
        self.assertEqual(1125899906842624,exampleComputer.outputs[0])

if __name__ == '__main__':
    unittest.main()
