colorDictionary = {0:'black',1:'white'}
drawDictionary = {0:'.',1:'#'}

from Intcode import computer

class Map:
    def __init__(self):
        self.knownCoordinatesObjects = []
        self.knownCoordinatesNames = []
    class _Coordinates:
        def __init__(self,x,y,value =0):
            self.x = x
            self.y = y
            self.value = value
        def __repr__(self):
            return Map._returnXYString(self,self.x,self.y)

    def _returnXYString(self,x,y):
        return f'{x}x{y}y'

    def getCoordinatesObjectAt(self,x,y):
        posString = self._returnXYString(x,y)
        if not posString in self.knownCoordinatesNames:
            newObject = self._Coordinates(x,y)
            self.knownCoordinatesObjects.append(newObject)
            self.knownCoordinatesNames.append(posString)
        posIndex = self.knownCoordinatesNames.index(posString)
        posObject = self.knownCoordinatesObjects[posIndex]
        return posObject

    def setValueAtCoordinates(self,x,y,value):
        currentObject = self.getCoordinatesObjectAt(x,y)
        currentObject.value = value

    def getValueAtCoordinates(self,x,y):
        currentObject = self.getCoordinatesObjectAt(x,y)
        result = currentObject.value
        return result

    def printMap(self,pretty=False, myReprensation = None,default=0):
        if myReprensation == None:
            printRepresentation = Representation('print',drawDictionary)
        else:
            printRepresentation = myReprensation
        minX = 0
        maxX = 0
        minY = 0
        maxY = 0
        for i in self.knownCoordinatesObjects:
            if i.x < minX:
                minX = i.x
            if i.x > maxX:
                maxX = i.x
            if i.y < minY:
                minY = i.y
            if i.y > maxY:
                maxY = i.y
        printWidth = abs(minX)+1+abs(maxX)
        printHeight = abs(minY)+1+abs(maxY)
        printGrid = [[] for c in range(printHeight)]
        for i in range(printHeight):
            printGrid[i] = [default for r in range(printWidth)]
        startx = printWidth-maxX-1
        starty = printHeight-maxY-1
        for r in range(printHeight):
            for c in range(printWidth):
                printGrid[r][c] = printRepresentation.convertKeyToValue(printGrid[r][c])
        for i in self.knownCoordinatesObjects:
            col = i.x+startx
            row = i.y+starty
            value = printRepresentation.convertKeyToValue(i.value)
            printGrid[row][col] = value
        if not pretty:
            print(printGrid)
        else:
            for i in range(printHeight):
                printString = ''
                for j in range(printWidth):
                    printString += printGrid[printHeight-i-1][j]+' '
                print(printString)

class Painter:
    def __init__(self):
        self.map = Map()
        self.startAtZeroXZeroY()
        self.currentDirectionAsOnClock = 12

    def startAtZeroXZeroY(self):
        x = 0
        y = 0
        self.moveTo(x,y)

    def moveTo(self,x,y):
        self.currentPositionObject = self.map.getCoordinatesObjectAt(x,y)

    def getValueAtCurrentPosition(self):
        result = self.currentPositionObject.value
        return result

    def paintKeyFromRepresentationValueAtCurrentPosition(self,value,dictionary):
        paintRepresentation = Representation('Paint',dictionary)
        key = paintRepresentation.convertValueToKey(value)
        self.currentPositionObject.value = key

    def paintCurrentBlack(self):
        self.paintKeyFromRepresentationValueAtCurrentPosition('black',colorDictionary)
    def paintCurrentWhite(self):
        self.paintKeyFromRepresentationValueAtCurrentPosition('white',colorDictionary)
    def turnSome(self,turnAmount):
        newDirection = self.currentDirectionAsOnClock+turnAmount
        if newDirection > 12:
            adjustedDirection = newDirection%12
        elif newDirection <= 0:
            adjustedDirection = 12-newDirection%12
        else:
            adjustedDirection = newDirection
        self.currentDirectionAsOnClock = adjustedDirection
    def turnLeft(self):
        self.turnSome(-3)
    def turnRight(self):
        self.turnSome(3)
    def moveOneForward(self):
        oldX = self.currentPositionObject.x
        oldY = self.currentPositionObject.y
        if self.currentDirectionAsOnClock == 12:
            newX = oldX
            newY = oldY+1
        elif self.currentDirectionAsOnClock == 3:
            newX = oldX+1
            newY = oldY
        elif self.currentDirectionAsOnClock == 6:
            newX = oldX
            newY = oldY-1
        elif self.currentDirectionAsOnClock == 9:
            newX = oldX-1
            newY = oldY
        else:
            raise Exception(f'You done goofed @ moveOneForward {self.currentDirectionAsOnClock}')
        self.moveTo(newX,newY)

class Representation:
    def __init__(self,name,dictionary):
        self.name = name
        self.representationDictionary = dictionary.copy()

    def convertKeyToValue(self,key):
        if key in self.representationDictionary:
            return self.representationDictionary[key]
        else:
            raise ValueError(f'Key {key} is not in the {self.name} dictionary')
    def convertValueToKey(self,value):
        if value in self.representationDictionary.values():
            for key in self.representationDictionary:
                if value == self.representationDictionary[key]:
                    return key
        else:
            raise ValueError(f'value {value} is not in the {self.name} dictionary')

class RobotPainter:
    def __init__(self,intcodeList):
        self.brain = computer(intcodeList,automaticMode=True)
        self.painter = Painter()

    def performActions(self):
        cameraValue = self.painter.getValueAtCurrentPosition()
        self.brain.automaticModeTakeInputAndUnpauze(cameraValue)
        first = self.brain.outputs[-2]
        second = self.brain.outputs[-1]
        if first == 0:
            self.painter.paintCurrentBlack()
        elif first == 1:
            self.painter.paintCurrentWhite()
        else:
            raise Exception(f'performActions doesnt know what to do with first: {first}')
        if second == 0:
            self.painter.turnLeft()
        elif second == 1:
            self.painter.turnRight()
        else:
            raise Exception(f'performActions doesnt know what to do with second: {second}')
        self.painter.moveOneForward()

    def run(self):
        self.performActions()
        while self.brain.log[-1] != 'opcode 99, exiting':
            self.performActions()

def constructRobotPainterFromPath(path):
    rawData = []
    with open(path) as file:
        rawData = file.readlines()
    rawIntcode = rawData[0].split(',')
    intcode = []
    for i in range(0, len(rawIntcode)):
        intcode.append(int(rawIntcode[i]))
    result = RobotPainter(intcode)
    return result




