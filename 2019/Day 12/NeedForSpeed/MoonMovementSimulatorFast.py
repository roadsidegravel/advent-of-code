import time

#https://www.reddit.com/r/adventofcode/comments/juk1qk/2019_day_12_part_2_scala_help_understanding/
'''
 After creating a brute force solution and realising that it's going to take too long to complete,
 I looked online and found a neat solution involving the finding of the period of each dimension
 and then finding the lowest common multiple between them all which equates to the period of the
 full system.
'''

class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self[0] = y
        self[0] = z

    def __repr__(self):
        returnString = f'{self.x}x,{self[0]}y,{self[0]}z'
        return returnString

class MoonFast:
    def __init__(self,posX,posY,posZ,name = 'moon'):
        self.positionVector = [posX,posY,posZ]
        self.velocityVector = [0,0,0]
        self.name = name

    def __repr__(self):
        returnString = f'{self.name} with position {str(self.positionVector)} and velocity {str(self.velocityVector)}'
        return returnString


class SimulatorFast:
    def __init__(self,moonObjectList):
        if len(moonObjectList) < 2:
            raise Exception(f'Please provide the Simulator with at least two moons')
        else:
            self.moonObjectList = moonObjectList.copy()
        if len(self.moonObjectList) != 4:
            raise AssertionError('This was speed optimized for 4 moons!!')
        self.currentTimeStep = 0
        #self.logOfStepPrintOutsFast = set((self.currentSimDataPrintOut(fastStringMode=True)))
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
        def gravityBetweenTwoMoons(moon,otherMoon):
            if moon.positionVector[0] < otherMoon.positionVector[0]:
                moon.velocityVector[0] += 1
                otherMoon.velocityVector[0] += -1
            elif moon.positionVector[0] > otherMoon.positionVector[0]:
                moon.velocityVector[0] += -1
                otherMoon.velocityVector[0] += 1
            if moon.positionVector[1] < otherMoon.positionVector[1]:
                moon.velocityVector[1] += 1
                otherMoon.velocityVector[1] += -1
            elif moon.positionVector[1] > otherMoon.positionVector[1]:
                moon.velocityVector[1] += -1
                otherMoon.velocityVector[1] += 1
            if moon.positionVector[2] < otherMoon.positionVector[2]:
                moon.velocityVector[2] += 1
                otherMoon.velocityVector[2] += -1
            elif moon.positionVector[2] > otherMoon.positionVector[2]:
                moon.velocityVector[2] += -1
                otherMoon.velocityVector[2] += 1

        gravityBetweenTwoMoons(self.moonObjectList[0], self.moonObjectList[1])
        gravityBetweenTwoMoons(self.moonObjectList[0], self.moonObjectList[2])
        gravityBetweenTwoMoons(self.moonObjectList[0], self.moonObjectList[3])
        gravityBetweenTwoMoons(self.moonObjectList[1], self.moonObjectList[2])
        gravityBetweenTwoMoons(self.moonObjectList[1], self.moonObjectList[3])
        gravityBetweenTwoMoons(self.moonObjectList[2], self.moonObjectList[3])

        #werkt maar is trager
        #moon.velocityVector = [sum(pair) for pair in zip(moon.velocityVector,velocityChange)]

    def applyVelocityEffects(self):
        for moon in self.moonObjectList:
            moon.positionVector[0] += moon.velocityVector[0]
            moon.positionVector[1] += moon.velocityVector[1]
            moon.positionVector[2] += moon.velocityVector[2]

    def currentSimDataPrintOut(self,printInLog=False,OneStringMode=False):
        #set printInLog to True for easy visual check
        if OneStringMode:
            moon0 = f'{self.moonObjectList[0].positionVector}#{self.moonObjectList[0].velocityVector}'
            moon1 = f'{self.moonObjectList[1].positionVector}#{self.moonObjectList[1].velocityVector}'
            moon2 = f'{self.moonObjectList[2].positionVector}#{self.moonObjectList[2].velocityVector}'
            moon3 = f'{self.moonObjectList[3].positionVector}#{self.moonObjectList[3].velocityVector}'
            OneString = f'{moon0}+{moon1}+{moon2}+{moon3}'
            return OneString
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
            pot = abs(moon.positionVector[0])+abs(moon.positionVector[1])+abs(moon.positionVector[2])
            kin = abs(moon.velocityVector[0])+abs(moon.velocityVector[1])+abs(moon.velocityVector[2])
            result += pot*kin
        return result

    def takeStepsTillSimRepeats(self):
        keepGoing = True
        counter = 0
        startX = self.getXorYorZForCurrentStep('X')
        startY = self.getXorYorZForCurrentStep('Y')
        startZ = self.getXorYorZForCurrentStep('Z')
        intervalX = 0
        intervalY = 0
        intervalZ = 0
        intervalXYZ = 0
        while keepGoing:
            counter += 1
            curX = self.getXorYorZForCurrentStep('X')
            curY = self.getXorYorZForCurrentStep('Y')
            curZ = self.getXorYorZForCurrentStep('Z')
            if curX == startX and self.currentTimeStep > 0 and intervalX == 0:
                intervalX = self.currentTimeStep
                print(f'X repeats in {intervalX} with {curX}')
            if curY == startY and self.currentTimeStep > 0 and intervalY == 0:
                intervalY = self.currentTimeStep
                print(f'Y repeats in {intervalY} with {curY}')
            if curZ == startZ and self.currentTimeStep > 0 and intervalZ == 0:
                intervalZ = self.currentTimeStep
                print(f'Z repeats in {intervalZ} with {curZ}')
            multipliedIntervals = intervalX*intervalY*intervalZ
            if multipliedIntervals > 0:
                intervalXYZ = self.lowestCommonMultiplier(intervalX,intervalY,intervalZ)
                print(f'the system repeats every {intervalXYZ} steps')
                keepGoing = False
            if keepGoing:
                self.takeOneTimeStep()
            if counter == 100000:
                currentTime = time.time()
                print(f'{self.currentTimeStep} timegap: {currentTime-self.startTime}')
                self.startTime = currentTime
                counter = 0
        return intervalXYZ

    def lowestCommonMultiplier(self,a,b,c):
        numbers = [a,b,c]
        numbers.sort()
        x = numbers[2]
        y = numbers[1]
        z = numbers[0]
        mul = x
        calculating = True
        while calculating:
            if mul%y == 0 and mul%z == 0:
                calculating = False
            else:
                mul +=x
        return mul



    def getXorYorZForCurrentStep(self,XorYorZ):
        if XorYorZ == 'X':
            i = 0
        if XorYorZ == 'Y':
            i = 1
        if XorYorZ == 'Z':
            i = 2
        stringeling = ''
        for m in range(len(self.moonObjectList)):
            stringeling += str(self.moonObjectList[m].positionVector[i])
        for m in range(len(self.moonObjectList)):
            stringeling += str(self.moonObjectList[m].velocityVector[i])
        return stringeling


def constructMoonListFromPathFast(path):
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
        newMoon = MoonFast(x,y,z)
        moonList.append(newMoon)
        result = moonList
    return result

def constructSimulatorFromPathFast(path):
    moonList = constructMoonListFromPathFast(path)
    sim =SimulatorFast(moonList)
    return sim

