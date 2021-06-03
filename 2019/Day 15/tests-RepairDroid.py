import unittest
from unittest.mock import  patch
from RepairDroid import RepairDroid
import Pickling


class RepairDroidTests(unittest.TestCase):
    def setUp(self):
        path = 'Inputs/InputDay15'
        self.repairDroid = RepairDroid(path)
    def tearDown(self):
        self.repairDroid = None
    def test_StartPositionPrintMap(self):
        with patch('builtins.print') as p:
            self.repairDroid.printMap()
        p.assert_called_with('  ?   ')
    def test_StartPositionPointsToExploreList(self):
        exploreList = self.repairDroid.pointsToExploreList
        self.assertEqual([[0, 1], [0, -1], [1, 0], [-1, 0]] ,exploreList)
    def test_TryNorthFromStartExploreList(self):
        self.repairDroid.tryNorth()
        exploreList = self.repairDroid.pointsToExploreList
        self.assertEqual([[0, -1], [1, 0], [-1, 0]],exploreList)
    def test_TrySouthFromStartPrintMap(self):
        self.repairDroid.trySouth()
        with patch('builtins.print') as p:
            self.repairDroid.printMap()
        p.assert_called_with('  #   ')
    def test_TryEastFromStartPrintMap(self):
        self.repairDroid.tryEast()
        self.repairDroid.tryEast()
        self.repairDroid.tryEast()
        with patch('builtins.print') as p:
            self.repairDroid.printMap()
        p.assert_called_with('  ? ? ?   ')
    def test_TryWestFromStartPrintMap(self):
        self.repairDroid.tryWest()
        with patch('builtins.print') as p:
            self.repairDroid.printMap()
        valueWest = self.repairDroid.map.getValueAtCoordinates(-1,0)
        self.assertEqual(0,valueWest)
    def test_exploreFromStart1(self):
        self.assertEqual([[0, 1], [0, -1], [1, 0], [-1, 0]],self.repairDroid.pointsToExploreList)
        self.repairDroid.exploreItemOnExploreList()
        self.assertEqual([[0, 1], [0, -1], [1, 0]],self.repairDroid.pointsToExploreList)
    def test_exploreFromStart6(self):
        self.assertEqual([[0, 1], [0, -1], [1, 0], [-1, 0]], self.repairDroid.pointsToExploreList)
        self.repairDroid.exploreItemOnExploreList()
        self.repairDroid.exploreItemOnExploreList()
        self.repairDroid.exploreItemOnExploreList()
        self.repairDroid.exploreItemOnExploreList()
        self.repairDroid.exploreItemOnExploreList()
        self.repairDroid.exploreItemOnExploreList()
        #self.repairDroid.printMap()
        self.assertEqual([[0, 1], [0, -1], [1, 1], [1, -1], [2, 1], [2, -2]],self.repairDroid.pointsToExploreList)
    def test_borderingValuesFromStartAt0x0y(self):
        values = self.repairDroid.getBorderingValues(0,0)
        self.assertEqual((-1, -1, -1, -1),values)
    def test_borderingValuesFromStartAt3x3y(self):
        values = self.repairDroid.getBorderingValues(3, 3)
        self.assertEqual((None,None,None,None), values,f'Unknown territory')
    def test_borderingValuesStartNorthNeighbour(self):
        xn,yn = 0,1
        valuesNorth = self.repairDroid.getBorderingValues(xn,yn)
        self.assertEqual((None, None, 1, None),valuesNorth,f'north neighbour bordering values')
    def test_borderingValuesStartSouthNeighbour(self):
        xs,ys =0,-1
        valuesSouth = self.repairDroid.getBorderingValues(xs,ys)
        self.assertEqual((1, None, None, None),valuesSouth,f'south neighbour bordering values')
    def test_borderingValuesExplore5fromStartAndAt2x0y(self):
        self.repairDroid.exploreItemOnExploreList()
        self.repairDroid.exploreItemOnExploreList()
        self.repairDroid.exploreItemOnExploreList()
        self.repairDroid.exploreItemOnExploreList()
        self.repairDroid.exploreItemOnExploreList()
        x,y = 2,0
        values = self.repairDroid.getBorderingValues(x,y)
        #self.repairDroid.printMap()
        self.assertEqual((-1, 0, 1, 1),values,f'explore 5 and get bordering values at 2x0y')
    def test_exploreAllFromStart(self):
        #print("skipping test exploreAll")
        self.repairDroid.exploreAll()
        #self.repairDroid.printMap()
        lenExploreList = len(self.repairDroid.pointsToExploreList)
        self.assertEqual(0,lenExploreList)
    def test_exploreAllOxyGenPos(self):
        self.repairDroid.exploreAll()
        oxyPos = self.repairDroid.oxygenGeneratorPositionPair
        #self.repairDroid.printMap()
        self.assertEqual([12,-14],oxyPos)
    def test_calculateOxygenFillTime(self):
        minutesTaken = self.repairDroid.calculateOxygenFillTime()
        print(minutesTaken)
        self.repairDroid.printMap()
    
