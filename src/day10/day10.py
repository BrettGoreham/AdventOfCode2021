with open('day10Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

openers = ['(', '[', '{', '<']
closer = {'>': '<', ')': '(', '}': '{', ']': '['}
points = {'>': 25137, ')': 3, '}': 1197, ']': 57}

part2Points = {'(': 1, '{': 3, '[': 2, '<': 4}
lineCompleteScores = []

pointTotal = 0
for line in content:
    errorlessLine = True
    bracketStack = []
    for letter in line:
        if letter in openers:
            bracketStack.append(letter)
        else:
            lastCloser = bracketStack.pop(len(bracketStack) - 1)
            if lastCloser != closer[letter]:
                pointTotal += points[letter]
                errorlessLine = False
                break

    if errorlessLine:
        score = 0
        while len(bracketStack) > 0:
            score = (score * 5) + part2Points[bracketStack.pop(len(bracketStack) - 1)]
        lineCompleteScores.append(score)

print(pointTotal)
lineCompleteScores.sort()
print(lineCompleteScores[int(len(lineCompleteScores)/2)])
