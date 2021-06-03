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

from WireGrid import wireGrid,ManhattanDistance,wirePath
class testWireGrid(unittest.TestCase):
    def test_EmptyWireGrid(self):
        wireLayout = wireGrid()
        origin = wireLayout.O
        self.assertEqual(0,origin.x,f'origin x coordinate should be 0')
        self.assertEqual(0,origin.y,f'origin y coordinate should be 0')
    def test_ManhattanDistance5x6y(self):
        result = ManhattanDistance(5,6)
        self.assertEqual(11,result,f'Manhattan distance for 5,6 should be 11')
    def test_ManhattanDistance0xminus5y(self):
        result = ManhattanDistance(0,-5)
        self.assertEqual(5, result, f'Manhattan distance for 0,-5 should be 5')
    def test_wirePathR3(self):
        wire = wirePath(['R3'])
        result = wire.locations
        self.assertEqual(4,len(result),f'R3 should be 4 positions, O and 0,1 0,2 0,3')
        self.assertEqual(0, result[0].x, f'R3 should be 4 positions, O and 0,1 0,2 0,3')
        self.assertEqual(0, result[0].y, f'R3 should be 4 positions, O and 0,1 0,2 0,3')
        self.assertEqual(1, result[1].x, f'R3 should be 4 positions, O and 0,1 0,2 0,3')
        self.assertEqual(0, result[1].y, f'R3 should be 4 positions, O and 0,1 0,2 0,3')
        self.assertEqual(2, result[2].x, f'R3 should be 4 positions, O and 0,1 0,2 0,3')
        self.assertEqual(0, result[2].y, f'R3 should be 4 positions, O and 0,1 0,2 0,3')
        self.assertEqual(3, result[3].x, f'R3 should be 4 positions, O and 0,1 0,2 0,3')
        self.assertEqual(0, result[3].y, f'R3 should be 4 positions, O and 0,1 0,2 0,3')
    def test_wirePathU2(self):
        wire = wirePath(['U2'])
        result = wire.locations
        self.assertEqual(3,len(result),f'U2 should be 3 positions, O, and 1,0 2,0')
        self.assertEqual(0, result[0].x, f'U2 should be 3 positions, O, and 1,0 2,0')
        self.assertEqual(0, result[0].y, f'U2 should be 3 positions, O, and 1,0 2,0')
        self.assertEqual(0, result[1].x, f'U2 should be 3 positions, O, and 1,0 2,0')
        self.assertEqual(1, result[1].y, f'U2 should be 3 positions, O, and 1,0 2,0')
        self.assertEqual(0, result[2].x, f'U2 should be 3 positions, O, and 1,0 2,0')
        self.assertEqual(2, result[2].y, f'U2 should be 3 positions, O, and 1,0 2,0')
    def test_wirePathL1(self):
        wire = wirePath(['L1'])
        result = wire.locations
        self.assertEqual(2, len(result), f'L1 should be 2 positions, O, and -1,0')
        self.assertEqual(0, result[0].x, f'L1 should be 2 positions, O, and -1,0')
        self.assertEqual(0, result[0].y, f'L1 should be 2 positions, O, and -1,0')
        self.assertEqual(-1, result[1].x, f'L1 should be 2 positions, O, and -1,0')
        self.assertEqual(0, result[1].y, f'L1 should be 2 positions, O, and -1,0')
    def test_wirePathD1(self):
        wire = wirePath(['D1'])
        result = wire.locations
        self.assertEqual(2, len(result), f'D1 should be 2 positions, O, and 0,-1')
        self.assertEqual(0, result[0].x, f'D1 should be 2 positions, O, and 0,-1')
        self.assertEqual(0, result[0].y, f'D1 should be 2 positions, O, and 0,-1')
        self.assertEqual(0, result[1].x, f'D1 should be 2 positions, O, and 0,-1')
        self.assertEqual(-1, result[1].y, f'D1 should be 2 positions, O, and 0,-1')
    def test_wirePathXUnknownCatcher(self):
        #had eerder gemoeten
        #https://medium.com/python-pandemonium/testing-sys-exit-with-pytest-10c6e5f7726f
        with self.assertRaises(SystemExit) as e:
            wirePath(['X2'])
        self.assertEqual('@wirepath, requested direction not understood: X',e.exception.code)
    def test_wirePathL2D1(self):
        wire = wirePath(['L2','D1'])
        result = wire.locations
        self.assertEqual(4,len(result))
        self.assertEqual(-2,result[-1].x)
        self.assertEqual(-1,result[-1].y)
    def test_wirePathExampleDay3(self):
        wire = wirePath(['R8','U5','L5','D3'])
        result = wire.locations
        self.assertEqual(3,result[-1].x)
        self.assertEqual(2,result[-1].y)
    def test_wireGridTwoWires(self):
        wireALocations = wirePath(['R8','U5','L5','D3']).locations
        wireBLocations = wirePath(['U7','R6','D4','L4']).locations
        wiresOnGrid = wireGrid([wireALocations,wireBLocations])
        lastWireAOnGrid = wiresOnGrid.wireLocations[0][-1]
        lastWireBOnGrid = wiresOnGrid.wireLocations[1][-1]
        self.assertEqual(3,lastWireAOnGrid.x)
        self.assertEqual(2,lastWireAOnGrid.y)
        self.assertEqual(2,lastWireBOnGrid.x)
        self.assertEqual(3,lastWireBOnGrid.y)
    def test_wireGridIntersections(self):
        wireALocations = wirePath(['R8','U5','L5','D3']).locations
        wireBLocations = wirePath(['U7','R6','D4','L4']).locations
        wiresOnGrid = wireGrid([wireALocations, wireBLocations])
        intersections = wiresOnGrid.intersections
        self.assertEqual(2,len(intersections))
        ManhattanX1 = ManhattanDistance(intersections[0].x,intersections[0].y)
        self.assertEqual(11,ManhattanX1)
        ManhattanX2 = ManhattanDistance(intersections[1].x,intersections[1].y)
        self.assertEqual(6,ManhattanX2)
    def test_ManhattanAcceptsXYclass(self):
        wireALocations = wirePath(['R8', 'U5', 'L5', 'D3']).locations
        wireBLocations = wirePath(['U7', 'R6', 'D4', 'L4']).locations
        wiresOnGrid = wireGrid([wireALocations, wireBLocations])
        intersections = wiresOnGrid.intersections
        self.assertEqual(2, len(intersections))
        ManhattanX1 = ManhattanDistance(intersections[0])
        ManhattanX2 = ManhattanDistance(intersections[1])
        self.assertEqual(11, ManhattanX1)
        self.assertEqual(6, ManhattanX2)
    def test_ManhattanAcceptsXYList(self):
        wireALocations = wirePath(['R8', 'U5', 'L5', 'D3']).locations
        wireBLocations = wirePath(['U7', 'R6', 'D4', 'L4']).locations
        wiresOnGrid = wireGrid([wireALocations, wireBLocations])
        intersections = wiresOnGrid.intersections
        Manhattans = ManhattanDistance(intersections)
        self.assertEqual(2,len(Manhattans))
        self.assertEqual(11,Manhattans[0])
        self.assertEqual(6,Manhattans[1])
    def test_Example1(self):
        path = 'example1'
        wiresExample1 = wireGrid(path)
        closestManhattan = wiresExample1.closestManhattan
        self.assertEqual(159,closestManhattan)
    def test_Example2(self):
        path = 'example2'
        wiresExample2 = wireGrid(path)
        closestManhattan = wiresExample2.closestManhattan
        self.assertEqual(135,closestManhattan)
    def test_speedup(self):
        #self.assertEqual('day3','solution correct but its way too slow')
        #made changes to _intersections, slow part found and fixed
        pass
    def test_intersectionDistanceExample1part2(self):
        path = 'part2example1'
        wiresOnGrid = wireGrid(path)
        closest = wiresOnGrid.shortedDistance
        self.assertEqual(610,closest)
    def test_intersectionDistanceExample2part2(self):
        path = 'part2example2'
        wiresOnGrid = wireGrid(path)
        closest = wiresOnGrid.shortedDistance
        self.assertEqual(410,closest)









if __name__ == '__main__':
    unittest.main()
