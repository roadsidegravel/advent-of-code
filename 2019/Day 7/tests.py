import unittest
from unittest.mock import patch
# unittest most used asserts:
# self.assertEqual(a,b)
# self.assertFalse(bool)
# self.assertTrue(bool)
# self.assertRaises(error)
# https://docs.python.org/3/library/unittest.html
# def setUp(self):
# def tearDown(self):
# def suite for custom test suite building (which tests to run)

# https://queirozf.com/entries/python-unittest-examples-mocking-and-patching

import Intcode
class testIntcode(unittest.TestCase):
    # implement unknown opcode
    # something went wrong
    def test_opcodeUnknown12345(self):
        intcode = [11145]
        # with self.assertRaises(NotImplementedError):
        #   Intcode.computer(intcode).takeStep()
        message = Intcode.computer(intcode).takeStep()
        self.assertEqual('Uknown opcode encountered, 45 at position 0, exiting', message)

    # implement opcode 99
    # read a 99: finished, halt program immediately
    def test_opcode99(self):
        intcode = [99]
        message = Intcode.computer(intcode).takeStep()
        self.assertEqual('opcode 99, exiting', message, f'99 should exit the program')

    # implement catching of going out of lower bound
    def test_lowerBoundPassed(self):
        intcode = []
        message = Intcode.computer(intcode).takeStep(-125)
        self.assertEqual('position too low, -125, exiting', message)

    def test_upperBoundPassed(self):
        intcode = []
        message = Intcode.computer(intcode).takeStep(25)
        self.assertEqual('position too high, 25, exiting', message)

    # implement opcode 1
    # read a 1: add two positions together and store in the third position
    def test_opcode1with1111(self):
        intcode = [1, 1, 1, 1]
        computer = Intcode.computer(intcode)
        message = computer.takeStep()
        self.assertEqual('opcode 1 at position 0 processed', message)
        self.assertEqual(1, computer.intcode[0])
        self.assertEqual(2, computer.intcode[1])
        self.assertEqual(1, computer.intcode[2])
        self.assertEqual(1, computer.intcode[3])

    def test_opcode1with1003(self):
        intcode = [1, 0, 0, 3]
        computer = Intcode.computer(intcode)
        message = computer.takeStep()
        self.assertEqual('opcode 1 at position 0 processed', message)
        self.assertEqual(1, computer.intcode[0])
        self.assertEqual(0, computer.intcode[1])
        self.assertEqual(0, computer.intcode[2])
        self.assertEqual(2, computer.intcode[3])

    # implement opcode 2
    # read a 2: multiply two positions and store in the third position
    def test_opcode2with2111(self):
        intcode = [2, 1, 1, 1]
        computer = Intcode.computer(intcode)
        message = computer.takeStep()
        self.assertEqual('opcode 2 at position 0 processed', message)
        self.assertEqual(2, computer.intcode[0])
        self.assertEqual(1, computer.intcode[1])
        self.assertEqual(1, computer.intcode[2])
        self.assertEqual(1, computer.intcode[3])

    def test_opcode2with2003(self):
        intcode = [2, 0, 0, 3]
        computer = Intcode.computer(intcode)
        message = computer.takeStep()
        self.assertEqual('opcode 2 at position 0 processed', message)
        self.assertEqual(2, computer.intcode[0])
        self.assertEqual(0, computer.intcode[1])
        self.assertEqual(0, computer.intcode[2])
        self.assertEqual(4, computer.intcode[3])

    def test_runningIntcodeComputer1and99(self):
        intcode = [1, 1, 1, 1, 99]
        computer = Intcode.computer(intcode)
        message0 = computer.takeStep()
        message1 = computer.takeStep()
        self.assertEqual('opcode 1 at position 0 processed', message0)
        self.assertEqual('opcode 99, exiting', message1)
        self.assertEqual(1, computer.intcode[0])
        self.assertEqual(2, computer.intcode[1])
        self.assertEqual(1, computer.intcode[2])
        self.assertEqual(1, computer.intcode[3])
        self.assertEqual(99, computer.intcode[4])

    def test_runningIntcodeComputer1and2and99(self):
        intcode = [1, 1, 1, 1, 2, 4, 4, 3, 99]
        computer = Intcode.computer(intcode)
        message0 = computer.takeStep()
        message1 = computer.takeStep()
        message2 = computer.takeStep()
        self.assertEqual('opcode 1 at position 0 processed', message0)
        self.assertEqual('opcode 2 at position 4 processed', message1)
        self.assertEqual('opcode 99, exiting', message2)
        self.assertEqual(1, computer.intcode[0])
        self.assertEqual(2, computer.intcode[1])
        self.assertEqual(1, computer.intcode[2])
        self.assertEqual(4, computer.intcode[3])
        self.assertEqual(2, computer.intcode[4])
        self.assertEqual(4, computer.intcode[5])
        self.assertEqual(4, computer.intcode[6])
        self.assertEqual(3, computer.intcode[7])
        self.assertEqual(99, computer.intcode[8])

    def test_runningIntcodeComputerExampleDay2(self):
        intcode = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        computer = Intcode.computer(intcode)
        computer.running = True
        while computer.running:
            computer.takeStep()
        self.assertEqual(70, computer.intcode[3])
        self.assertEqual(3500, computer.intcode[0])

    def test_runCommandExampleDay2(self):
        intcode = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        computer = Intcode.computer(intcode)
        computer.run()
        self.assertEqual(70, computer.intcode[3])
        self.assertEqual(3500, computer.intcode[0])

    # Day 5
    # left to right
    # 0 or 1: postion or immediate mode parameter 3
    # 0 or 1: position or immediate mode parameter 2
    # 0 or 1: position or immediate mode parameter 1
    # 00 to 99: opcodes, 01, 02, 03,... 99
    # 0 is default added
    # add command 3
    def test_opcode3(self):
        # https://dev.to/vergeev/how-to-test-input-processing-in-python-3
        # https://stackoverflow.com/questions/21046717/python-mocking-raw-input-in-unittests
        # https://stackoverflow.com/questions/18161330/using-unittest-mock-to-patch-input-in-python-3
        intcode = [3, 1, 99]
        userInput = 5
        with patch('builtins.input', lambda *args: userInput):
            computer = Intcode.computer(intcode)
            computer.run()
        self.assertEqual(3, computer.intcode[0])
        self.assertEqual(userInput, computer.intcode[1])
        self.assertEqual(99, computer.intcode[2])

    def test_copde3inputs5and3(self):
        intcode = [3, 0, 3, 1, 99]
        inputs = [5, 3]
        computer = Intcode.computer(intcode)
        computer.inputs = inputs
        computer.run()
        self.assertEqual(5, computer.intcode[0])
        self.assertEqual(3, computer.intcode[1])
        self.assertEqual(3, computer.intcode[2])
        self.assertEqual(1, computer.intcode[3])
        self.assertEqual(99, computer.intcode[4])

    # add command 4
    def test_code4output(self):
        intcode = [4, 0, 99]
        with patch('builtins.print') as p:
            computer = Intcode.computer(intcode)
            computer.run()
            p.assert_called_with(4)
            self.assertEqual(4, computer.outputs[0])

    def test_example304099(self):
        intcode = [3, 0, 4, 0, 99]
        computer = Intcode.computer(intcode)
        inputValue = 123
        computer.inputs = [inputValue]
        computer.run()
        self.assertEqual(inputValue, computer.outputs[0])

    # add mode 1
    # refactored takeStep
    # refactored opcode1
    def test_immediateModeOpcode1(self):
        intcode = [1101, 5, 7, 3, 99]
        computer = Intcode.computer(intcode)
        computer.run()
        self.assertEqual([1101, 5, 7, 12, 99], computer.intcode)

    def test_immediateModeOpcode1Mixed(self):
        intcode = [1001, 0, 120, 3, 99]
        computer = Intcode.computer(intcode)
        computer.run()
        self.assertEqual([1001, 0, 120, 1121, 99], computer.intcode)

    def test_immediateModeOpcode1ValueErrorParameter3(self):
        intcode = [10001, 0, 0, 99]
        # https://stackoverflow.com/questions/129507/how-do-you-test-that-a-python-function-throws-an-exception
        with self.assertRaises(ValueError) as e:
            computer = Intcode.computer(intcode)
            computer.run()
        self.assertEqual('Parameters that an instruction writes to will never be in immediate mode.', str(e.exception))

    # refactored opcode2
    def test_immediateModeOpcode2ValueErrorParamater3(self):
        intcode = [10002, 0, 0, 99]
        # https://stackoverflow.com/questions/129507/how-do-you-test-that-a-python-function-throws-an-exception
        with self.assertRaises(ValueError) as e:
            computer = Intcode.computer(intcode)
            computer.run()
        self.assertEqual('Parameters that an instruction writes to will never be in immediate mode.', str(e.exception))

    def test_immediateModeOpcode2(self):
        intcode = [1102, 5, 7, 3, 99]
        computer = Intcode.computer(intcode)
        computer.run()
        self.assertEqual([1102, 5, 7, 35, 99], computer.intcode)

    def test_immediateModeOpcode2Mixed(self):
        intcode = [1002, 0, 2, 3, 99]
        computer = Intcode.computer(intcode)
        computer.run()
        self.assertEqual([1002, 0, 2, 2004, 99], computer.intcode)

    # bug found
    def test_ensureModesAre1or0(self):
        with self.assertRaises(ValueError) as e:
            intcode = [20001, 99]
            computer = Intcode.computer(intcode)
            computer.run()
        self.assertEqual(f'Parameter A should be 1 or 0, not 2', str(e.exception))
        with self.assertRaises(ValueError) as e:
            intcode = [3001, 99]
            computer = Intcode.computer(intcode)
            computer.run()
        self.assertEqual(f'Parameter B should be 1 or 0, not 3', str(e.exception))
        with self.assertRaises(ValueError) as e:
            intcode = [401, 99]
            computer = Intcode.computer(intcode)
            computer.run()
        self.assertEqual(f'Parameter C should be 1 or 0, not 4', str(e.exception))

    # imediate mode 3 & 4
    def test_immediateModeOpcode3ValueErrorParameterA(self):
        intcode = [103, 1, 99]
        # https://stackoverflow.com/questions/129507/how-do-you-test-that-a-python-function-throws-an-exception
        with self.assertRaises(ValueError) as e:
            userInput = 4
            with patch('builtins.input', lambda *args: userInput):
                computer = Intcode.computer(intcode)
                computer.run()
        self.assertEqual('Parameters that an instruction writes to will never be in immediate mode.', str(e.exception))

    def test_immediateModeOpcode4ParameterA(self):
        intcode = [104, 5, 99, 3, 4, 5]
        with patch('builtins.print') as p:
            computer = Intcode.computer(intcode)
            computer.run()
            p.assert_called_with(5)
            self.assertEqual(5, computer.outputs[0])

    # refactoring/code cleaning/restructuring
    # @dinges, setter getter enzo (voorlopig nog niet gebruikt)
    # kunt functies nesten, en classes
    # opcode 5
    def test_opcode5OnZeroDoNothing(self):
        intcode = [5, 6, 7, 1, 4, 4, 0, 99]
        computer = Intcode.computer(intcode)
        computer.run()
        self.assertEqual(len(computer.log), 3)
        self.assertEqual(computer.log[0], f'opcode 5 at position 0 processed')
        self.assertEqual(computer.log[1], f'opcode 1 at position 3 processed')
        self.assertEqual(computer.log[2], f'opcode 99, exiting')

    def test_opcode5OnNotZeroJump(self):
        intcode = [5, 7, 1, 1, 4, 4, 6, 99]
        computer = Intcode.computer(intcode)
        computer.run()
        self.assertEqual(len(computer.log), 2)
        self.assertEqual(computer.log[0], f'opcode 5 at position 0 processed')
        self.assertEqual(computer.log[1], f'opcode 99, exiting')

    # imediate mode opcode 5
    def test_opcode5ImediateModeJump(self):
        intcode = [1105, 1, 7, 4, 0, 4, 0, 99]
        computer = Intcode.computer(intcode)
        computer.run()
        self.assertEqual(len(computer.log), 2)
        self.assertEqual(computer.log[0], f'opcode 5 at position 0 processed')
        self.assertEqual(computer.log[1], f'opcode 99, exiting')

    def test_opcode5ImediateModeDontJump(self):
        intcode = [1105, 0, 7, 3, 0, 3, 0, 99]
        computer = Intcode.computer(intcode)
        computer.inputs = [1, 5]
        computer.run()
        self.assertEqual(len(computer.log), 4)
        self.assertEqual(computer.log[0], f'opcode 5 at position 0 processed')
        self.assertEqual(computer.log[1], f'opcode 3 at position 3 processed')
        self.assertEqual(computer.log[2], f'opcode 3 at position 5 processed')
        self.assertEqual(computer.log[3], f'opcode 99, exiting')

    # opcode 6
    def test_opcode6OnNotZeroDoNothing(self):
        intcode = [6, 6, 7, 1, 4, 4, 1, 99]
        computer = Intcode.computer(intcode)
        computer.run()
        self.assertEqual(len(computer.log), 3)
        self.assertEqual(computer.log[0], f'opcode 6 at position 0 processed')
        self.assertEqual(computer.log[1], f'opcode 1 at position 3 processed')
        self.assertEqual(computer.log[2], f'opcode 99, exiting')

    def test_opcode6OnZeroJump(self):
        intcode = [6, 6, 3, 7, 4, 4, 0, 99]
        computer = Intcode.computer(intcode)
        computer.run()
        self.assertEqual(len(computer.log), 2)
        self.assertEqual(computer.log[0], f'opcode 6 at position 0 processed')
        self.assertEqual(computer.log[1], f'opcode 99, exiting')

    # imediate mode opcode 6
    def test_opcode6ImediateModeJump(self):
        intcode = [1106, 0, 7, 4, 0, 4, 0, 99]
        computer = Intcode.computer(intcode)
        computer.run()
        self.assertEqual(len(computer.log), 2)
        self.assertEqual(computer.log[0], f'opcode 6 at position 0 processed')
        self.assertEqual(computer.log[1], f'opcode 99, exiting')

    def test_opcode6ImediateModeDontJump(self):
        intcode = [1106, 1, 7, 3, 0, 3, 0, 99]
        computer = Intcode.computer(intcode)
        computer.inputs = [1, 5]
        computer.run()
        self.assertEqual(len(computer.log), 4)
        self.assertEqual(computer.log[0], f'opcode 6 at position 0 processed')
        self.assertEqual(computer.log[1], f'opcode 3 at position 3 processed')
        self.assertEqual(computer.log[2], f'opcode 3 at position 5 processed')
        self.assertEqual(computer.log[3], f'opcode 99, exiting')

    # opcode 7
    def test_opcode7LessThanStore1ImmediateMode(self):
        intcode = [1107, 2, 4, 1, 99]
        computer = Intcode.computer(intcode)
        computer.run()
        self.assertEqual([1107, 1, 4, 1, 99], computer.intcode)

    def test_opcode7LessThanStore1ImmediateMode(self):
        intcode = [1107, 6, 3, 5, 99, 5]
        computer = Intcode.computer(intcode)
        computer.run()
        self.assertEqual([1107, 6, 3, 5, 99, 0], computer.intcode)

    # refactoring, modes
    # opcode 8
    def test_opcode8EqualStore1Mixed(self):
        intcode = [108, 5, 1, 5, 99, 5]
        computer = Intcode.computer(intcode)
        computer.run()
        self.assertEqual([108, 5, 1, 5, 99, 1], computer.intcode)

    def test_opcode8EqualStore0Mixed(self):
        intcode = [108, 5, 0, 5, 99, 5]
        computer = Intcode.computer(intcode)
        computer.run()
        self.assertEqual([108, 5, 0, 5, 99, 0], computer.intcode)

    # refactoring def retrieve first and second
    # refactoring def write to third
    # refactoring more def like that
    # day 7
    def test_opcode3AutomaticModePausesIntcomputerTillInputIsgiven(self):
        intcode = [3,1,99]
        automaticIntcomputer = Intcode.computer(intcode,True)
        automaticIntcomputer.run()
        self.assertFalse(automaticIntcomputer.running)
        automaticIntcomputer.automaticModeTakeInputAndUnpauze(5)
        self.assertEqual([3,5,99],automaticIntcomputer.intcode)
        self.assertEqual(3,len(automaticIntcomputer.log))
        self.assertEqual('pausing for input at position 0', automaticIntcomputer.log[0])
        self.assertEqual('opcode 3 at position 0 processed', automaticIntcomputer.log[1])
        self.assertEqual('opcode 99, exiting', automaticIntcomputer.log[2])

