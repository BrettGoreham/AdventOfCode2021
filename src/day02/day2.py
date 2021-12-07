with open('day2Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]


x = 0
y = 0
for i in content:
    part = i.split(' ')
    if part[0] == 'forward':
        x += int(part[1])
    elif part[0] == 'down':
        y += int(part[1])
    elif part[0] == 'up':
        y -= int(part[1])

print('part 1', (x * y))


x = 0
y = 0
aim = 0
for i in content:
    part = i.split(' ')
    if part[0] == 'forward':
        x += int(part[1])
        y += aim * int(part[1])
    elif part[0] == 'down':
        aim += int(part[1])
    elif part[0] == 'up':
        aim -= int(part[1])


print('part 2', (x * y))
