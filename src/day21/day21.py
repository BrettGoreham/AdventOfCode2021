with open('day21Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

p1Pos = int(content[0].split(': ')[1]) - 1
p2Pos = int(content[1].split(': ')[1]) - 1

p1points = 0
p2points = 0
die = 0
rollCount = 0
p1Turn = True
while p1points < 1000 and p2points < 1000:
    roll = 0
    for x in range(3):
        rollCount += 1
        die += 1
        if die > 100:
            die -= 100
        roll += die

    if p1Turn:
        p1Pos = (p1Pos + roll) % 10
        p1points += p1Pos + 1
    else:
        p2Pos = (p2Pos + roll) % 10
        p2points += p2Pos + 1

    p1Turn = not p1Turn

result = int
if p1points >= 1000:
    result = p2points * rollCount
else:
    result = p1points * rollCount

print('part 1', result)


previouslySeenUniverses = []

p1Win =0
p2Win = 0

p1Pos = int(content[0].split(': ')[1]) - 1
p2Pos = int(content[1].split(': ')[1]) - 1
p1points = 0
p2points = 0
die = 0
rollCount = 0
p1Turn = True
universes = {(p1points, p1Pos, p2points, p2Pos, p1Turn): 1}
rolls = { 3 : 1, 4: 3, 5: 6, 6: 7, 7: 6, 8:3, 9 :1}
while len(universes.keys()) > 0:

    universe, occurrence = universes.popitem()
    for roll in rolls:

        if universe[4]:
            newp1Pos = (universe[1] + roll) % 10
            newp1points = universe[0] + newp1Pos + 1
            if newp1points >= 21:
                p1Win += occurrence * rolls[roll]
                continue
            newUniverse = (newp1points, newp1Pos, universe[2], universe[3], False)
        else:
            newp2Pos = (universe[3] + roll) % 10
            newp2points = universe[2] + newp2Pos + 1
            if newp2points >= 21:
                p2Win += occurrence * rolls[roll]
                continue
            newUniverse = (universe[0], universe[1], newp2points, newp2Pos, True)

        occurrenceOfOld = universes.get(newUniverse, 0)
        universes[newUniverse] = occurrenceOfOld + (occurrence * rolls[roll])


print('part 2 max of: ', p1Win, p2Win)