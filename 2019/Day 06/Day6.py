from UniversalOrbitMap import ConstructOrbitMapFromDataFile
import time

begin  = time.time()
pathDay6 = 'inputDay6'
OrbitMapDay6 = ConstructOrbitMapFromDataFile(pathDay6)
print(f'{OrbitMapDay6.totalNumberOfOrbits} :  621125')
numberOfTransferOrbits = OrbitMapDay6.CalculateOrbitsBetweenTwoNames('YOU','SAN')
print(f'{numberOfTransferOrbits} : 550')
end = time.time()
executiontime = end-begin
print(f'it took {executiontime}')
