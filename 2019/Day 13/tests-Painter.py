import unittest
from unittest.mock import patch

from Painter import Map, constructRobotPainterFromPath, Painter, colorDictionary,drawDictionary, Representation

class MapTests(unittest.TestCase):
    def test_EmptyFieldStartCoordinatesValue0(self):
        emptyMap = Map()
        startCoor = emptyMap._Coordinates(0,0)
        self.assertEqual(0,startCoor.value)
    def test_EmptyFieldStartCoordinatesReprString(self):
        emptyMap = Map()
        startCoor = emptyMap._Coordinates(0,0)
        self.assertEqual('0x0y',str(startCoor))
    def test_EmptyFieldGetCoordinatesObject15xmin30y(self):
        emptyMap = Map()
        pos15xmin30y = emptyMap.getCoordinatesObjectAt(15,-30)
        self.assertTrue(isinstance(pos15xmin30y,Map._Coordinates))
        self.assertEqual(15,pos15xmin30y.x)
        self.assertEqual(-30,pos15xmin30y.y)
        self.assertEqual(0,pos15xmin30y.value)
    def test_EmptyFieldSet5x7yValueTo5AndThenGetIt(self):
        emptyMap = Map()
        x = 5
        y = 7
        value = 5
        emptyMap.setValueAtCoordinates(x,y,value)
        pos5x7y = emptyMap.getCoordinatesObjectAt(x,y)
        self.assertEqual(value,pos5x7y.value,f'getCoordinatesObjectAt')
        retrievedValue = emptyMap.getValueAtCoordinates(x,y)
        self.assertEqual(value,retrievedValue,f'getValueAtCoordinates')
    def test_EmptyPrintMap(self):
        emptyMap = Map()
        with patch('builtins.print') as p:
            emptyMap.printMap()
        p.assert_called_with([['.']])

class PainterTests(unittest.TestCase):
    def test_StartPositionPainter(self):
        painter = Painter()
        self.assertEqual(1,len(painter.map.knownCoordinatesObjects))
        self.assertEqual(['0x0y'],painter.map.knownCoordinatesNames)
        self.assertEqual(0,painter.currentPositionObject.x)
        self.assertEqual(0,painter.currentPositionObject.y)
        self.assertEqual(0,painter.currentPositionObject.value)
        self.assertEqual(12,painter.currentDirectionAsOnClock)
    def test_StartPositionReadColor(self):
        painter = Painter()
        retrievedValue = painter.getValueAtCurrentPosition()
        self.assertEqual(0,retrievedValue)
    def test_StartPositionPaintWhiteBlackWhite(self):
        painter = Painter()
        initialColor = painter.getValueAtCurrentPosition()
        self.assertEqual(0,initialColor,'intial color is black')
        painter.paintCurrentWhite()
        whiteCoat = painter.getValueAtCurrentPosition()
        self.assertEqual(1,whiteCoat,'white coat')
        painter.paintCurrentBlack()
        blackCoat = painter.getValueAtCurrentPosition()
        self.assertEqual(0,blackCoat,'black coat')
        painter.paintCurrentWhite()
        whiteFinish = painter.getValueAtCurrentPosition()
        self.assertEqual(1,whiteFinish,'white finish')
    def test_turnLeftFromNorth(self):
        painter = Painter()
        painter.turnLeft()
        curDir = painter.currentDirectionAsOnClock
        self.assertEqual(9,curDir)
    def test_turnRightFromNorth(self):
        painter = Painter()
        painter.turnRight()
        curDir = painter.currentDirectionAsOnClock
        self.assertEqual(3,curDir)
    def test_turnPlus533FromNorth(self):
        #12*44+5 = 533
        painter = Painter()
        painter.turnSome(533)
        curDir = painter.currentDirectionAsOnClock
        self.assertEqual(5,curDir)
    def test_turnMinus332FromNorth(self):
        #12*27+8 = 332
        painter = Painter()
        painter.turnSome(-332)
        curDir = painter.currentDirectionAsOnClock
        self.assertEqual(8, curDir)
    def test_goforwardNorth(self):
        painter = Painter()
        painter.moveOneForward()
        self.assertEqual(0,painter.currentPositionObject.x)
        self.assertEqual(1,painter.currentPositionObject.y)
    def test_MakeRightChessHorseJumpLMove(self):
        painter = Painter()
        painter.moveOneForward()
        painter.turnRight()
        painter.moveOneForward()
        painter.moveOneForward()
        self.assertEqual(2,painter.currentPositionObject.x)
        self.assertEqual(1,painter.currentPositionObject.y)
    def test_makeRightChessHorseJumpLMoveMapPrint(self):
        painter = Painter()
        painter.paintCurrentWhite()
        painter.moveOneForward()
        painter.paintCurrentWhite()
        painter.turnRight()
        painter.moveOneForward()
        painter.paintCurrentWhite()
        painter.moveOneForward()
        painter.paintCurrentWhite()
        with patch('builtins.print') as p:
            painter.map.printMap()
        p.assert_called_with([['#', '.', '.'], ['#', '#', '#']])


class RepresentationTests(unittest.TestCase):
    def test_colorDictionary0isBlack(self):
        self.assertEqual('black',colorDictionary[0])
    def test_colorDictionary1isWhite(self):
        self.assertEqual('white',colorDictionary[1])
    def test_drawDictionary0isBlack(self):
        self.assertEqual('.',drawDictionary[0])
    def test_drawDictionary1isWhite(self):
        self.assertEqual('#',drawDictionary[1])
    def test_colorReprensentationValue636RaisesValueError(self):
        colRep = Representation('color',colorDictionary)
        with self.assertRaises(ValueError) as e:
            colRep.convertKeyToValue(636)
        self.assertEqual('Key 636 is not in the color dictionary',str(e.exception))
    def test_drawReprensentationKey1ReturnsValueHekje(self):
        drawRep = Representation('draw',drawDictionary)
        key = 1
        value = drawRep.convertKeyToValue(key)
        self.assertEqual('#',value)
    def test_drawReprensentationValueHekjeReturnsKey1(self):
        drawRep = Representation('draw',drawDictionary)
        value = '#'
        key = drawRep.convertValueToKey(value)
        self.assertEqual(1,key)

class robotPainterTests(unittest.TestCase):
    pass

class constructRobotPainterFromPathTests(unittest.TestCase):
    def test_constructDay11RobotPainter(self):
        path ='Inputs/inputDay11'
        robotPainter = constructRobotPainterFromPath(path)
        robotPainter.run()
        self.assertEqual(2064,len(robotPainter.painter.map.knownCoordinatesNames))
        self.assertEqual(2064,len(robotPainter.painter.map.knownCoordinatesObjects))





if __name__ == '__main__':
    unittest.main()
