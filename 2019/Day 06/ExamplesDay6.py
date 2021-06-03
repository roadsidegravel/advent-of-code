import unittest
from UniversalOrbitMap import ConstructOrbitMapFromDataFile

class ExamplesDay6(unittest.TestCase):
    def test_Example1(self):
        path = 'example1'
        example1Map = ConstructOrbitMapFromDataFile(path)
        self.assertEqual(42,example1Map.totalNumberOfOrbits)



if __name__ == '__main__':
    unittest.main()
