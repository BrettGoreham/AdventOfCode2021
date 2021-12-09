with open('day9Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

points = []
for line in content:
    points.append([int(x) for x in line])

lows = []

for y in range(len(points)):
    for x in range(len(points[y])):
        point = points[y][x]

        isLow = True
        if y - 1 >= 0:
            above = points[y - 1][x]
            if point >= above:
                isLow = False
        if y + 1 < len(points):
            if point >= points[y+1][x]:
                isLow = False
        if x - 1 >= 0:
            if point >= points[y][x - 1]:
                isLow = False
        if x + 1 < len(points[y]):
            if point >= points[y][x + 1]:
                isLow = False

        if isLow:
            lows.append((y, x))

total = 0
for x in lows:
    total += points[x[0]][x[1]] + 1

print('part 1: ', total)

# start finding Basins
basinSizeList = []
for low in lows:
    toVisitStack = [low]
    visitedList = []

    while len(toVisitStack) > 0:
        visiting = toVisitStack.pop(0)
        neighbours = [(visiting[0] - 1, visiting[1]),
                      (visiting[0] + 1, visiting[1]),
                      (visiting[0], visiting[1] - 1),
                      (visiting[0], visiting[1] + 1)]

        for neighbour in neighbours:
            if 0 <= neighbour[0] < len(points) and 0 <= neighbour[1] < len(points[0]): # check if neighbour is in the list
                if neighbour not in toVisitStack and neighbour not in visitedList: # check if neighbour is already found to be in the basin
                    point = points[neighbour[0]][neighbour[1]]
                    if 9 > point > points[visiting[0]][visiting[1]]:
                        toVisitStack.append(neighbour)

        visitedList.append(visiting)

    basinSizeList.append(len(visitedList))

basinSizeList.sort(reverse=True)

print('part 2: ', basinSizeList[0] * basinSizeList[1] * basinSizeList[2])
