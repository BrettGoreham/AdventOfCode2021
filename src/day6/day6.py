def get_fish_count(_fish_map, iterations):
    for i in range(iterations):
        new = {}
        for key in _fish_map:
            value = _fish_map[key]
            if key == 0:
                new[8] = value
            new_key = key - 1
            if new_key == -1:
                new_key = 6

            new[new_key] = new.get(new_key, 0) + _fish_map[key]

        _fish_map = new

    count = 0
    for key in _fish_map:
        count += _fish_map[key]

    return count


with open('day6Input.txt') as f:
    content = f.readlines()
content = [int(x) for x in content[0].split(',')]

fishMap = {}
for x in range(len(content)):
    fishMap[content[x]] = fishMap.get(content[x], 0) + 1

print('part 1: ', get_fish_count(fishMap.copy(), 80))
print('part 2: ', get_fish_count(fishMap.copy(), 256))
