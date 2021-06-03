class computer:
    def __init__(self,intcode,automaticMode = False):
        self.automaticMode = automaticMode
        self.intcode = []
        self.running = False
        self.position = 0
        self.inputs = []
        self.outputs = []
        self.log = []
        for i in range(0,len(intcode)):
            self.intcode.append(intcode[i])
    #https://stackoverflow.com/questions/15189245/assigning-class-variable-as-default-value-to-class-method-argument

    class modes:
         def __init__(self, A,B,C):
            self.modeFirstParam = C
            self.modeSecondParam = B
            self.modeThirdParam = A

    class parametersClass:
        def __init__(self,oneIntcode):
            self.A = 0 #third parameter
            self.B = 0 #second parameter
            self.C = 0 #first parameter
            self.D = 0 #opcode first digit
            self.E = 0 #opcode second digit
            arrayParam = self.buildParamArray(str(oneIntcode))
            self.A = self.checkZeroOrOne(arrayParam[0], 'Parameter A')
            self.B = self.checkZeroOrOne(arrayParam[1], 'Parameter B')
            self.C = self.checkZeroOrOne(arrayParam[2], 'Parameter C')
            self.D = arrayParam[3]
            self.E = arrayParam[4]

        def buildParamArray(self,intcodeString):
            result = [0,0,0,0,0]
            for i in range(1, len(intcodeString) + 1):
                result[-i] = int(intcodeString[-i])
            return result.copy()

        def checkZeroOrOne(self,value,valueNameForErrorMessage):
            if value == 0 or value == 1:
                return value
            else:
                raise ValueError(f'{valueNameForErrorMessage} should be 1 or 0, not {value}')

        def returnModes(self):
            result = computer.modes(self.A,self.B,self.C)
            return result

    def run(self):
        self.running = True
        while self.running:
            self.log.append(self.takeStep())

    def takeStep(self, position = None):
        if position is None:
            position = self.position
        #bounds limit check
        if position < 0:
            return self.exitMessage(f'position too low, {position}')
        if position > len(self.intcode)-1:
            return self.exitMessage(f'position too high, {position}')
        currentParameters = self.parametersClass(self.intcode[position])
        currentModes = currentParameters.returnModes()
        opcode = int(currentParameters.D*10+currentParameters.E)
        if opcode is 1:
            return self.opcode1(position,currentModes)
        elif opcode is 2:
            return self.opcode2(position,currentModes)
        elif opcode is 3:
            return self.opcode3(position,currentModes)
        elif opcode is 4:
            return self.opcode4(position,currentModes)
        elif opcode is 5:
            return self.opcode5(position,currentModes)
        elif opcode is 6:
            return self.opcode6(position,currentModes)
        elif opcode is 7:
            return self.opcode7(position,currentModes)
        elif opcode is 8:
            return self.opcode8(position,currentModes)
        elif opcode is 99:
            return self.exitMessage('opcode 99')
        else:
            print(f'unknown opcode {opcode} encountered at position {position}')
            return self.exitMessage(f'Uknown opcode encountered, {opcode} at position {position}')

    def exitMessage(self,string):
        self.running = False
        result = string+', exiting'
        return result

    def getValueFromIntcodes(self,position,param):
        if param == 0:
            actualPosition = self.intcode[position]
            result = self.intcode[actualPosition]
        elif param == 1:
            result = self.intcode[position]
        else:
            raise ValueError('parameter should be 0 or 1 and this should be caught earlier')
        return result

    def writeResultToIntcodes(self,position,param,result):
        if param == 0:
            actualPosition = self.intcode[position]
            self.intcode[actualPosition] = result
        elif param == 1:
            raise ValueError('Parameters that an instruction writes to will never be in immediate mode.')
        else:
            raise ValueError('parameter should be 0 or 1 and this should be caught earlier')

    def retrieveFirst(self,position, modes):
        return self.getValueFromIntcodes(position + 1, modes.modeFirstParam)
    def retrieveSecond(self,position, modes):
        return self.getValueFromIntcodes(position + 2, modes.modeSecondParam)
    def retrieveFirstAndSecond(self,position,modes):
        first = self.retrieveFirst(position,modes)
        second = self.retrieveSecond(position,modes)
        return first, second
    def writeToFirst(self,position, modes, result):
        self.writeResultToIntcodes(position+1,modes.modeFirstParam,result)
    def writeToThird(self,position, modes,result):
        self.writeResultToIntcodes(position + 3, modes.modeThirdParam, result)

    def opcode1(self,position,modes):
        #adds
        first, second = self.retrieveFirstAndSecond(position,modes)
        result = first+second
        self.writeToThird(position,modes,result)
        self.position += 4
        return f'opcode 1 at position {position} processed'

    def opcode2(self,position,modes):
        #multiplies
        first, second = self.retrieveFirstAndSecond(position,modes)
        result = first * second
        self.writeToThird(position,modes,result)
        self.position += 4
        return f'opcode 2 at position {position} processed'

    def opcode3(self,position,modes):
        if len(self.inputs) > 0:
            inputReceived = self.inputs[0]
            self.inputs = self.inputs[1:]
        else:
            if self.automaticMode:
                # wait for input
                self.running = False
                return f'pausing for input at position {position}'
            else:
                inputReceived = input('Enter an integer: ')
        try:
            intInputReceived = int(inputReceived)
        except:
            raise ValueError('I said, an integer.')
        self.writeToFirst(position, modes, intInputReceived)
        self.position += 2
        return f'opcode 3 at position {position} processed'

    def automaticModeTakeInputAndUnpauze(self,singleInput):
        self.inputs.append(singleInput)
        self.running = True
        self.run()

    def opcode4(self,position,modes):
        #output
        result = self.retrieveFirst(position,modes)
        if not self.automaticMode:
            print(result)
        self.outputs.append(result)
        self.position +=2
        return f'opcode 4 at position {position} processed'

    def opcode5(self, position, modes):
        #jump if true
        ZeroOrOther = self.retrieveFirst(position,modes)
        if ZeroOrOther == 0:
            self.position += 3
        else:
            distance = self.retrieveSecond(position,modes)
            self.position = distance
        return f'opcode 5 at position {position} processed'

    def opcode6(self, position, modes):
        #jump if false
        ZeroOrOther = self.retrieveFirst(position,modes)
        if ZeroOrOther == 0:
            distance = self.retrieveSecond(position, modes)
            self.position = distance
        else:
            self.position += 3
        return f'opcode 6 at position {position} processed'

    def opcode7(self,position, modes):
        #less than
        first, second = self.retrieveFirstAndSecond(position,modes)
        if first < second:
            result = 1
        else:
            result = 0
        self.writeToThird(position,modes,result)
        self.position +=4
        return f'opcode 7 at position {position} processed'

    def opcode8(self,position, modes):
        #equals
        first, second = self.retrieveFirstAndSecond(position,modes)
        if first == second:
            result = 1
        else:
            result = 0
        self.writeToThird(position,modes,result)
        self.position +=4
        return f'opcode 8 at position {position} processed'