class RepairDroidLoadedStateExplore40curPosMinus3Minus4Tests(unittest.TestCase):
    """
    def test_pickleAfter40(self):
        path = 'Inputs/InputDay15'
        self.repairDroid = RepairDroid(path)
        i = 0
        while i < 40:
            self.repairDroid.exploreItemOnExploreList()
            i += 1
        Picklee = self.repairDroid
        folderPath = 'SavedStates'
        fileName = 'savedState40ExploreItems'
        Pickling.pickleDump(Picklee,folderPath,fileName)
    """
    def setUp(self):
        folderPath = 'SavedStates'
        fileName = 'savedState40ExploreItems'
        self.repairDroid = Pickling.pickleLoad(folderPath,fileName)
    def tearDown(self):
        self.repairDroid = None
    def test_walkTominus4minus4(self):
        #self.repairDroid.printMap()
        xTarget = -4
        yTarget = -4
        self.repairDroid.walkTo(xTarget,yTarget)
        xCurrent = self.repairDroid.currentPositionObject.x
        yCurrent = self.repairDroid.currentPositionObject.y
        self.assertEqual(xTarget,xCurrent)
        self.assertEqual(yTarget,yCurrent)
        #self.repairDroid.printMap()
    def test_walkToUnknownGivesException(self):
        xTarget = -8
        yTarget = -4
        with self.assertRaises(Exception) as e:
            self.repairDroid.walkTo(xTarget,yTarget)
        self.assertEqual('You can only walk to a known point',str(e.exception))
    def test_walkToMinus2Minus4(self):
        #self.repairDroid.printMap()
        xTarget = -2
        yTarget = -4
        self.repairDroid.walkTo(xTarget,yTarget)
        xCurrent = self.repairDroid.currentPositionObject.x
        yCurrent = self.repairDroid.currentPositionObject.y
        self.assertEqual(xTarget,xCurrent)
        self.assertEqual(yTarget,yCurrent)
        #self.repairDroid.printMap()
    def test_walkToImpassableGivesException(self):
        xTarget = -1
        yTarget = -4
        with self.assertRaises(Exception) as e:
            self.repairDroid.walkTo(xTarget,yTarget)
        self.assertEqual('You can not walk to a revealed impassable tile',str(e.exception))
    def test_walkTo0x0y(self):
        #self.repairDroid.printMap()
        xTarget = 0
        yTarget = 0
        self.repairDroid.walkTo(xTarget,yTarget)
        xCurrent = self.repairDroid.currentPositionObject.x
        yCurrent = self.repairDroid.currentPositionObject.y
        self.assertEqual(xTarget,xCurrent)
        self.assertEqual(yTarget,yCurrent)
        #self.repairDroid.printMap()
    def test_walkToCurrentPosition(self):
        xTarget = -3
        yTarget = -4
        self.repairDroid.walkTo(xTarget,yTarget)
        xCurrent = self.repairDroid.currentPositionObject.x
        yCurrent = self.repairDroid.currentPositionObject.y
        self.assertEqual(xTarget,xCurrent)
        self.assertEqual(yTarget,yCurrent)
        
    
        
        
        
    
    



if __name__ == '__main__':
    unittest.main()
