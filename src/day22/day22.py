import math
with open('day22Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]


part1Set = set()
absMinX = 0
absMaxX = 0
absMinY = 0
absMaxY = 0
absMinZ = 0
absMaxZ = 0


for i, line in enumerate(content):
    print(i)
    onOff, coordinates = line.split(' ')
    xcoord, ycoord, zcoord = coordinates = coordinates.split(',')

    xmin, xmax = [int(i) for i in xcoord[2:].split('..')]
    ymin, ymax = [int(i) for i in ycoord[2:].split('..')]
    zmin, zmax = [int(i) for i in zcoord[2:].split('..')]

    absMinX = min(xmin, absMinX)
    absMaxX = max(xmax, absMaxX)
    absMinY = min(ymin, absMinY)
    absMaxY = max(ymax, absMaxY)
    absMinZ = min(zmin, absMinZ)
    absMaxZ = max(zmax, absMaxZ)

    for x in range(max(xmin, -50), min(xmax + 1, 51)):
        if x < -50 or x > 50:
            continue
        for y in range(max(ymin, -50), min(ymax + 1, 51)):
            if y < -50 or y > 50:
                continue
            for z in range(max(zmin, -50), min(zmax + 1, 51)):
                if z < -50 or z > 50:
                    continue
                if onOff == 'on':
                    part1Set.add((x, y, z))
                else:
                    part1Set.discard((x, y, z))

print(len(part1Set))

class Cube:

    def __init__(self, id, xMax, xMin, yMax, yMin, zMax, zMin):
        self.id = id
        self.xMax = xMax
        self.xMin = xMin
        self.yMax = yMax
        self.yMin = yMin
        self.zMax = zMax
        self.zMin = zMin
        self.intersectedOn = set()

    def intersects_with(self, cube2):
        if self.xMax >= cube2.xMin:
            if self.xMin <= cube2.xMax:
                if self.yMax >= cube2.yMin:
                    if self.yMin <= cube2.yMax:
                        if self.zMax >= cube2.zMin:
                            if self.zMin <= cube2.zMax:
                                return True

        return False

    def pretty_print(self):
        print('x:' + str(self.xMin) + ' -> ' + str(self.xMax) + ' y:' + str(self.yMin) + ' -> ' + str(self.yMax) + ' z:' + str(self.zMin) + ' -> ' + str(self.zMax))

    def ignore_intersection(self, cube):
        intersection = Cube(-1,
             min(self.xMax, cube.xMax),
             max(self.xMin, cube.xMin),
             min(self.yMax, cube.yMax),
             max(self.yMin, cube.yMin),
             min(self.zMax, cube.zMax),
             max(self.zMin, cube.zMin)
             )
        for c in self.intersectedOn:
            if c.intersects_with(intersection):
                c.ignore_intersection(intersection)

        self.intersectedOn.add(intersection)

    def get_remaining_area(self):
        area = ((self.xMax + 1 - self.xMin) * (self.yMax + 1 - self.yMin) * (self.zMax + 1 - self.zMin))
        for _cube in self.intersectedOn:
            area -= _cube.get_remaining_area()
        return max(area, 0)


cubes = []

part2count = 0

for i, line in enumerate(content):
    print(i)
    onOff, coordinates = line.split(' ')
    xcoord, ycoord, zcoord = coordinates = coordinates.split(',')

    xmin, xmax = [int(i) for i in xcoord[2:].split('..')]
    ymin, ymax = [int(i) for i in ycoord[2:].split('..')]
    zmin, zmax = [int(i) for i in zcoord[2:].split('..')]

    newCube = Cube(i, xmax, xmin, ymax, ymin, zmax, zmin)
    for cube in cubes:
        #print('cube ' + str(i) + ' intersects with cube ' + str(cube.id))
        if newCube.intersects_with(cube):
            cube.ignore_intersection(newCube)

    if onOff == 'on':
        print('cube' + str(i) + 'remaining area' + str(newCube.get_remaining_area()))
        cubes.append(newCube)

for cube in cubes:
    print(cube.get_remaining_area())
    part2count += cube.get_remaining_area()

print("part 2 count:", part2count)