class amplifier:
    def __init__(self,intcode,phaseSetting):
        automaticMode = True
        self.computer = computer(intcode,automaticMode)
        self.takeInput(phaseSetting)

    def takeInput(self,value):
        self.computer.automaticModeTakeInputAndUnpauze(value)

    def takeOutput(self):
        return self.computer.outputs[-1]

class amplifiersInSeries:
    def __init__(self,intcode,phaseSettings):
        stringPhaseSettings = str(phaseSettings)
        self.ampList = []
        for i in range(0,len(stringPhaseSettings)):
            self.ampList.append(amplifier(intcode,stringPhaseSettings[i]))
        self.ampList[0].takeInput(0)
        for i in range(1,len(stringPhaseSettings)):
            self.ampList[i].takeInput(self.ampList[i-1].takeOutput())

    def giveFinalOutput(self):
        return self.ampList[-1].takeOutput()


def constructAmplifiersInSeriesFromFile(path,phaseSettings):
    rawData = []
    with open(path) as file:
        rawData = file.readlines()
    splitData = rawData[0].split(',')
    cleanedData = [int(i) for i in splitData]
    return amplifiersInSeries(cleanedData,phaseSettings)

class FindMaxThrusterSignalFromPath:
    def __init__(self,path):
        self.path = path
        self.amplifierSettingsList = self.returnListOfValidPhaseSettings()
        self.highestThrusterSignal = 0
        self.findHighestThrusterSignal()

    def returnListOfValidPhaseSettings(self):
        result = []
        numbers = ['0','1','2','3','4']
        for i in range(0,len(numbers)):
            first= numbers[i]
            iRemoved = list(numbers)
            iRemoved.remove(numbers[i])
            for j in range(0,len(iRemoved)):
                second = iRemoved[j]
                ijRemoved = list(iRemoved)
                ijRemoved.remove(iRemoved[j])
                for k in range(0,len(ijRemoved)):
                    third = ijRemoved[k]
                    ijkRemoved = list(ijRemoved)
                    ijkRemoved.remove(ijRemoved[k])
                    for l in range(0,len(ijkRemoved)):
                        fourth = ijkRemoved[l]
                        ijklRemoved = list(ijkRemoved)
                        ijklRemoved.remove(ijkRemoved[l])
                        for m in range(0,len(ijklRemoved)):
                            fifth = ijklRemoved[m]
                            result.append(first+second+third+fourth+fifth)
        return result

    def findHighestThrusterSignal(self):
        for ampSetting in self.amplifierSettingsList:
            ampBank = constructAmplifiersInSeriesFromFile(self.path,ampSetting)
            result = ampBank.giveFinalOutput()
            if result > self.highestThrusterSignal:
                self.highestThrusterSignal = result

