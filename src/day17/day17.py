with open('day17Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

#target area: x=20..30, y=-10..-5 #exmaple
#target area: x=70..96, y=-179..-124
minX = 70
maxX = 96
miny = -179
maxy = -124
x = 0
count = 0
while x < minX:
    count+=1
    x += count


possibleYs = set()
maxyv = miny
for yv in range(miny, -1 * miny):
    curryv = yv
    ypos = 0
    while ypos > miny:
        ypos += curryv
        curryv -= 1
        if maxy >= ypos >= miny:
            maxyv = yv
            possibleYs.add(yv)
            break


maxHeight = int((maxyv * (maxyv + 1))/2)
print('part 1', maxHeight)

part2 = 0
for yv in possibleYs:
    for xv in range(count, (maxX+1)):
        curryv = yv
        currxv = xv
        x = 0
        y = 0

        while y > miny and x < maxX:
            x += currxv
            currxv = max( (currxv -1), 0 )
            y += curryv
            curryv -= 1

            if minX <= x <= maxX and maxy >= y >= miny:
                part2 += 1  # am accidentially checking xv yv pairs more than once somehow instead of fixing it i used a set
                break

print('part 2', part2)
