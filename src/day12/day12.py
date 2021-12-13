with open('day12Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

fromToMap = {}
for line in content:
    fromPoint, to = line.split('-')
    if fromPoint != 'end' and to != 'start':
        array = fromToMap.get(fromPoint, [])
        array.append(to)
        fromToMap[fromPoint] = array

    if to != 'end' and fromPoint != 'start':
        #bidirectional but dont want to go back from start or end
        toArray = fromToMap.get(to, [])
        toArray.append(fromPoint)
        fromToMap[to] = toArray

pathStarts = []
for cave in fromToMap['start']:
    pathStarts.append([cave])

finishingPaths = []
while len(pathStarts) > 0:
    path = pathStarts.pop(0)
    lastCave = path[len(path) - 1]
    for cave in fromToMap[lastCave]:
        copiedPath = path.copy()
        if cave == 'end':
            copiedPath = path.copy()
            copiedPath.append(cave)
            finishingPaths.append(copiedPath)
        elif cave.islower():
            if cave not in copiedPath:
                copiedPath.append(cave)
                pathStarts.append(copiedPath)
        else:
            copiedPath.append(cave)
            pathStarts.append(copiedPath)

print(len(finishingPaths))

#part2 start
pathStarts = []
for cave in fromToMap['start']:
    pathStarts.append(([cave], False)) #same array as first go but a boolean to tell if weve visited a small cave twice

finishingPaths = []

while len(pathStarts) > 0:
    path = pathStarts.pop(0)
    lastCave = path[0][len(path[0]) - 1]
    for cave in fromToMap[lastCave]:
        copiedPath = path[0].copy()
        if cave == 'end':
            copiedPath.append(cave)
            finishingPaths.append((copiedPath, path[1]))
        elif cave.islower():
            if cave not in copiedPath or path[1] is False:
                boolean = path[1]
                if cave in copiedPath:
                    boolean = True
                copiedPath.append(cave)
                pathStarts.append((copiedPath, boolean))
        else:
            copiedPath.append(cave)
            pathStarts.append((copiedPath, path[1]))

print(len(finishingPaths))
