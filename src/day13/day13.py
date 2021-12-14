with open('day13Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

charToPrint = '█'
points = []
count = 0
highestX = 0
highestY = 0
while content[count] != "":
    x, y = (int(z) for z in content[count].split(','))
    if x > highestX:
        highestX = x
    if y > highestY:
        highestY = y
    points.append((y,x))
    count += 1

grid = []
for y in range(highestY + 1):
    gridRow = []
    for x in range(highestX + 1):
        gridRow.append('.')
    grid.append(gridRow)

for point in points:
    grid[point[0]][point[1]] = charToPrint

firstFold = content[count + 1]

axis, index = firstFold.split(' ')[2].split('=')
index = int(index)
if axis == 'y':
    foldCount = 1
    while foldCount + index < len(grid):
        for x in range(len(grid[0])):
            if grid[foldCount + index][x] == charToPrint:
                grid[index - foldCount][x] = charToPrint
        foldCount += 1

    grid = grid[:index]

if axis == 'x':
    foldCount = 1
    while foldCount + index < len(grid[0]):
        for y in range(len(grid)):
            if grid[y][foldCount + index] == charToPrint:
                grid[y][index - foldCount] = charToPrint
        foldCount += 1

    for i in range(len(grid)):
        grid[i] = grid[i][:index]

p1Count = 0
for row in grid:
    for index in row:
        if index == charToPrint:
            p1Count += 1

print('part 1', p1Count)

count += 2
while count < len(content):
    fold = content[count]
    axis, index = fold.split(' ')[2].split('=')
    index = int(index)
    if axis == 'y':
        foldCount = 1
        while foldCount + index < len(grid):
            for x in range(len(grid[0])):
                if grid[foldCount + index][x] == charToPrint:
                    grid[index - foldCount][x] = charToPrint
            foldCount += 1

        grid = grid[:index]

    if axis == 'x':
        foldCount = 1
        while foldCount + index < len(grid[0]):
            for y in range(len(grid)):
                if grid[y][foldCount + index] == charToPrint:
                    grid[y][index - foldCount] = charToPrint
            foldCount += 1

        for i in range(len(grid)):
            grid[i] = grid[i][:index]

    count+=1

print('part 2 you must find capital letters by sight')
for row in grid:
    line = ""
    for x in row:
        if x == '.':
            line += ' '
        else:
            line += x

    print(line)