from Intcode import amplifier
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

from Intcode import amplifiersInSeries
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

#load from file
from Intcode import constructAmplifiersInSeriesFromFile
class testsAmplifiersInSeries(unittest.TestCase):
    def test_FirstHighestOutputExample(self):
        phaseSettings = '43210'
        path = 'ExampleData\Example1'
        ampBank = constructAmplifiersInSeriesFromFile(path,phaseSettings)
        self.assertEqual(43210, ampBank.giveFinalOutput())
    def test_SecondHighestOutputExample(self):
        phaseSettings = '01234'
        path = 'ExampleData\Example2'
        ampBank = constructAmplifiersInSeriesFromFile(path,phaseSettings)
        self.assertEqual(54321, ampBank.giveFinalOutput())
    def test_ThirdHighestOutputExample(self):
        phaseSettings = '10432'
        path = 'ExampleData\Example3'
        ampBank = constructAmplifiersInSeriesFromFile(path,phaseSettings)
        self.assertEqual(65210, ampBank.giveFinalOutput())

from Intcode import FindMaxThrusterSignalFromPath
class testsFindMaxThrusterSignalFromPath(unittest.TestCase):
    def test_FirstExample(self):
        path = 'ExampleData\Example1'
        testBank = FindMaxThrusterSignalFromPath(path)
        self.assertEqual(43210,testBank.highestThrusterSignal)
    def test_SecondExample(self):
        path = 'ExampleData\Example2'
        testBank = FindMaxThrusterSignalFromPath(path)
        self.assertEqual(54321,testBank.highestThrusterSignal)
    def test_ThirdExample(self):
        path = 'ExampleData\Example3'
        testBank = FindMaxThrusterSignalFromPath(path)
        self.assertEqual(65210,testBank.highestThrusterSignal)

