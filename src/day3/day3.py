with open('day3Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

gamma = ''
epsilon = ''

for x in range(len(content[0])):
    _0 = 0
    _1 = 0
    for c in content:
        if c[x] == '1':
            _1 += 1
        else:
            _0 += 1

    if _0 > _1:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

print(int(gamma, 2) * int(epsilon, 2))

oxygen = content.copy()
c02 = content.copy()

for x in range(len(content[0])):
    if len(oxygen) == 1:
        break
    _0 = 0
    _1 = 0

    for o in oxygen:
        if o[x] == '1':
            _1 += 1
        else:
            _0 += 1

    if _0 > _1:
        oxygen = list(filter(lambda c: c[x] == '0', oxygen))
    if _1 >= _0:
        oxygen = list(filter(lambda c: c[x] == '1', oxygen))


for x in range(len(content[0])):
    if len(c02) == 1:
        break
    _0 = 0
    _1 = 0

    for o in c02:
        if o[x] == '1':
            _1 += 1
        else:
            _0 += 1

    if _0 > _1:
        c02 = list(filter(lambda c0: c0[x] == '1', c02))
    if _1 >= _0:
        c02 = list(filter(lambda c0: c0[x] == '0', c02))

print (int(oxygen[0], 2) * int(c02[0], 2))

