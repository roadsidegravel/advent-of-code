movementDictionary = {'north':1,'south':2,'west':3,'east':4}
statusDictionary = {-4:'s',-3:'D',-2:' ',-1:'?',0:'#',1:'.',2:'O'}

from Intcode import constructComputerFromFile
from Painter import  Map, Representation

class Hallways(Map):
    def __init__(self):
        super().__init__()
    class _Coordinates:
        def __init__(self,x,y,value =-1):
            self.x = x
            self.y = y
            self.value = value
        def __repr__(self):
            return Map._returnXYString(self,self.x,self.y)


class RepairDroid:
    def __init__(self, filePath):
        self.map = Hallways()
        self.brain = constructComputerFromFile(filePath,automaticMode=True)
        self.screenRepresentation = Representation('status', statusDictionary)
        self.pointsToExploreList = []
        self.currentPositionObject = None
        self.oxygenGeneratorPositionPair = None
        self.startAtZeroXZeroY()

    def xyFromPair(self,pair):
        x = pair[0]
        y = pair[-1]
        return x,y        

    def checkIfUnexplored(self,x, y):
        unexplored = -1
        return self.map.getValueAtCoordinates(x,y) == unexplored

    def fourDirectionsFromXY(self,x,y):
        north = [x, y + 1]
        south = [x, y - 1]
        east = [x + 1, y]
        west = [x - 1, y]
        return north, east, south, west

    def appendToExploreList(self,x,y):
        north, east, south, west = self.fourDirectionsFromXY(x,y)
        if north not in self.pointsToExploreList:
            xn, yn = self.xyFromPair(north)
            if self.checkIfUnexplored(xn, yn):
                self.pointsToExploreList.append(north)
        if south not in self.pointsToExploreList:
            xs, ys = self.xyFromPair(south)
            if self.checkIfUnexplored(xs, ys):
                self.pointsToExploreList.append(south)
        if east not in self.pointsToExploreList:
            xe, ye = self.xyFromPair(east)
            if self.checkIfUnexplored(xe, ye):
                self.pointsToExploreList.append(east)
        if west not in self.pointsToExploreList:
            xw, yw = self.xyFromPair(west)
            if self.checkIfUnexplored(xw, yw):
                self.pointsToExploreList.append(west)


    def exploreItemOnExploreList(self,index = -1):
        target = self.pointsToExploreList[index]
        xTarget, yTarget = self.xyFromPair(target)
        self.walkTo(xTarget,yTarget)
        
    def walkTo(self,xTarget,yTarget):
        pathWay = self.returnShortestPath(xTarget,yTarget)
        #print(f'pathWay is: {pathWay}')
        self.walkAlongPath(pathWay)
        
    def returnShortestPath(self,xTarget,yTarget):
        passable = (-4, -3, 1, 2)
        targetName = self.convertXYtoMapPointName(xTarget,yTarget)
        if not targetName in self.map.knownCoordinatesNames:
            raise Exception('You can only walk to a known point')
        targetValue = self.map.getValueAtCoordinates(xTarget,yTarget)
        if not targetValue in passable and not targetValue == -1:
            raise Exception('You can not walk to a revealed impassable tile')
        xStart = self.currentPositionObject.x
        yStart = self.currentPositionObject.y
        target = [xTarget,yTarget]
        targetReached = False
        pathWayTree = [[[xStart,yStart]]]
        if xStart == xTarget and yStart == yTarget:
            targetReached = True
        while not targetReached:
            newTree = []
            for pathWay in pathWayTree:
                xLast = pathWay[-1][0]
                yLast = pathWay[-1][1]
                north,east,south,west = self.fourDirectionsFromXY(xLast,yLast)
                valueNorth,valueEast,valueSouth,valueWest = self.getBorderingValues(xLast,yLast)
                directionList = [north,east,south,west]
                valueList = [valueNorth,valueEast,valueSouth,valueWest]
                for i in range(0,4):
                    curDirection = directionList[i]
                    curValue = valueList[i]
                    if not curDirection in pathWay:
                        if curDirection == target or curValue in passable:
                            newPathWay = pathWay.copy()
                            newPathWay.append(curDirection)
                            newTree.append(newPathWay)
                            if curDirection == target:
                                targetReached = True
            pathWayTree = newTree.copy()
        result = None
        for i in pathWayTree:
            if result == None and i[-1] == target:
                result = i[1:]
        return result
    

    def walkAlongPath(self,walkPath):
        for i in range(0,len(walkPath)):
            #print(f'path {walkPath} element {i} is {walkPath[i]}')            
            currentx,currenty = self.currentPositionObject.x,self.currentPositionObject.y
            targetx,targety = walkPath[i][0],walkPath[i][1]
            if currentx == targetx and currenty != targety:
                if currenty > targety:
                    self.trySouth()
                else:
                    self.tryNorth()
            elif currentx != targetx and currenty == targety:
                if currentx > targetx:
                    self.tryWest()
                else:
                    self.tryEast()

    def getBorderingValues(self,x,y):
        def retrieveBorderValue(repairDroid,borderPair):
            borderValue = None
            borderName = repairDroid.convertPairToMapPointName(borderPair)
            if borderName in repairDroid.map.knownCoordinatesNames:
                borderx, bordery = repairDroid.xyFromPair(borderPair)
                borderValue = repairDroid.map.getValueAtCoordinates(borderx,bordery)
            return borderValue

        valueNorth, valueEast, valueSouth, valueWest = None, None, None, None
        xyName = self.convertXYtoMapPointName(x,y)
        if self.checkMapNameInKnownList(xyName):
            north, east, south, west = self.fourDirectionsFromXY(x, y)
            valueNorth = retrieveBorderValue(self,north)
            valueEast = retrieveBorderValue(self,east)
            valueSouth = retrieveBorderValue(self,south)
            valueWest = retrieveBorderValue(self,west)
        return valueNorth, valueEast, valueSouth, valueWest
    
    def calculateOxygenFillTime(self):
        if len(self.pointsToExploreList) > 0:
            self.exploreAll()
        passable = (-4, -3, 1, 2)
        xStart = self.oxygenGeneratorPositionPair[0]
        yStart = self.oxygenGeneratorPositionPair[1]
        minutes = 0
        growth = True
        filledList = []
        borderList = [[xStart,yStart]]
        while len(borderList) > 0:
            newBorderList = []
            for filled in borderList:
                xfilled = filled[0]
                yfilled = filled[1]
                north,east,south,west = self.fourDirectionsFromXY(xfilled,yfilled)
                valueNorth,valueEast,valueSouth,valueWest = self.getBorderingValues(xfilled,yfilled)
                directionList = [north,east,south,west]
                valueList = [valueNorth,valueEast,valueSouth,valueWest]
                for i in range(0,4):
                    curDirection = directionList[i]
                    curValue = valueList[i]
                    if not curDirection in filledList:
                        if curValue in passable:
                            if not curDirection in borderList:
                                newBorderList.append(curDirection)
                filledList.append(filled)
                self.map.setValueAtCoordinates(xfilled,yfilled,2)
                borderList = newBorderList.copy()
            if len(borderList) > 0:
                minutes += 1
        result = minutes
        return result
            

    def checkMapNameInKnownList(self,mapName):
        result = mapName in self.map.knownCoordinatesNames
        return result


    def convertPairToMapPointName(self,pair):
        x,y = self.xyFromPair(pair)
        result = self.convertXYtoMapPointName(x,y)
        return result

    def convertXYtoMapPointName(self,x,y):
        return f'{x}x{y}y'

    def convertMapNameToXY(self,mapName):
        indexx = mapName.index('x')
        indexy = mapName.index('y')
        x = mapName[0:indexx]
        y = mapName[indexx+1:indexy]
        return int(x),int(y)

    def exploreAll(self):
        pointsToExploreCounter = len(self.pointsToExploreList)
        while pointsToExploreCounter > 0:
            self.exploreItemOnExploreList()
            #self.printMap()
            pointsToExploreCounter = len(self.pointsToExploreList)



    def startAtZeroXZeroY(self):
        x = 0
        y = 0
        self.map.setValueAtCoordinates(0, 0,1)
        self.currentPositionObject = self.map.getCoordinatesObjectAt(x,y)
        self.appendToExploreList(x,y)

    def moveTo(self,x,y):
        #overwrite inherited function
        self.walkTo(x,y)

    def tryNorth(self):
        xn = self.currentPositionObject.x
        yn = self.currentPositionObject.y+1
        self.brain.automaticModeTakeInputAndUnpauze(movementDictionary['north'])
        result = self.brain.outputs[-1]
        self.handleStatusResult(result,xn,yn)

    def trySouth(self):
        xs = self.currentPositionObject.x
        ys = self.currentPositionObject.y - 1
        self.brain.automaticModeTakeInputAndUnpauze(movementDictionary['south'])
        result = self.brain.outputs[-1]
        self.handleStatusResult(result, xs, ys)

    def tryEast(self):
        x = self.currentPositionObject.x+1
        y = self.currentPositionObject.y
        self.brain.automaticModeTakeInputAndUnpauze(movementDictionary['east'])
        result = self.brain.outputs[-1]
        self.handleStatusResult(result, x, y)

    def tryWest(self):
        x = self.currentPositionObject.x-1
        y = self.currentPositionObject.y
        self.brain.automaticModeTakeInputAndUnpauze(movementDictionary['west'])
        result = self.brain.outputs[-1]
        self.handleStatusResult(result, x, y)

    def handleStatusResult(self,statusResult,x,y):
        #print(f'status {statusResult} @ {x} {y}')
        self.map.setValueAtCoordinates(x, y, statusResult)
        if statusResult == 1 or statusResult == 2:
            oldx = self.currentPositionObject.x
            oldy = self.currentPositionObject.y
            oldv = self.currentPositionObject.value
            if oldv != 2:
                self.map.setValueAtCoordinates(oldx,oldy,1)
            self.currentPositionObject = self.map.getCoordinatesObjectAt(x,y)
            self.appendToExploreList(x,y)
        if statusResult == 2:
            self.oxygenGeneratorPositionPair = [x,y]
        point = [x,y]
        if point in self.pointsToExploreList:
            self.pointsToExploreList.remove(point)


    def printMap(self):
        if self.currentPositionObject.value != 2:
            x = self.currentPositionObject.x
            y = self.currentPositionObject.y
            self.map.setValueAtCoordinates(x,y,-3)
            self.currentPositionObject = self.map.getCoordinatesObjectAt(x,y)
        self.map.setValueAtCoordinates(0,0,-4)
        self.map.printMap(pretty=True,myReprensation=self.screenRepresentation,default=-2)
