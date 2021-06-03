from Intcode import constructComputerFromFile,FindMaxThrusterSignalFromPath,FindMaxThrusterFeedbackLoopSignalFromPath
from unittest.mock import patch
import time
begin  = time.time()

pathInput2 = 'Inputs/inputDay2'
day2computer = constructComputerFromFile(pathInput2)
day2computer.intcode[1] = 12
day2computer.intcode[2] = 2
day2computer.run()
print(f'Day 2, part 1: After running the program, the value at position 0 is: {day2computer.intcode[0]} (3716293)')
for noun in range(0,100):
    for verb in range(0,100):
        day2part2computer = constructComputerFromFile(pathInput2)
        day2part2computer.intcode[1] = noun
        day2part2computer.intcode[2] = verb
        day2part2computer.run()
        #print(f'reached {noun} and {verb}: {day2part2computer.intcode[0]}')
        if day2part2computer.intcode[0] == 19690720:
            print(f'Day 2, part 2: The answer is: {(noun*100)+verb} (6429)')

pathInput5 = 'Inputs/inputDay5'
day5computer = constructComputerFromFile(pathInput5)
day5computer.inputs.append(1)
with patch('builtins.print') as p:
    day5computer.run()
print(f'Day 5, part 1: After running the program, the last output is is: {day5computer.outputs[-1]} (12428642)')
day5part2computer = constructComputerFromFile(pathInput5)
day5part2computer.inputs.append(5)
with patch('builtins.print') as p:
    day5part2computer.run()
print(f'Day 5, part 2: The diagnostic code for system ID 5 is: {day5part2computer.outputs[-1]} (918655)')

pathInput7 = 'Inputs/inputDay7'
testBank = FindMaxThrusterSignalFromPath(pathInput7)
resultBank = testBank.highestThrusterSignal
print(f'Day 7, part 1: The highest thruster output is: {resultBank} (17790)')
testBankFeedbackLoop = FindMaxThrusterFeedbackLoopSignalFromPath(pathInput7)
resultFeedbackLoop = testBankFeedbackLoop.highestThrusterSignal
print(f'Day 7, part 2: The highest thruster output with feedback is: {resultFeedbackLoop} (19384820)')

pathInput9 = 'Inputs/inputDay9'
day9computer = constructComputerFromFile(pathInput9)
day9computer.inputs.append(1)
with patch('builtins.print') as p:
    day9computer.run()
print(f'Day 9, part 1: The BOOST keycode is: {day9computer.outputs[0]} (3380552333)')
day9part2computer = constructComputerFromFile(pathInput9)
day9part2computer.inputs.append(2)
with patch('builtins.print') as p:
    day9part2computer.run()
print(f'Day 9, part 2: The coordinates for the Ceres monitoring station are: {day9part2computer.outputs[0]} (78831)')

end = time.time()
executiontime = end-begin
print(f'it took {executiontime}')


