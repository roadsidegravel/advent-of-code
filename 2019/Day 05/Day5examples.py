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

#https://queirozf.com/entries/python-unittest-examples-mocking-and-patching

import Intcode
class testDay5examples(unittest.TestCase):
    def test_Day5Part2Example1(self):
        intcode = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
        computerTrue = Intcode.computer(intcode)
        userInput8 = 8
        with patch('builtins.input', lambda *args: userInput8):
            computerTrue.run()
            self.assertEqual(1, computerTrue.outputs[0])
        computerFalse = Intcode.computer(intcode)
        userInput5 = 5
        with patch('builtins.input', lambda *args: userInput5):
            computerFalse.run()
            self.assertEqual(0, computerFalse.outputs[0])
    def test_Day5Part2Example2(self):
        intcode = [3,9,7,9,10,9,4,9,99,-1,8]
        computerEqual = Intcode.computer(intcode)
        userInputEqual = 8
        with patch('builtins.input', lambda *args: userInputEqual):
            computerEqual.run()
            self.assertEqual(0, computerEqual.outputs[0])
        computerLess = Intcode.computer(intcode)
        userInputLess = 5
        with patch('builtins.input', lambda *args: userInputLess):
            computerLess.run()
            self.assertEqual(1, computerLess.outputs[0])
    def test_Day5Part2Example3(self):
        intcode = [3,3,1108,-1,8,3,4,3,99]
        computerEqual = Intcode.computer(intcode)
        userInputEqual = 8
        with patch('builtins.input', lambda *args: userInputEqual):
            computerEqual.run()
            self.assertEqual(1, computerEqual.outputs[0])
        computerLess = Intcode.computer(intcode)
        userInputLess = 5
        with patch('builtins.input', lambda *args: userInputLess):
            computerLess.run()
            self.assertEqual(0, computerLess.outputs[0])
    def test_Day5Part2Example4(self):
        intcode = [3,3,1107,-1,8,3,4,3,99]
        computerEqual = Intcode.computer(intcode)
        userInputEqual = 8
        with patch('builtins.input', lambda *args: userInputEqual):
            computerEqual.run()
            self.assertEqual(0, computerEqual.outputs[0])
        computerLess = Intcode.computer(intcode)
        userInputLess = 5
        with patch('builtins.input', lambda *args: userInputLess):
            computerLess.run()
            self.assertEqual(1, computerLess.outputs[0])
    def test_Day5Part2Example5(self):
        intcode = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
        computerInputZero = Intcode.computer(intcode)
        userInputZero = 0
        with patch('builtins.input', lambda *args: userInputZero):
            computerInputZero.run()
            self.assertEqual(0, computerInputZero.outputs[0])
        computerInputNonZero = Intcode.computer(intcode)
        userInputNonZero = 1
        with patch('builtins.input', lambda *args: userInputNonZero):
            computerInputNonZero.run()
            self.assertEqual(1, computerInputNonZero.outputs[0])
    def test_Day5Part2Example6(self):
        intcode = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
        computerInputZero = Intcode.computer(intcode)
        userInputZero = 0
        with patch('builtins.input', lambda *args: userInputZero):
            computerInputZero.run()
            self.assertEqual(0, computerInputZero.outputs[0])
        computerInputNonZero = Intcode.computer(intcode)
        userInputNonZero = 1
        with patch('builtins.input', lambda *args: userInputNonZero):
            computerInputNonZero.run()
            self.assertEqual(1, computerInputNonZero.outputs[0])
    def test_Day5Part2Example7(self):
        intcode = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
        computerEqual = Intcode.computer(intcode)
        userInputEqual = 8
        with patch('builtins.input', lambda *args: userInputEqual):
            computerEqual.run()
            self.assertEqual(1000, computerEqual.outputs[0])
        computerLess = Intcode.computer(intcode)
        userInputLess = 5
        with patch('builtins.input', lambda *args: userInputLess):
            computerLess.run()
            self.assertEqual(999, computerLess.outputs[0])
        computerGreater = Intcode.computer(intcode)
        userInputGreater = 11
        with patch('builtins.input', lambda *args: userInputGreater):
            computerGreater.run()
            self.assertEqual(1001, computerGreater.outputs[0])

if __name__ == '__main__':
    unittest.main()
