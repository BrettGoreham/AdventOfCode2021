with open('day5Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

coordMap = {}
diagonalMap = {}  # used to keep part 1 and two in one loop

for line in content:
    parts = line.split(' -> ')
    first = [int(x) for x in parts[0].split(",")]
    second = [int(x) for x in parts[1].split(",")]
    run = 0
    rise = 0
    if first[0] != second[0]:  # vertical line
        run = 1 if second[0] - first[0] > 0 else - 1

    if first[1] != second[1]:
        rise = 1 if second[1] - first[1] > 0 else - 1

    while first[0] != second[0] or first[1] != second[1]:
        if rise == 0 or run == 0:
            coordMap[(first[0], first[1])] = coordMap.get((first[0], first[1]), 0) + 1
        else:
            diagonalMap[(first[0], first[1])] = diagonalMap.get((first[0], first[1]), 0) + 1
        first[0] += run
        first[1] += rise

    if rise == 0 or run == 0:
        coordMap[(second[0], second[1])] = coordMap.get((second[0], second[1]), 0) + 1
    else:
        diagonalMap[(second[0], second[1])] = diagonalMap.get((second[0], second[1]), 0) + 1

part1Count = 0
for key in coordMap.keys():
    if coordMap[key] >= 2:
        part1Count += 1

print('part 1:', part1Count)


part2Count = 0
for key in set.union(set(diagonalMap.keys()), set(coordMap.keys())):
    if coordMap.get(key, 0) + diagonalMap.get(key, 0) >= 2:
        part2Count += 1

print('part 2:', part2Count)