from Intcode import amplifiersInSeriesWithFeedbackLoop
class testsAmplifiersInSeriesWithFeedbackLoop(unittest.TestCase):
    def test_FourthHighestExample(self):
        testIntcode = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
        phaseSettings = '98765'
        ampBank = amplifiersInSeriesWithFeedbackLoop(testIntcode,phaseSettings)
        self.assertEqual(139629729,ampBank.giveFinalOutput())

from Intcode import constructAmplifiersInSeriesWithFeedbackLoopFromFile
class testsAmplifiersInSeriesWithFeedbackLoopFromFile(unittest.TestCase):
    def test_FourthHighestOutputExample(self):
        phaseSettings = '98765'
        path = 'ExampleData\Example4'
        ampBank = constructAmplifiersInSeriesWithFeedbackLoopFromFile(path,phaseSettings)
        self.assertEqual(139629729, ampBank.giveFinalOutput())
    def test_FifthHighestOutputExample(self):
        phaseSettings = '97856'
        path = 'ExampleData\Example5'
        ampBank = constructAmplifiersInSeriesWithFeedbackLoopFromFile(path,phaseSettings)
        self.assertEqual(18216, ampBank.giveFinalOutput())

from Intcode import FindMaxThrusterFeedbackLoopSignalFromPath
class testsFindMaxThrusterFeedbackLoopSignalFromPath(unittest.TestCase):
    def test_FourthExample(self):
        path = 'ExampleData\Example4'
        testBank = FindMaxThrusterFeedbackLoopSignalFromPath(path)
        self.assertEqual(139629729,testBank.highestThrusterSignal)
    def test_FifthExample(self):
        path = 'ExampleData\Example5'
        testBank = FindMaxThrusterFeedbackLoopSignalFromPath(path)
        self.assertEqual(18216,testBank.highestThrusterSignal)




if __name__ == '__main__':
    unittest.main()
