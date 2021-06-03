import unittest
# unittest most used asserts:
# self.assertEqual(a,b)
# self.assertFalse(bool)
# self.assertTrue(bool)
# self.assertRaises(error)
# https://docs.python.org/3/library/unittest.html
# def setUp(self):
# def tearDown(self):
# def suite for custom test suite building (which tests to run)

import Intcode


class testIntcode(unittest.TestCase):
    # implement unknown opcode
    # something went wrong
    def test_opcodeUnknown12345(self):
        intcode = [12345]
        #with self.assertRaises(NotImplementedError):
        #   Intcode.computer(intcode).takeStep()
        message = Intcode.computer(intcode).takeStep()
        self.assertEqual('Uknown opcode encountered, 12345 at position 0, exiting', message)
    # implement opcode 99
    # read a 99: finished, halt program immediately
    def test_opcode99(self):
        intcode = [99]
        message = Intcode.computer(intcode).takeStep()
        self.assertEqual('opcode 99, exiting', message, f'99 should exit the program')
    #implement catching of going out of lower bound
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
        self.assertEqual('opcode 1 at position 0 processed',message)
        self.assertEqual(1,computer.intcode[0])
        self.assertEqual(2,computer.intcode[1])
        self.assertEqual(1,computer.intcode[2])
        self.assertEqual(1,computer.intcode[3])
    def test_opcode1with1003(self):
        intcode = [1, 0, 0, 3]
        computer = Intcode.computer(intcode)
        message = computer.takeStep()
        self.assertEqual('opcode 1 at position 0 processed',message)
        self.assertEqual(1,computer.intcode[0])
        self.assertEqual(0,computer.intcode[1])
        self.assertEqual(0,computer.intcode[2])
        self.assertEqual(2,computer.intcode[3])
    #implement opcode 2
    #read a 2: multiply two positions and store in the third position
    def test_opcode2with2111(self):
        intcode = [2, 1, 1, 1]
        computer = Intcode.computer(intcode)
        message = computer.takeStep()
        self.assertEqual('opcode 2 at position 0 processed',message)
        self.assertEqual(2,computer.intcode[0])
        self.assertEqual(1,computer.intcode[1])
        self.assertEqual(1,computer.intcode[2])
        self.assertEqual(1,computer.intcode[3])
    def test_opcode2with2003(self):
        intcode = [2, 0, 0, 3]
        computer = Intcode.computer(intcode)
        message = computer.takeStep()
        self.assertEqual('opcode 2 at position 0 processed',message)
        self.assertEqual(2,computer.intcode[0])
        self.assertEqual(0,computer.intcode[1])
        self.assertEqual(0,computer.intcode[2])
        self.assertEqual(4,computer.intcode[3])
    def test_runningIntcodeComputer1and99(self):
        intcode = [1, 1, 1, 1, 99]
        computer = Intcode.computer(intcode)
        message0 = computer.takeStep()
        message1 = computer.takeStep()
        self.assertEqual('opcode 1 at position 0 processed',message0)
        self.assertEqual('opcode 99, exiting',message1)
        self.assertEqual(1,computer.intcode[0])
        self.assertEqual(2,computer.intcode[1])
        self.assertEqual(1,computer.intcode[2])
        self.assertEqual(1,computer.intcode[3])
        self.assertEqual(99,computer.intcode[4])
    def test_runningIntcodeComputer1and2and99(self):
        intcode = [1, 1, 1, 1, 2, 4, 4, 3, 99]
        computer = Intcode.computer(intcode)
        message0 = computer.takeStep()
        message1 = computer.takeStep()
        message2 = computer.takeStep()
        self.assertEqual('opcode 1 at position 0 processed',message0)
        self.assertEqual('opcode 2 at position 4 processed',message1)
        self.assertEqual('opcode 99, exiting',message2)
        self.assertEqual(1,computer.intcode[0])
        self.assertEqual(2,computer.intcode[1])
        self.assertEqual(1,computer.intcode[2])
        self.assertEqual(4,computer.intcode[3])
        self.assertEqual(2,computer.intcode[4])
        self.assertEqual(4,computer.intcode[5])
        self.assertEqual(4,computer.intcode[6])
        self.assertEqual(3,computer.intcode[7])
        self.assertEqual(99,computer.intcode[8])
    def test_runningIntcodeComputerExampleDay2(self):
        intcode = [1,9,10,3,2,3,11,0,99,30,40,50]
        computer = Intcode.computer(intcode)
        computer.running = True
        while computer.running:
            computer.takeStep()
        self.assertEqual(70, computer.intcode[3])
        self.assertEqual(3500, computer.intcode[0])
    def test_runCommandExampleDay2(self):
        intcode = [1,9,10,3,2,3,11,0,99,30,40,50]
        computer = Intcode.computer(intcode)
        computer.run()
        self.assertEqual(70, computer.intcode[3])
        self.assertEqual(3500, computer.intcode[0])

if __name__ == '__main__':
    unittest.main()
