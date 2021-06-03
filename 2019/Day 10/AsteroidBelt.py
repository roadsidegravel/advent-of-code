import math

def constructAsteroidMapFromFile(path):
    rawData = []
    with open(path) as file:
        rawData = file.readlines()
    cleanedData = [i.strip() for i in rawData]
    result = AsteroidMap(cleanedData)
    return result

class AsteroidMap:
    def __init__(self, mapData):
        self.numbersStringLength = 3
        self.mapData = mapData.copy()
        self.createAsteroidList()
        self.findPositionWithMostVisibleAsteroids()
        self.laserOrderNestedListFromBestPosition = self.createLaserOrderNestedListsFromPosition(self.bestPosition)
        self.laserOrderNamesFromBestPosition = self.createLaserOrderNamesFromNestedList(self.laserOrderNestedListFromBestPosition)

    def takeXFromAsteroidString(self,asteroidString):
        return int(asteroidString[0:self.numbersStringLength])
    def takeYFromAsteroidString(self,asteroidString):
        return int(asteroidString[self.numbersStringLength + 1:self.numbersStringLength + self.numbersStringLength + 1])

    def createAsteroidList(self):
        def padNumber(value,lengthAfterPadding = self.numbersStringLength):
            valueString = str(value)
            paddedList =  ['0']* lengthAfterPadding
            for i in range(1,len(valueString)+1):
                paddedList[-i] = valueString [-i]
            result = ''
            for i in range(0,len(paddedList)):
                result += str(paddedList[i])
            return result

        self.asteroidList = []
        for row in range(0,len(self.mapData)):
            rowString = str(self.mapData[row])
            for col in range(0,len(rowString)):
                if rowString[col] == '#':
                    paddedRow = padNumber(row)
                    paddedCol = padNumber(col)
                    self.asteroidList.append(f'{paddedCol}x{paddedRow}y')

    def countVisibleFromPosition(self,asteroidString):
        directionList = []
        if not asteroidString in self.asteroidList:
            raise ValueError(f'{asteroidString} is not in the asteroid list')
        referenceX = self.takeXFromAsteroidString(asteroidString)
        referenceY = self.takeYFromAsteroidString(asteroidString)
        for i in self.asteroidList:
            if i != asteroidString:
                direction = ''
                objectX = self.takeXFromAsteroidString(i)
                objectY = self.takeYFromAsteroidString(i)
                adjustedX = objectX-referenceX
                adjustedY = objectY-referenceY
                if adjustedX >= 0 and adjustedY >=0:
                    direction += 'A'
                elif adjustedX >= 0 and adjustedY < 0:
                    direction += 'B'
                elif adjustedX < 0 and adjustedY < 0:
                    direction += 'C'
                else:
                    direction += 'D'
                if adjustedX == 0:
                    ratio = 'X'
                elif adjustedY == 0:
                    ratio = 'Y'
                else:
                    ratio = adjustedY/adjustedX
                direction += str(ratio)
                if not direction in directionList:
                    directionList.append(direction)
        return len(directionList)

    def findPositionWithMostVisibleAsteroids(self):
        currentMostVisibleCount = 0
        result = None
        for a in self.asteroidList:
            counted = self.countVisibleFromPosition(a)
            if counted > currentMostVisibleCount:
                currentMostVisibleCount = counted
                result = a
        self.bestPosition = result
        self.bestPositionSeesCount = currentMostVisibleCount

    def createLaserOrderNestedListsFromPosition(self,asteroidString):
        unsortedObjectList = []
        for i in self.asteroidList:
            if not i == asteroidString:
                newObject = self.createAngleDistanceObjectFromAToReference(i,asteroidString)
                unsortedObjectList.append(newObject)
        allAnglesList = []
        for i in unsortedObjectList:
            angle = i.angle
            if angle not in allAnglesList:
                allAnglesList.append(angle)
        allAnglesList.sort()
        angledObjects = [[] for x in range(0,len(allAnglesList))]
        for i in allAnglesList:
            for u in unsortedObjectList:
                if i == u.angle:
                    angledObjects[allAnglesList.index(i)].append(u)
        for i in angledObjects:
            objectsAtAngle = i.copy()
            distances = []
            for u in objectsAtAngle:
                if u.distance not in distances:
                    distances.append(u.distance)
            distances.sort()
            sortedObjectsByDistance = []
            for d in range(0,len(distances)):
                for o in objectsAtAngle:
                    if o.distance == distances[d]:
                        sortedObjectsByDistance.append(o)
            angledObjects[angledObjects.index(i)] = sortedObjectsByDistance.copy()
        return angledObjects

    def createAngleDistanceObjectFromAToReference(self, aName,referenceName):
        referenceX = self.takeXFromAsteroidString(referenceName)
        referenceY = self.takeYFromAsteroidString(referenceName)
        objectX = self.takeXFromAsteroidString(aName)
        objectY = self.takeYFromAsteroidString(aName)
        adjustedX = objectX - referenceX
        adjustedY = objectY - referenceY
        distance = (adjustedX**2+adjustedY**2)**(1/2)
        cosObject = adjustedY/distance
        if adjustedX > 0:
            angle = 180-math.degrees(math.acos(cosObject))
        elif adjustedX < 0:
            angle = 180+math.degrees(math.acos(cosObject))
        elif adjustedX == 0:
            if adjustedY < 0:
                angle = 0.0
            if adjustedY > 0:
                angle = 180.0
        #print(angle)
        result = AngleDistanceAToReferenceObject(aName,referenceName,angle,distance)
        return result

    def createLaserOrderNamesFromNestedList(self,nestedList):
        myNestedList = nestedList.copy()
        for i in range(0,len(myNestedList)):
            myNestedList[i] = []
            myNestedList[i] = nestedList[i].copy()
            myNestedList[i].reverse()
        nameList = []
        while len(nameList) < self.bestPositionSeesCount:
            for i in range(0,len(myNestedList)):
                if len(myNestedList[i]) > 0:
                    object = myNestedList[i].pop()
                    nameList.append(object.name)
        return nameList







class AngleDistanceAToReferenceObject:
    def __init__(self, name, refenceObjectName, angle, distance):
        self.name = name
        self.referenceObjectName = refenceObjectName
        self.angle = angle
        self.distance = distance
    def __repr__(self):
        return self.name








