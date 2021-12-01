with open('day1Input.txt') as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]


count = 0
prev = None
for c in content:
    curr = c
    if prev is not None and curr > prev:
        count += 1
    prev = curr

print('part 1', count)

count2 = 0
prev = None
for x in range(len(content)-2):
    curr = content[x] + content[x+1] + content[x+2]
    if prev is not None and curr > prev:
        count2 += 1

    prev = curr

print('part 2', count2)


#did this after the fact as a way to do it without repeating so much code
def count_increasing_total(ints, look_ahead):
    _count = 0
    _prev = None
    for x in range(len(ints) - (look_ahead - 1)):
        _curr = 0
        for i in range(look_ahead):
            _curr += ints[x + i]

        if _prev is not None and _curr > _prev:
            _count += 1
        _prev = _curr

    return _count


print('part 1 again', count_increasing_total(content, 1))
print('part 2 again', count_increasing_total(content, 3))