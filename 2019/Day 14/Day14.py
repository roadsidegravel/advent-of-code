from Nanofactory import Nanofactory,CargoHoldToFuel

path = 'InputDay14'
nanofactory = Nanofactory(path)
cost1FUEL = nanofactory.costToProduce('1 FUEL')
print(f'Day 14 part 1: It costs {cost1FUEL} ORE to produce 1 FUEL (1037742)')
cargohold = CargoHoldToFuel(nanofactory)
fuel = cargohold.fuel
print(f'Day 14 part 2: With one trillion you can produce {fuel} FUEL (1572358)')