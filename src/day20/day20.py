with open('day20Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]


pixelstring = content[0]

lowestX = 20000000
lowestY = 20000000
highestX = 0
highestY = 0
pixels = {}
for y in range(2, len(content)):
    for x in range(len(content[y])):
        if content[y][x] == '#':
            pixels[((y - 2),x)] = '#'
            if x < lowestX:
                lowestX = x
            elif x > highestX:
                highestX = x
            if y - 2 < lowestY:
                lowestY = y - 2
            elif y - 2 > highestY:
                highestY = y - 2

print(pixels)
print(lowestX, highestX)
print(lowestY, highestY)

afterPixels = {}
newLowestX = 200000
newLowestY = 200000
newHighestX = 0
newHighestY = 0

for z in range(50):
    afterPixels = {}

    for y in range(lowestY - 3, highestY + 3):
        for x in range(lowestX - 3, highestX + 3):
            string = ''
            for ys in range(y-1, y+2):
                for xs in range(x-1, x+2):
                    if z % 2 == 1 and content[0][0] == '#' and \
                            (ys < lowestY or ys > highestY or xs < lowestX or xs > highestX):
                        string += '1'
                    elif pixels.get((ys,xs), '') == '#':
                        string += '1'
                    else:
                        string += '0'

            newPx = pixelstring[int(string, 2)]

            if newPx == '#':
                afterPixels[(y, x)] = '#'
                if x < newLowestX:
                    newLowestX = x
                elif x > newHighestX:
                    newHighestX = x
                if y < newLowestY:
                    newLowestY = y
                elif y > newHighestY:
                    newHighestY = y

    lowestX = newLowestX
    lowestY = newLowestY
    highestX = newHighestX
    highestY = newHighestY
    pixels = afterPixels

print(len(afterPixels.keys()))