from MoonMovementSimulatorFast import constructSimulatorFromPathFast

path = 'input'
sim = constructSimulatorFromPathFast(path)
sim.skipToTimeStep(1000)
totalEnergy = sim.calculateCurrentTotalEnergy()
print(f'Day 12 part 1: the total energy after 1000 steps is {totalEnergy} (14907)')
simInterval = constructSimulatorFromPathFast(path)
interval = simInterval.takeStepsTillSimRepeats()
print(f'Day 12 part 2: it takes {interval} steps till the sim repeats (467081194429464)')