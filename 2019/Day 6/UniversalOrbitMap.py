class Object:
    def __init__(self,name,orbitsObject):
        self.name = str(name)
        self._setOrbitsObject(orbitsObject)
        self._setOrbitCount()

    def _setOrbitsObject(self,orbitsObject):
        if orbitsObject is None:
            self.orbitsObject = orbitsObject
        elif isinstance(orbitsObject,Object):
            self.orbitsObject = orbitsObject
        else:
            raise TypeError('orbitsObject should be an Object or None')

    def _setOrbitCount(self):
        if self.orbitsObject is None:
            result = 0
        else:
            result = self.orbitsObject.orbitCount+1
        self.orbitCount = result

class OrbitMap:
    def __init__(self,dataList):
        self.objects = []
        self.objectNames = []
        self.constructOrbitMapFromDataList(dataList)
        self.countAllOrbits()

    def constructOrbitMapFromDataList(self,dataList):
        def goThroughList(list):
            backLog = []
            for data in list:
                dataSplit = data.split(')')
                objectName = dataSplit[1]
                orbitsObjectName = dataSplit[0]
                if orbitsObjectName in self.objectNames:
                    orbitsObject = self.retrieveObjectFromObjectsList(orbitsObjectName)
                    self.addObjectToOrbitMap(objectName, orbitsObject)
                else:
                    backLog.append(data)
            if len(backLog) > 0:
                if len(backLog) < len(list):
                    goThroughList(backLog)
                else:
                    raise RecursionError(f'@constructOrbitmapFromDataList: goThroughList: backlog did not shrink')

        self.addObjectToOrbitMap('COM',None)
        goThroughList(dataList)



    def retrieveObjectFromObjectsList(self,objectName):
        index = self.objectNames.index(objectName)
        result = self.objects[index]
        return result

    def addObjectToOrbitMap(self, objectName,orbitsObject):
        newObject = Object(objectName,orbitsObject)
        self.objects.append(newObject)
        self.objectNames.append(self.objects[-1].name)

    def countAllOrbits(self):
        result = 0
        for o in self.objects:
            result += o.orbitCount
        self.totalNumberOfOrbits = result

    def BuildListOfAncestorNames(self,startName):
        startObject = self.retrieveObjectFromObjectsList(startName)
        ancestors = []
        startObjectDaddyObject = startObject.orbitsObject
        while startObjectDaddyObject != None:
            ancestors.append(startObjectDaddyObject.name)
            startObjectDaddyObject = startObjectDaddyObject.orbitsObject
        return ancestors

    def FindCommonAncestorNames(self,eddy,wally):
        eddyAncestorNames = self.BuildListOfAncestorNames(eddy)
        wallyAncestorNames = self.BuildListOfAncestorNames(wally)
        commonAncestorsNames = [i for i in eddyAncestorNames if i in wallyAncestorNames]
        return commonAncestorsNames

    def CalculateOrbitsBetweenTwoNames(self,eddy,wally):
        eddyDaddies = self.BuildListOfAncestorNames(eddy)
        wallyDaddies = self.BuildListOfAncestorNames(wally)
        commonDaddies = self.FindCommonAncestorNames(eddy,wally)
        result = len(eddyDaddies)+len(wallyDaddies)-2*len(commonDaddies)
        return result

def ConstructOrbitMapFromDataFile(path):
    rawData = []
    with open(path) as file:
        rawData = file.readlines()
    # https://stackoverflow.com/questions/3849509/how-to-remove-n-from-a-list-element
    cleanedData = [i.strip() for i in rawData]
    return OrbitMap(cleanedData)
