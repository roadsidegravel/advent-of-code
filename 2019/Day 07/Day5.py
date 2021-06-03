from Intcode import computer
path = 'inputDay5'
rawData = []
with open(path) as file:
    rawData = file.readlines()

rawIntcode = rawData[0].split(',')
intcode = []
for i in range(0,len(rawIntcode)):
    intcode.append(int(rawIntcode[i]))
day5computer = computer(intcode)
day5computer.inputs.append(1)
day5computer.run()
print(f'After running the program, the last output is is: {day5computer.outputs[-1]} (12428642)')
day5part2computer = computer(intcode)
day5part2computer.inputs.append(5)
day5part2computer.run()
print(f'The diagnostic code for system ID 5 is: {day5part2computer.outputs[-1]} (918655)')

#part2
