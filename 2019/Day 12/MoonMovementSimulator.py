import time

class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        returnString = f'{self.x}x,{self.y}y,{self.z}z'
        return returnString

class Moon:
    def __init__(self,posX,posY,posZ,name = 'moon'):
        self.positionVector = Vector(posX,posY,posZ)
        self.velocityVector = Vector(0,0,0)
        self.name = name

    def __repr__(self):
        returnString = f'{self.name} with position {str(self.positionVector)} and velocity {str(self.velocityVector)}'
        return returnString


class Simulator:
    def __init__(self,moonObjectList):
        if len(moonObjectList) < 2:
            raise Exception(f'Please provide the Simulator with at least two moons')
        else:
            self.moonObjectList = moonObjectList.copy()
        self.currentTimeStep = 0
        self.logOfStepPrintOutsFast = set((self.currentSimDataPrintOut(fastStringMode=True)))
        self.startTime = time.time()
        #self.logOfStepPrintOutsFast.add(self.currentSimDataPrintOut(fastStringMode=True))
    def takeOneTimeStep(self):
        self.currentTimeStep += 1
        self.applyGravityEffects()
        self.applyVelocityEffects()

    def skipToTimeStep(self,timeStep):
        if timeStep > self.currentTimeStep:
            while self.currentTimeStep < timeStep:
                self.takeOneTimeStep()
        else:
            raise ValueError(f'time can only move forward, pick a later timeStep to skip to, current {self.currentTimeStep} skip to {timeStep}')

    def applyGravityEffects(self):
        for moon in self.moonObjectList:
            for otherMoon in self.moonObjectList:
                if moon != otherMoon:
                    xvelocityChange = 0
                    if moon.positionVector.x < otherMoon.positionVector.x:
                        xvelocityChange += 1
                    if moon.positionVector.x > otherMoon.positionVector.x:
                        xvelocityChange += -1
                    moon.velocityVector.x += xvelocityChange
                    yvelocityChange = 0
                    if moon.positionVector.y < otherMoon.positionVector.y:
                        yvelocityChange += 1
                    if moon.positionVector.y > otherMoon.positionVector.y:
                        yvelocityChange += -1
                    moon.velocityVector.y += yvelocityChange
                    zvelocityChange = 0
                    if moon.positionVector.z < otherMoon.positionVector.z:
                        zvelocityChange += 1
                    if moon.positionVector.z > otherMoon.positionVector.z:
                        zvelocityChange += -1
                    moon.velocityVector.z += zvelocityChange

    def applyVelocityEffects(self):
        for moon in self.moonObjectList:
            moon.positionVector.x += moon.velocityVector.x
            moon.positionVector.y += moon.velocityVector.y
            moon.positionVector.z += moon.velocityVector.z

    def currentSimDataPrintOut(self,printInLog=False,fastStringMode=False):
        #set printInLog to True for easy visual check
        if fastStringMode:
            if len(self.moonObjectList) != 4:
                raise AssertionError('This was speed optimized for 4 moons!!')
            moon0 = str(self.moonObjectList[0])
            moon1 = str(self.moonObjectList[1])
            moon2 = str(self.moonObjectList[2])
            moon3 = str(self.moonObjectList[3])
            fastString = f'{moon0}+{moon1}+{moon2}+{moon3}'
            return fastString
        else:
            printOut = []
            printOut.append(f'Simulator state at time step {self.currentTimeStep}')
            for i in range(len(self.moonObjectList)):
                printOut.append(str(self.moonObjectList[i]))
            if printInLog:
                for i in range(len(printOut)):
                    print(printOut[i])

            return printOut


    def calculateCurrentTotalEnergy(self):
        result = 0
        for moon in self.moonObjectList:
            pot = 0
            pot += abs(moon.positionVector.x)
            pot += abs(moon.positionVector.y)
            pot += abs(moon.positionVector.z)
            kin = 0
            kin += abs(moon.velocityVector.x)
            kin += abs(moon.velocityVector.y)
            kin += abs(moon.velocityVector.z)
            energy = pot*kin
            result += energy
        return result

    def takeStepsTillSimRepeats(self):
        keepGoing = True
        counter = 0
        while keepGoing:
            counter += 1
            newPrintOutFast = self.currentSimDataPrintOut(fastStringMode=True)
            if newPrintOutFast in self.logOfStepPrintOutsFast:
                    keepGoing = False
            self.logOfStepPrintOutsFast.add(newPrintOutFast)
            if keepGoing:
                self.takeOneTimeStep()
            if counter == 100000:
                currentTime = time.time()
                print(f'{self.currentTimeStep} timegap: {currentTime-self.startTime}')
                self.startTime = currentTime
                counter = 0



def constructMoonListFromPath(path):
    rawData = []
    with open(path) as file:
        rawData = file.readlines()
    rawMoonPositions =[]
    for i in range(len(rawData)):
        strippedRawData = rawData[i].strip()
        replacedAndStrippedData = strippedRawData.replace('<','').replace('>','')
        rawMoonPositions.append(replacedAndStrippedData)
    moonList = []
    for i in range(len(rawMoonPositions)):
        rawMoonPositionString = rawMoonPositions[i]
        splitMoonPosition = rawMoonPositionString.split(',')
        xString = splitMoonPosition[0].replace('x=','')
        x = int(xString)
        yString = splitMoonPosition[1].replace('y=','')
        y = int(yString)
        zString = splitMoonPosition[2].replace('z=','')
        z = int(zString)
        newMoon = Moon(x,y,z)
        moonList.append(newMoon)
        result = moonList
    return result

def constructSimulatorFromPath(path):
    moonList = constructMoonListFromPath(path)
    sim =Simulator(moonList)
    return sim

