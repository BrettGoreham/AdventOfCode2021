import math
with open('day7Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

crabs = [int(x) for x in content[0].split(',')]
crabs.sort()

total = 0
for crab in crabs:
    total += crab

print('median', crabs[int(len(crabs)/2)])
print('mean', math.floor(total / len(crabs)))

bestLocationPart1 = 0
bestFuelPart1 = float('inf')
bestLocationPart2 = 0
bestFuelPart2 = float('inf')
for x in range(crabs[0], crabs[len(crabs)-1]):
    disPart1 = 0
    disPart2 = 0
    for crab in crabs:
        between = abs(x - crab)
        disPart1 += between
        disPart2 += (between * (between + 1) // 2)

    if bestFuelPart1 > disPart1:
        bestFuelPart1 = disPart1
        bestLocationPart1 = x
    if bestFuelPart2 > disPart2:
        bestFuelPart2 = disPart2
        bestLocationPart2 = x

print('part 1, best location : ' + str(bestLocationPart1) + ', fuel used: ' + str(bestFuelPart1))
print('part 2, best location : ' + str(bestLocationPart2) + ', fuel used: ' + str(bestFuelPart2))
