import math
import time
import bisect
from datetime import timedelta

with open('day15Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

map = []
for line in content:
    map.append([int(x) for x in line])

map2 = []
for y in range(len(map) * 5):
    yIndex = math.floor(y / len(map))
    yvalue = y % len(map)
    row = []
    for x in range(len(map[0] * 5)):
        xIndex = math.floor(x / len(map[0]))
        xvalue = x % len(map[0])
        val = map[yvalue][xvalue] + yIndex + xIndex

        if val > 9:
            val = val - 9
        row.append(val)
    map2.append(row)


def sorted_insert(_paths, value):
    lo= 0
    hi = len(_paths)
    while lo < hi:
        mid = (lo + hi) // 2
        if value[1] < _paths[mid][1]:
            hi = mid
        else:
            lo = mid + 1
    _paths.insert(lo, value)
    return _paths


def find_fastest_path(_map, _goal):
    vectors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    paths = [[(0,0), 0]]
    lowest_to_point = {}
    while len(paths) > 0:
        path = paths.pop(0)
        point = path[0]
        value = path[1]
        #if path was added before goal was found but value is greater than goals current skip path and move on
        if value < lowest_to_point.get(_goal, float('inf')):
            for vector in vectors:
                new_point = (point[0] + vector[0], point[1] + vector[1])
                if 0 <= new_point[0] < len(_map) and 0 <= new_point[1] < len(_map[0]):
                    new_point_value = value + _map[new_point[0]][new_point[1]]
                    # if new point is not the lowest value for that point already found current path cant be the fastest.
                    if new_point_value < lowest_to_point.get(new_point, float('inf')):
                        # no point in keeping going if already greater
                        if new_point_value < lowest_to_point.get(_goal, float('inf')):
                            # sorted inserting to ensure that the next path to check is the lowest value.
                            paths = sorted_insert(paths, [new_point, new_point_value])
                            lowest_to_point[new_point] = new_point_value



    return lowest_to_point[(len(_map)-1, len(_map[0])-1)]


start_time = time.monotonic()
print('part1: ',find_fastest_path(map, (len(map) - 1, len(map[0])-1)))
end_time = time.monotonic()
print(timedelta(seconds=end_time - start_time))


start_time = time.monotonic()
print('part2: ', find_fastest_path(map2, (len(map2) - 1, len(map2[0])-1)))
end_time = time.monotonic()
print(timedelta(seconds=end_time - start_time))