with open('day1Input.txt') as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]

count = 0
prev = None
for c in content:
    if prev is None:
        prev = c
    else:
        if c > prev:
            count += 1
        prev = c

print('part 1', count)

count2= 0
prev = None
for x in range(len(content)-2):
    curr = content[x] + content[x+1] + content[x+2]
    print(str(curr) + ' ' + str(prev))
    if prev is not None and curr > prev:
        print('true')
        count2 += 1

    prev = curr

print(count2)



