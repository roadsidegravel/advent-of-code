from MoonMovementSimulator import constructSimulatorFromPath

path = 'input'
sim = constructSimulatorFromPath(path)
sim.skipToTimeStep(1000)
totalEnergy = sim.calculateCurrentTotalEnergy()
print(f'Day 12 part 1: the total energy after 1000 steps is {totalEnergy} (14907)')