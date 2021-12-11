with open('day11Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

octopuses = []
for line in content:
    octopuses.append([int(x) for x in line])

vectors = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, -1), (-1, 1), (-1, -1), (1, 1)]
totalFlashesBefore100 = 0
stepAllFlash = -1
step = 0
while stepAllFlash < 0 or step < 100:
    toFlash = []
    flashed = []
    for y in range(len(octopuses)):
        for x in range(len(octopuses)):
            octopuses[y][x] += 1
            if octopuses[y][x] > 9:
                toFlash.append((y, x))

    while len(toFlash) > 0:
        flasher: tuple[int, int] = toFlash.pop(0)
        for vector in vectors:
            yCoord = flasher[0] + vector[0]
            xCoord = flasher[1] + vector[1]
            if 0 <= yCoord < 10 and 0 <= xCoord < 10:
                if (yCoord, xCoord) not in toFlash and (yCoord, xCoord) not in flashed:
                    octopuses[yCoord][xCoord] += 1
                    if octopuses[yCoord][xCoord] > 9:
                        toFlash.append((yCoord, xCoord))

        flashed.append(flasher)

    for y in range(len(octopuses)):
        for x in range(len(octopuses)):
            if octopuses[y][x] > 9:
                octopuses[y][x] = 0

    if step < 100:
        totalFlashesBefore100 += len(flashed)
    if len(flashed) == 100:
        stepAllFlash = step + 1
    step += 1

print('part 1:', totalFlashesBefore100)
print('part 2:', stepAllFlash)
