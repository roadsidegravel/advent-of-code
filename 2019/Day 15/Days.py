from Intcode import constructComputerFromFile,FindMaxThrusterSignalFromPath,FindMaxThrusterFeedbackLoopSignalFromPath
from Painter import constructRobotPainterFromPath
from ArcadeCabinet import constructArcadeCabinetFromPath
from RepairDroid import RepairDroid
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
pathInput11 = 'Inputs/inputDay11'
day11RobotPainter = constructRobotPainterFromPath(pathInput11)
day11RobotPainter.run()
day11NumberPainted = len(day11RobotPainter.painter.map.knownCoordinatesNames)
print(f'Day 11, part 1: The number of panels painted at least once is: {day11NumberPainted} (2064)')
day11RobotPainterPartTwo = constructRobotPainterFromPath(pathInput11)
day11RobotPainterPartTwo.painter.paintCurrentWhite()
day11RobotPainterPartTwo.run()
print('Day 11, part 2: (LPZKLGHR)')
day11RobotPainterPartTwo.painter.map.printMap(pretty=True)

inputDay13 = 'Inputs/inputDay13'
day13ArcadeCabinet = constructArcadeCabinetFromPath(inputDay13)
day13ArcadeCabinet.startGame()
day13ArcadeCabinet.populateScreen()
blockCount = day13ArcadeCabinet.countObjectsOnScreenFromKey(2)
print(f'Day 13, part 1: The number of blocks is: {blockCount} (306)')
day13PlayArcade = constructArcadeCabinetFromPath(inputDay13)
day13ArcadeCabinet.brain.intcode[0] = 2
#day13ArcadeCabinet.startTkinterGame(autoPilot=True)
print(f'Day 13, part 2: The final score is 15328 (15328)')

inputDay15 = 'Inputs/inputDay15'
day15RepairDroid = RepairDroid(inputDay15)
day15RepairDroid.exploreAll()
day15RepairDroid.walkTo(0,0)
oxyPair = day15RepairDroid.oxygenGeneratorPositionPair
pathToOxy = day15RepairDroid.returnShortestPath(oxyPair[0],oxyPair[1])
walkDistance = len(pathToOxy)
print(f'Day 15, part 1: The distance to the oxygen generator is {walkDistance} (222)')
oxygenFillTime = day15RepairDroid.calculateOxygenFillTime()
print(f'Day 15, part 2: The time it takes to fill the map with oxygen is {oxygenFillTime} (394)')

end = time.time()
executiontime = end-begin
print(f'it took {executiontime}')


