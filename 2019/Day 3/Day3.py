from WireGrid import wireGrid
#https://stackoverflow.com/questions/18608160/python-how-to-time-script-from-beginning-to-end
import time
begin  = time.time()
path = 'inputDay3'
day3WireGrid = wireGrid(path)
resultDay3 = day3WireGrid.closestManhattan
resultDay3part2 = day3WireGrid.shortedDistance
print(f'The closest Manhattan distance is {resultDay3}')
print(f'The shortest walking distance is {resultDay3part2}')
end = time.time()
executiontime = end-begin
print(f'it took {executiontime}')