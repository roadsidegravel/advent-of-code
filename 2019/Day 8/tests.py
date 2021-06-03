import unittest
from unittest.mock import patch

from SpaceImagingFormat import SIFLayers
class TestsSIFLayers(unittest.TestCase):
    def setUp(self):
        data = 123456789012
        width = 3
        height = 2
        self.example1Layers = SIFLayers(data, width, height)
    def tearDown(self):
        self.example1Layers = None
    def test_Example1FromString(self):
        self.assertEqual(2,len(self.example1Layers.layerList))
        self.assertEqual('123456',self.example1Layers.layerList[0])
        self.assertEqual('789012',self.example1Layers.layerList[1])
    def test_Example1FewestZeroesLayer(self):
        self.assertEqual(0,self.example1Layers.fewestZeroLayerID)
    def test_Example1MultiplicationOnFewestZeroesLayer(self):
        self.assertEqual(1,self.example1Layers.returnOnFewestZeroesLayerMultiplyOneCountByTwoCount())


from SpaceImagingFormat import constructSIFLayersFromFile
class TestsConstructSIFLayersFromFile(unittest.TestCase):
    def setUp(self):
        path = 'example1'
        width = 3
        height = 2
        self.example1Layers = constructSIFLayersFromFile(path,width,height)
    def tearDown(self):
        self.example1Layers = None
    def test_Example1FromData(self):
        self.assertEqual(2, len(self.example1Layers.layerList))
        self.assertEqual('123456', self.example1Layers.layerList[0])
        self.assertEqual('789012', self.example1Layers.layerList[1])
    def test_Example1FromDataFewestZeroesLayer(self):
        self.assertEqual(0, self.example1Layers.fewestZeroLayerID)
    def test_Example1FromDataMultiplicationOnFewestZeroesLayer(self):
        self.assertEqual(1, self.example1Layers.returnOnFewestZeroesLayerMultiplyOneCountByTwoCount())

from SpaceImagingFormat import DecodedSIF
class TestsDecodedSIFFromString(unittest.TestCase):
    def setUp(self):
        string = '0222112222120000'
        width = 2
        height = 2
        layers = SIFLayers(string, width, height)
        self.image = DecodedSIF(layers)
    def tearDown(self):
        self.image = None
    def test_Example2FromString(self):
        self.assertEqual(4,len(self.image.pixelList))
        self.assertEqual('0120',self.image.pixelList[0])
        self.assertEqual('2120',self.image.pixelList[1])
        self.assertEqual('2210',self.image.pixelList[2])
        self.assertEqual('2220',self.image.pixelList[3])
    def testExample2FromStringTopPixels(self):
        self.assertEqual(4,len(self.image.topVisiblePixelList))
        self.assertEqual(['0', '1', '1', '0'], self.image.topVisiblePixelList)
    def testExample2FromStringImage(self):
        print(f'From string:')
        print(self.image)
        """with patch('builtins.print') as p:
            print(self.image)
            p.assert_called_with('01\n10')"""


from SpaceImagingFormat import constructDecodedSIFFromFile
class TestsConstructDecodedSIFFromFile(unittest.TestCase):
    def setUp(self):
        path = 'example2'
        width = 2
        height = 2
        self.image = constructDecodedSIFFromFile(path, width, height)
    def tearDown(self):
        self.image = None
    def test_Example2FromFile(self):
        self.assertEqual(4, len(self.image.pixelList))
        self.assertEqual('0120', self.image.pixelList[0])
        self.assertEqual('2120', self.image.pixelList[1])
        self.assertEqual('2210', self.image.pixelList[2])
        self.assertEqual('2220', self.image.pixelList[3])
    def testExample2FromFileTopPixels(self):
        self.assertEqual(4,len(self.image.topVisiblePixelList))
        self.assertEqual(['0', '1', '1', '0'], self.image.topVisiblePixelList)
    def testExample2FromFileImage(self):
        print(f'From file:')
        print(self.image)

if __name__ == '__main__':
    unittest.main()
