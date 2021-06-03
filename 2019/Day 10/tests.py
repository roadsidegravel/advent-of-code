import unittest
from AsteroidBelt import AsteroidMap,constructAsteroidMapFromFile
# onzichtbaar als er een tweede is op dezelfde lijn
# dus de hoek berekenen, per kwadrant of referentie richting (noord?)
# basicly, zijn er vectoren met dezelfde hoek?
# punt A heeft x samenvallende vectoren
# punt B stoppen met berekenen zodra het >x samenvallende vectoren heeft


class TestsMapListHekjeDotjeHekjHekje(unittest.TestCase):
    def setUp(self):
        mapList = ['#.##']
        self.asteroidMap = AsteroidMap(mapList)
    def tearDown(self):
        self.asteroidMap = None
    def test_AsteroidList(self):
        self.assertEqual(['000x000y', '002x000y', '003x000y'],self.asteroidMap.asteroidList)
    def test_countVisibleThrowsException(self):
        with self.assertRaises(ValueError) as e:
            self.asteroidMap.countVisibleFromPosition('Jan')
        self.assertEqual('Jan is not in the asteroid list',str(e.exception))
    def test_visibleCountFrom000x000y(self):
        visibleCount = self.asteroidMap.countVisibleFromPosition('000x000y')
        self.assertEqual(1,visibleCount)
    def test_visibleCountFrom000x002y(self):
        visibleCount = self.asteroidMap.countVisibleFromPosition('002x000y')
        self.assertEqual(2,visibleCount)
    def test_mostDetectingLocation(self):
        self.assertEqual('002x000y',self.asteroidMap.bestPosition)
        self.assertEqual(2,self.asteroidMap.bestPositionSeesCount)
    def test_AngleDistanceObjectFrom000x000yTo003x000yDistance(self):
        asteroid = '000x000y'
        referenceAsteroid = '003x000y'
        angleDistanceObject = self.asteroidMap.createAngleDistanceObjectFromAToReference(asteroid,referenceAsteroid)
        self.assertEqual(3,angleDistanceObject.distance)
    def test_AngleDistanceObjectFrom000x000yTo003x000yDistance(self):
        asteroid = '000x000y'
        referenceAsteroid = '003x000y'
        angleDistanceObject = self.asteroidMap.createAngleDistanceObjectFromAToReference(asteroid,referenceAsteroid)
        self.assertEqual(270.0,angleDistanceObject.angle)
    def test_AngleDistanceObjectFrom003x000yTo000x000yDistance(self):
        asteroid = '003x000y'
        referenceAsteroid = '000x000y'
        angleDistanceObject = self.asteroidMap.createAngleDistanceObjectFromAToReference(asteroid,referenceAsteroid)
        self.assertEqual(3,angleDistanceObject.distance)
    def test_AngleDistanceObjectFrom003x000yTo000x000yDistance(self):
        asteroid = '003x000y'
        referenceAsteroid = '000x000y'
        angleDistanceObject = self.asteroidMap.createAngleDistanceObjectFromAToReference(asteroid,referenceAsteroid)
        self.assertEqual(90.0,angleDistanceObject.angle)
    def test_laserOrderNestedListsFromBestHekjeDotjeHekjeHekje(self):
        laserOrder = self.asteroidMap.laserOrderNestedListFromBestPosition
        self.assertEqual('[[003x000y], [000x000y]]',str(laserOrder))
    def test_laserOrderNamesFromBestHekjeDotjeHekjeHekje(self):
        laserOrder = self.asteroidMap.laserOrderNamesFromBestPosition
        self.assertEqual(['003x000y', '000x000y'],laserOrder)

