class FlawedFrequencyTransmission:
    def __init__(self,path):
        rawData = []
        with open(path) as file:
            rawData = file.readlines()
        self.startSignal = rawData[0]
        self.basePattern = (0,1,0,-1)
        self.currentSignal = self.startSignal
    
    def applyPhaseOnCurrentSignal(self):
        curSignal = self.currentSignal
        patternLength = len(self.basePattern)
        pattern = self.basePattern
        newSignal = ''
        signalDict = {i:curSignal[i] for i in range(0,len(curSignal))}
        newSignalDict = signalDict.copy()
        for d in range(0,len(signalDict)):
            position = d+1
            posValuesDict = {}
            negValuesDict = {}
            for k in signalDict.keys():
                multiplierIndex = (k+1)//position%patternLength
                if multiplierIndex == 1:
                    posValuesDict[k] = int(signalDict[k])
                if multiplierIndex == 3:
                    negValuesDict[k] = int(signalDict[k])
            posValueSum = sum(posValuesDict.values())
            negValueSum = sum(negValuesDict.values())
            valueSum = posValueSum-negValueSum
            lastDigit = str(valueSum)[-1]
            newSignalDict[d]= str(lastDigit)
        """
        for d in range(0,len(signalDict)):
            position = d+1
            newValue = 0
            multiplierIndex = 0
            for p in range(0,len(signalDict)):
                value = int(signalDict[p])
                multiplierIndex = (p+1)//position%patternLength
                if multiplierIndex is 1 or multiplierIndex is 3:
                    multiplier = pattern[multiplierIndex]
                    #print(value,multiplier)
                    newValue += value*multiplier
            #print('----')
            lastDigit = str(newValue)[-1]
            newSignalDict[d]= str(lastDigit)
        """
        """
        for i in range(0,len(curSignal)):
            position = i+1
            newValue = 0
            multiplierIndex = 0
            for p in range(0,len(curSignal)):
                value = int(curSignal[p])
                multiplierIndex = (p+1)//position%patternLength
                multiplier = pattern[multiplierIndex]
                #print(value,multiplier)
                newValue += value*multiplier
            #print('----')
            lastDigit = str(newValue)[-1]
            newSignal += str(lastDigit)
        """
        newSignal = ''.join(newSignalDict.values())
        self.currentSignal = newSignal
        
    def applySeveralPhasesOnCurrentSignal(self,amount):
        for i in range(0,amount):
            self.applyPhaseOnCurrentSignal()
        return self.returnFirstEightDigitsCurrentSignal()
            
    def returnFirstEightDigitsCurrentSignal(self):
        result = self.currentSignal[0:8]
        return result
        
        