class amplifiersInSeriesWithFeedbackLoop:
    def __init__(self,intcode,phaseSettings):
        stringPhaseSettings = str(phaseSettings)
        self.ampList = []
        for i in range(0,len(stringPhaseSettings)):
            self.ampList.append(amplifier(intcode,stringPhaseSettings[i]))
        self.goThroughAmpList(0)

    def goThroughAmpList(self,firstInput):
        self.ampList[0].takeInput(firstInput)
        for i in range(1,len(self.ampList)):
            self.ampList[i].takeInput(self.ampList[i-1].takeOutput())
        lastLog = self.ampList[-1].computer.log[-1]
        if lastLog != 'opcode 99, exiting':
            self.goThroughAmpList(self.ampList[-1].takeOutput())

    def giveFinalOutput(self):
        return self.ampList[-1].takeOutput()

def constructAmplifiersInSeriesWithFeedbackLoopFromFile(path,phaseSettings):
    rawData = []
    with open(path) as file:
        rawData = file.readlines()
    splitData = rawData[0].split(',')
    cleanedData = [int(i) for i in splitData]
    return amplifiersInSeriesWithFeedbackLoop(cleanedData,phaseSettings)

class FindMaxThrusterFeedbackLoopSignalFromPath:
    def __init__(self,path):
        self.path = path
        self.amplifierSettingsList = self.returnListOfValidPhaseSettings()
        self.highestThrusterSignal = 0
        self.findHighestThrusterSignal()

    def returnListOfValidPhaseSettings(self):
        result = []
        numbers = ['5','6','7','8','9']
        for i in range(0,len(numbers)):
            first= numbers[i]
            iRemoved = list(numbers)
            iRemoved.remove(numbers[i])
            for j in range(0,len(iRemoved)):
                second = iRemoved[j]
                ijRemoved = list(iRemoved)
                ijRemoved.remove(iRemoved[j])
                for k in range(0,len(ijRemoved)):
                    third = ijRemoved[k]
                    ijkRemoved = list(ijRemoved)
                    ijkRemoved.remove(ijRemoved[k])
                    for l in range(0,len(ijkRemoved)):
                        fourth = ijkRemoved[l]
                        ijklRemoved = list(ijkRemoved)
                        ijklRemoved.remove(ijkRemoved[l])
                        for m in range(0,len(ijklRemoved)):
                            fifth = ijklRemoved[m]
                            result.append(first+second+third+fourth+fifth)
        return result

    def findHighestThrusterSignal(self):
        for ampSetting in self.amplifierSettingsList:
            ampBank = constructAmplifiersInSeriesWithFeedbackLoopFromFile(self.path,ampSetting)
            result = ampBank.giveFinalOutput()
            if result > self.highestThrusterSignal:
                self.highestThrusterSignal = result



