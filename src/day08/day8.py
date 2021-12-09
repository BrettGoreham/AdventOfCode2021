def get_key():
    return {0: {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
     1: {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
     2: {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
     3: {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
     4: {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
     5: {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
     6: {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
     7: {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
     8: {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
     9: {'a', 'b', 'c', 'd', 'e', 'f', 'g'}}


def check_number_with_one_and_four(_keys, _k, _signal):
    one_count = 0
    for _letter in _keys[1]:
        if _letter in _signal:
            one_count += 1

    if _k == 3:
        return one_count == 2

    if _k == 2:
        if one_count != 1:
            return False
        count = 0
        for _letter in _keys[4]:
            if _letter in _signal:
                count += 1
        return count == 2

    if _k == 5:
        if one_count != 1:
            return False
        count = 0
        for _letter in _keys[4]:
            if _letter in _signal:
                count += 1
        return count == 3


def check_number_with_seven(_keys, _k, _signal):
    count = 0
    for _letter in _keys[7]:
        if _letter in _signal:
            count += 1

    count4 = 0
    for _letter in _keys[4]:
        if _letter in _signal:
            count4 += 1
    if _k == 0:
        return count == 3 and count4 == 3
    if _k == 6:
        return count == 2 and count4 == 3
    if _k == 9:
        return count == 3 and count4 == 4


with open('day8Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

numberToSignalLength = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}

part1Count = 0
part2Total = 0
for x in content:
    keys = get_key()
    signals, answer = x.split(' | ')
    signals = signals.split(' ')
    answer = answer.split(' ')
    signals.sort(key=len)
    for signal in signals:
        signalLen = len(signal)
        potentialNumbers = []
        for k in numberToSignalLength:
            if numberToSignalLength[k] == signalLen:
                canBeNumber = True
                if numberToSignalLength[k] == 5:
                    canBeNumber = check_number_with_one_and_four(keys, k, signal)
                if numberToSignalLength[k] == 6:
                    canBeNumber = check_number_with_seven(keys, k, signal)

                if canBeNumber:
                    potentialNumbers.append(k)

        for num in potentialNumbers:
            keys[num] = keys[num].intersection(set(signal))

    ans = ''
    for y in answer:
        if len(y) == 2 or len(y) == 4 or len(y) == 3 or len(y) == 7:
            part1Count += 1

        for key in keys:
            if numberToSignalLength[key] == len(y):
                found = True
                for letter in y:
                    if letter not in keys[key]:
                        found = False

                if found:
                    ans += str(key)
                    break

    part2Total += int(ans)


print('part1 ', part1Count)
print('part2 ', part2Total)