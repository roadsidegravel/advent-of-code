class computer:
    def __init__(self,intcode):
        self.intcode = []
        self.running = False
        self.position = 0
        for i in range(0,len(intcode)):
            self.intcode.append(intcode[i])
    #https://stackoverflow.com/questions/15189245/assigning-class-variable-as-default-value-to-class-method-argument
    def takeStep(self, position = None):
        if position is None:
            position = self.position
        #bounds limit check
        if position < 0:
            return self.exitMessage(f'position too low, {position}')
        if position > len(self.intcode)-1:
            return self.exitMessage(f'position too high, {position}')
        #opcode
        opcode = self.intcode[position]
        if opcode is 1:
            return self.opcode1(position)
        elif opcode is 2:
            return self.opcode2(position)
        elif opcode is 99:
            return self.exitMessage('opcode 99')
        else:
            return self.exitMessage(f'Uknown opcode encountered, {opcode} at position {position}')

    def exitMessage(self,string):
        self.running = False
        result = string+', exiting'
        return result

    def opcode1(self,position):
        posA = self.intcode[position+1]
        posB = self.intcode[position+2]
        posResult = self.intcode[position+3]
        self.intcode[posResult] = self.intcode[posA]+self.intcode[posB]
        self.position += 4
        return f'opcode 1 at position {position} processed'
    def opcode2(self,position):
        posA = self.intcode[position+1]
        posB = self.intcode[position+2]
        posResult = self.intcode[position+3]
        self.intcode[posResult] = self.intcode[posA]*self.intcode[posB]
        self.position += 4
        return f'opcode 2 at position {position} processed'

    def run(self, position = None):
        if position is None:
            position = self.position
        self.running = True
        while self.running:
            self.takeStep()
