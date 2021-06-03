from ArcadeCabinet import constructArcadeCabinetFromPath

path = 'Inputs/inputDay13'
arcadeCabinet = constructArcadeCabinetFromPath(path)
arcadeCabinet.brain.intcode[0] = 2
arcadeCabinet.startTkinterGame(autoPilot=True)