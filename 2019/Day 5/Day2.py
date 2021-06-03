from Intcode import computer
path = 'inputDay2'
rawData = []
with open(path) as file:
    rawData = file.readlines()

rawIntcode = rawData[0].split(',')
intcode = []
for i in range(0,len(rawIntcode)):
    intcode.append(int(rawIntcode[i]))
day2computer = computer(intcode)
day2computer.intcode[1] = 12
day2computer.intcode[2] = 2
day2computer.run()
print(f'After running the program, the value at position 0 is: {day2computer.intcode[0]} (3716293)')

#part2
for noun in range(0,100):
    for verb in range(0,100):
        day2part2computer = computer(intcode)
        day2part2computer.intcode[1] = noun
        day2part2computer.intcode[2] = verb
        day2part2computer.run()
        #print(f'reached {noun} and {verb}: {day2part2computer.intcode[0]}')
        if day2part2computer.intcode[0] == 19690720:
            print(f'Part2, the answer is: {(noun*100)+verb} (6429)')