class TestsMapListDiagonaleHekjes(unittest.TestCase):
    def setUp(self):
        maplist = ['..#','.#.','#..']
        self.asteroidMap = AsteroidMap(maplist)
    def tearDown(self):
        self.asteroidMap = None
    def test_AsteroidList(self):
        self.assertEqual(['002x000y', '001x001y', '000x002y'],self.asteroidMap.asteroidList)
    def test_visibleCount000x002y(self):
        visibleCount = self.asteroidMap.countVisibleFromPosition('002x000y')
        self.assertEqual(1, visibleCount)
    def test_visibleCount001x001y(self):
        visibleCount = self.asteroidMap.countVisibleFromPosition('001x001y')
        self.assertEqual(2, visibleCount)
    def test_AngleDistanceObjectFrom002x000yTo001x001yDistance(self):
        asteroid = '002x000y'
        referenceAsteroid = '001x001y'
        angleDistanceObject = self.asteroidMap.createAngleDistanceObjectFromAToReference(asteroid,referenceAsteroid)
        self.assertEqual(2**(1/2),angleDistanceObject.distance)
    def test_AngleDistanceObjectFrom002x000yTo001x001yDistance(self):
        asteroid = '002x000y'
        referenceAsteroid = '001x001y'
        angleDistanceObject = self.asteroidMap.createAngleDistanceObjectFromAToReference(asteroid,referenceAsteroid)
        self.assertEqual(45.0,angleDistanceObject.angle)
    def test_AngleDistanceObjectFrom000x002yTo001x001yDistance(self):
        asteroid = '000x002y'
        referenceAsteroid = '001x001y'
        angleDistanceObject = self.asteroidMap.createAngleDistanceObjectFromAToReference(asteroid,referenceAsteroid)
        self.assertEqual(2**(1/2),angleDistanceObject.distance)
    def test_AngleDistanceObjectFrom000x002yTo001x001yDistance(self):
        asteroid = '000x002y'
        referenceAsteroid = '001x001y'
        angleDistanceObject = self.asteroidMap.createAngleDistanceObjectFromAToReference(asteroid,referenceAsteroid)
        self.assertEqual(225.0,angleDistanceObject.angle)
    def test_laserOrderFromBestHekjeDiagonal(self):
        laserOrder = self.asteroidMap.laserOrderNestedListFromBestPosition
        self.assertEqual('[[002x000y], [000x002y]]',str(laserOrder))
    def test_laserOrderNamesFromBestHekjeDiagonal(self):
        laserOrder = self.asteroidMap.laserOrderNamesFromBestPosition
        self.assertEqual(['002x000y', '000x002y'],laserOrder)

class Examples(unittest.TestCase):
    def test_Example1CorrectlyLoadsMap(self):
        path = 'Examples\Day10Example1'
        asteroidMap = constructAsteroidMapFromFile(path)
        self.assertEqual(5,len(asteroidMap.mapData))
        self.assertEqual('.#..#', asteroidMap.mapData[0])
        self.assertEqual('.....', asteroidMap.mapData[1])
        self.assertEqual('#####', asteroidMap.mapData[2])
        self.assertEqual('....#', asteroidMap.mapData[3])
        self.assertEqual('...##', asteroidMap.mapData[4])
    def test_Example1AngleDistanceObjectFrom001x000yTo001x002yDistance(self):
        path = 'Examples\Day10Example1'
        asteroidMap = constructAsteroidMapFromFile(path)
        asteroid = '001x000y'
        referenceAsteroid = '001x002y'
        angleDistanceObject = asteroidMap.createAngleDistanceObjectFromAToReference(asteroid,referenceAsteroid)
        self.assertEqual(0.0,angleDistanceObject.angle)
    def test_Example1AngleDistanceObjectFrom001x002yTo001x000yDistance(self):
        path = 'Examples\Day10Example1'
        asteroidMap = constructAsteroidMapFromFile(path)
        asteroid = '001x002y'
        referenceAsteroid = '001x000y'
        angleDistanceObject = asteroidMap.createAngleDistanceObjectFromAToReference(asteroid,referenceAsteroid)
        self.assertEqual(180.0,angleDistanceObject.angle)
    def test_Example1CalculatesBestPosition(self):
        path = 'Examples\Day10Example1'
        asteroidMap = constructAsteroidMapFromFile(path)
        self.assertEqual('003x004y',asteroidMap.bestPosition)
        self.assertEqual(8,asteroidMap.bestPositionSeesCount)
    def test_Example2CalculatesBestPosition(self):
        path = 'Examples\Day10Example2'
        asteroidMap = constructAsteroidMapFromFile(path)
        self.assertEqual('005x008y',asteroidMap.bestPosition)
        self.assertEqual(33,asteroidMap.bestPositionSeesCount)
    def test_Example3CalculatesBestPosition(self):
        path = 'Examples\Day10Example3'
        asteroidMap = constructAsteroidMapFromFile(path)
        self.assertEqual('001x002y',asteroidMap.bestPosition)
        self.assertEqual(35,asteroidMap.bestPositionSeesCount)
    def test_Example4CalculatesBestPosition(self):
        path = 'Examples\Day10Example4'
        asteroidMap = constructAsteroidMapFromFile(path)
        self.assertEqual('006x003y',asteroidMap.bestPosition)
        self.assertEqual(41,asteroidMap.bestPositionSeesCount)
    def test_Example5CalculatesBestPosition(self):
        path = 'Examples\Day10Example5'
        asteroidMap = constructAsteroidMapFromFile(path)
        self.assertEqual('011x013y',asteroidMap.bestPosition)
        self.assertEqual(210,asteroidMap.bestPositionSeesCount)
    def test_Example5Get200thAsteroid(self):
        path = 'Examples\Day10Example5'
        asteroidMap = constructAsteroidMapFromFile(path)
        print(asteroidMap.laserOrderNamesFromBestPosition[200])




if __name__ == '__main__':
    unittest.main()
