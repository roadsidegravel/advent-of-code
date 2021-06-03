from Intcode import FindMaxThrusterSignalFromPath,FindMaxThrusterFeedbackLoopSignalFromPath
import time

begin  = time.time()
path = 'inputDay7'
testBank = FindMaxThrusterSignalFromPath(path)
result = testBank.highestThrusterSignal
print(f'The highest thruster output is {result} : 17790')
testBankFeedbackLoop = FindMaxThrusterFeedbackLoopSignalFromPath(path)
resultFeedbackLoop = testBankFeedbackLoop.highestThrusterSignal
print(f'The highest thruster output with feedback is {resultFeedbackLoop} : 19384820')

end = time.time()
executiontime = end-begin
print(f'it took {executiontime}')

