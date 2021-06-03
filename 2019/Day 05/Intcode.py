class computer:
    def __init__(self,intcode):
        self.intcode = []
        self.running = False
        self.position = 0
        self.inputs = []
        self.outputs = []
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
        self.log = []
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
        #input
        if len(self.inputs) > 0:
            inputReceived = self.inputs[0]
            self.inputs = self.inputs[1:]
        else:
            inputReceived = input('Enter an integer: ')
        try:
            intInputReceived = int(inputReceived)
        except:
            raise ValueError('I said, an integer.')
        self.writeToFirst(position,modes,intInputReceived)
        self.position += 2
        return f'opcode 3 at position {position} processed'

    def opcode4(self,position,modes):
        #output
        result = self.retrieveFirst(position,modes)
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
