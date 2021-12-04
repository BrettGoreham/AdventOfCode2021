def check_board(_board):
    for x in range(5):
        bingo = True
        for y in range(5):
            if _board[x][y] != '':
                bingo = False
        if bingo:
            return bingo
    for y in range(5):
        bingo = True
        for x in range(5):
            if _board[x][y] != '':
                bingo = False
        if bingo:
            return bingo
    return False


def find_number(_board, number):
    for x in range(5):
        for y in range(5):
            if _board[x][y] == number:
                _board[x][y] = ''
                return True
    return False


def count_remaining_numbers(_board):
    count = 0
    for x in range(5):
        for y in range(5):
            if _board[x][y] != '':
                count += int(_board[x][y])

    return count


with open('day4Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

numbersDrawn = content[0].split(',')
boards = []

for i in range(2, len(content)-1, 6):
    board = []
    for j in range(5):
        board.append(list(filter(lambda c: c != '', content[i+j].split(' '))))

    boards.append(board)


numCount = 0
firstBingo = True
lastDrawnNumberForFirstBingo = -1

lastDrawnNumberForLastBingo = -1

boardsThatHaveWon = []
while len(boardsThatHaveWon) < len(boards):
    num = numbersDrawn[numCount]
    for i in range(len(boards)):
        if i in boardsThatHaveWon:
            continue

        found = find_number(boards[i], num)
        if found:
            complete = check_board(boards[i])
            if complete:
                boardsThatHaveWon.append(i)
                if firstBingo:
                    lastDrawnNumberForFirstBingo = num
                    firstBingo = False

                lastDrawnNumberForLastBingo = num
                lastBoardCompleted = i

    numCount += 1

firstWinCount = count_remaining_numbers(boards[boardsThatHaveWon[0]])
print('part1 ', firstWinCount * int(lastDrawnNumberForFirstBingo))

lastWinCount = count_remaining_numbers(boards[boardsThatHaveWon[len(boardsThatHaveWon) - 1]])
print('part2 ', lastWinCount * int(lastDrawnNumberForLastBingo))
