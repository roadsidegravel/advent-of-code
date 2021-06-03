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

from password import password
class testsPassword(unittest.TestCase):
    def test_passwordRange5and10(self):
        lower = 5
        upper = 10
        pw = password(lower,upper)
        self.assertEqual(5,pw._lowerRange)
        self.assertEqual(10,pw._upperRange)
    def test_valueErrorLowerBiggerThanUpper(self):
        with self.assertRaises(ValueError) as e:
            lower = 8
            upper = 4
            pw = password(lower,upper)
    def test_valueErrorIfInputIsntInt(self):
        with self.assertRaises(ValueError) as e:
            lower = 'a'
            upper = []
            pw = password(lower,upper)
    def test_rule_sixDigitNumber(self):
        pw = password(3,6)
        result123 = pw._isSixDigits(123)
        self.assertFalse(result123)
        result123456 = pw._isSixDigits(123456)
        self.assertTrue(result123456)
        result12345678 = pw._isSixDigits(12345678)
        self.assertFalse(result12345678)
    def test_rule_twoAdjacentIdenticalDigits(self):
        pw = password(3,6)
        result1234 = pw._twoAdjacentIdenticalDigits(1234)
        self.assertFalse(result1234)
        result11 = pw._twoAdjacentIdenticalDigits(11)
        self.assertTrue(result11)
        result1234444 = pw._twoAdjacentIdenticalDigits(1234444)
        self.assertTrue(result1234444)
    def test_rule_leftToRightIncreasesOrSame(self):
        pw = password(3,6)
        result123 = pw._leftToRightIncreasesOrSame(123)
        self.assertTrue(result123)
        result321 = pw._leftToRightIncreasesOrSame(321)
        self.assertFalse(result321)
        result111 = pw._leftToRightIncreasesOrSame(111)
        self.assertTrue(result111)
    def test_allThreeRules(self):
        pw = password(3,6)
        result111111 = pw._allRules(111111)
        self.assertTrue(result111111)
        result223450 = pw._allRules(223450)
        self.assertFalse(result223450)
        result123789 = pw._allRules(123789)
        self.assertFalse(result123789)
    def test_inGivenRange1855Pass(self):
        pw = password(138307,654504)
        result = pw.criteriaMetCount
        self.assertEqual(1855,result)
    #part 2
    def test_cointainsTwo(self):
        pw = password(3,6)
        result112233 = pw._containsTwo(112233)
        self.assertTrue(result112233)
        result123444 = pw._containsTwo(123444)
        self.assertFalse(result123444)
        result111122 = pw._containsTwo(111122)
        self.assertTrue(result111122)
    def test_allFourRules1253Pass(self):
        pw = password(138307,654504)
        result = pw.fourCriteriaMetCount
        self.assertEqual(1253,result)




if __name__ == '__main__':
    unittest.main()