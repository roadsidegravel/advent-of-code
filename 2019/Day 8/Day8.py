from SpaceImagingFormat import constructSIFLayersFromFile, constructDecodedSIFFromFile
import time

begin  = time.time()
pathDay8 = 'inputDay8'
length = 25
height = 6
SIFDay8 = constructSIFLayersFromFile(pathDay8,length,height)
print(f'The number of 1 digits multiplied by the number of 2 digits is {SIFDay8.returnOnFewestZeroesLayerMultiplyOneCountByTwoCount()} :  2806')
image = constructDecodedSIFFromFile(pathDay8,length,height)
print(f'The image looks like this:\n{image}')
print(f'(it should look like it says ZBJAB)')
end = time.time()
executiontime = end-begin
print(f'it took {executiontime}')