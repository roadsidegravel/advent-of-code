import unittest
from unittest.mock import  patch
from  ArcadeCabinet import constructArcadeCabinetFromPath

class TestsArcadeCabinet(unittest.TestCase):
    def setUp(self):
        path = 'Inputs/inputDay13'
        self.arcadeCabinet = constructArcadeCabinetFromPath(path)
        self.arcadeCabinet.startGame()
        self.arcadeCabinet.populateScreen()
    def test_prettyPrint(self):
        with patch('builtins.print') as p:
            self.arcadeCabinet.printScreen()
        self.assertEqual(1170*3,len(self.arcadeCabinet.brain.outputs))
        self.assertEqual(1170,len(self.arcadeCabinet.screen.knownCoordinatesNames))
    def test_countBall(self):
        ballCount = self.arcadeCabinet.countObjectsOnScreenFromKey(4)
        self.assertEqual(1,ballCount)
    def test_countBlocks(self):
        blockCount = self.arcadeCabinet.countObjectsOnScreenFromKey(2)
        self.assertEqual(306,blockCount)

if __name__ == '__main__':
    unittest.main()
