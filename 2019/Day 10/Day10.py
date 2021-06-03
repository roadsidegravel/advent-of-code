from AsteroidBelt import constructAsteroidMapFromFile
path = 'inputDay10'
asteroidMap = constructAsteroidMapFromFile(path)
bestPosition = asteroidMap.bestPosition
bestVisibleCount = asteroidMap.bestPositionSeesCount
print(f'Day 10, part 1: {bestPosition} is the best position, it sees {bestVisibleCount} asteroids')
asteroid200Name = asteroidMap.laserOrderNamesFromBestPosition[200]
asteroid200X = asteroidMap.takeXFromAsteroidString(asteroid200Name)
asteroid200Y = asteroidMap.takeYFromAsteroidString(asteroid200Name)
betWinnerString = str(asteroid200X*100+asteroid200Y)
print(f'Day 10, part 2: the 200th asteroid is {asteroid200Name}, string is: {betWinnerString}')