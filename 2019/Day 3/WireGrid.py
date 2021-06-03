class wireGrid:
    def __init__(self,wireLocations = []):
        self.O = xy(0,0)
        self.wireLocations = []
        print('loading wireLocations')
        if isinstance(wireLocations,list):
            self.wireLocations = wireLocations.copy()
        elif isinstance(wireLocations,str):
            rawdata = None
            with open(wireLocations) as file:
                rawData = file.readlines()
                self._readRawData(rawData)
        print('wirelocations loaded, finding intersections')
        self._findIntersections()
        print('intersections found, calculating manhattans')
        self._findManhattans()
        print('manhattans found, finding closest one')
        self._findClosestManhattan()
        self._findDistances()
        self._findShortestDistance()

    def _readRawData(self,rawData):
        for r in rawData:
            wireDirections = r.replace('\n','').split(',')
            wireLocations = wirePath(wireDirections).locations
            self.wireLocations.append(wireLocations)

    def _findIntersections(self):
        self.intersections = []
        self._intersectionIndexesA = []
        self._intersectionIndexesB = []
        """Works but gets too slow
        if len(self.wireLocations) is 2:
            for e in self.wireLocations[0]:
                for f in self.wireLocations[1]:
                    if e.x == f.x:
                        if e.y == f.y:
                            if e.x != 0 and e.y != 0:
                                self.intersections.append(xy(e.x,e.y))
        """
        if len(self.wireLocations) is 2:
            print('transforming wire A to strings')
            wireCoordinatesA = []
            for i in range(1,len(self.wireLocations[0])):
                currentLocation = self.wireLocations[0][i]
                xCoor = str(currentLocation.x)+'x'
                yCoor = str(currentLocation.y)
                coordinates = xCoor+yCoor
                wireCoordinatesA.append(coordinates)
            print('transforming wire B to strings')
            wireCoordinatesB = []
            for i in range(1,len(self.wireLocations[1])):
                currentLocation = self.wireLocations[1][i]
                xCoor = str(currentLocation.x) + 'x'
                yCoor = str(currentLocation.y)
                coordinates = xCoor + yCoor
                wireCoordinatesB.append(coordinates)
            print('looking for intersections')
            #https://www.codespeedy.com/find-the-common-elements-in-two-lists-in-python/ second one
            intersectingCoordinates = list(set(wireCoordinatesA) & set(wireCoordinatesB))
            intersectingCoordinatesIndexA = []
            for a in intersectingCoordinates:
                intersectingCoordinatesIndexA.append(wireCoordinatesA.index(a))
            intersectingCoordinatesIndexA.sort()
            for a in intersectingCoordinatesIndexA:
                asplit = wireCoordinatesA[a].split('x')
                ax = int(asplit[0])
                ay = int(asplit[1])
                aXY = xy(ax,ay)
                self.intersections.append(aXY)
            #intersection distances
            for a in intersectingCoordinates:
                self._intersectionIndexesA.append(wireCoordinatesA.index(a))
                self._intersectionIndexesB.append(wireCoordinatesB.index(a))



    def _findManhattans(self):
        self.manhattans = ManhattanDistance(self.intersections)

    def _findClosestManhattan(self):
        result = None
        if len(self.manhattans) > 0:
            Manhattans = self.manhattans.copy()
            Manhattans.sort()
            result = Manhattans[0]
        self.closestManhattan = result

    def _findDistances(self):
        self._distances = []
        for i in range(0,len(self._intersectionIndexesA)):
            distance = self._intersectionIndexesA[i]+1+self._intersectionIndexesB[i]+1
            self._distances.append(distance)

    def _findShortestDistance(self):
        if len(self._distances) > 0:
            self._distances.sort()
            self.shortedDistance = self._distances[0]
        else:
            self.shortedDistance = None


def ManhattanDistance(*args):
    resultList = []
    result = None
    for a in args:
        #it's an xy object
        if isinstance(a,xy):
            #multiple xy objects
            if len(args) > 1:
                resultList.append(abs(a.x) + abs(a.y))
            #only one xy object
            else:
                result = abs(a.x)+abs(a.y)
        #input is two ints
        if isinstance(a,int):
            if len(args) is 2:
                result = abs(args[0])+abs(args[1])
        #input is a list of xy
        if isinstance(a,list):
            for i in a:
                if isinstance(i,xy):
                    resultList.append(abs(i.x)+abs(i.y))
    if result is None:
        return resultList
    else:
        return result

class xy:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class wirePath:
    def __init__(self,directions):
        self.locations = [xy(0,0)]
        for i in range(0,len(directions)):
            direction = directions[i][0]
            distance = directions[i][1:]
            #print(f'for {directions[i]} the direction is {direction} and the distance is {distance}')
            self._addLocations(direction,distance)
    def _addLocations(self,direction,distance):
        dirX = 0
        dirY = 0
        if direction is 'R':
            dirX = 1
        elif direction is 'L':
            dirX = -1
        elif direction is 'U':
            dirY = 1
        elif direction is 'D':
            dirY = -1
        else:
            quit(f'@wirepath, requested direction not understood: {direction}')

        distance = int(distance)
        for i in range(1,distance+1):
            latestLocation = self.locations[-1]
            newX = latestLocation.x+dirX
            newY = latestLocation.y+dirY
            newLocation = xy(newX,newY)
            self.locations.append(newLocation)


