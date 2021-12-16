import numpy


def get_val(_operand, _sub_numbers):
    _val = -1
    if _operand == 0:
        _val = sum(_sub_numbers)
    elif _operand == 1:
        if len(_sub_numbers) == 1:
            _val = _sub_numbers[0]
        else:
            _val = numpy.prod(_sub_numbers)
    elif _operand == 2:
        _val = min(_sub_numbers)
    elif _operand == 3:
        _val = max(_sub_numbers)
    elif _operand == 5:
        _val = int(_sub_numbers[0] > _sub_numbers[1])
    elif _operand == 6:
        _val = int(_sub_numbers[0] < _sub_numbers[1])
    elif _operand == 7:
        _val = int(_sub_numbers[0] == _sub_numbers[1])

    return _val


with open('day16Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

hexToBits = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
             '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

bits = ''
for letter in content[0]:
    bits += hexToBits[letter]

versionTotal = 0
produced = 0

# used to keep track of the current parent that the packet is a child of.
remainingLengthOfPacket = float('inf')
packetType = -1
parentLengthType = -1

subNumbers = []
parentPacketStack = []

index = 0

while index < len(bits) and '1' in bits[index:]:
    startIndex = index

    versionTotal += int(bits[index: index + 3], 2)
    index += 3
    childPacketType = int(bits[index:index + 3], 2)
    index += 3

    if childPacketType == 4:
        finished = False
        value = ''
        while finished is False:
            value += bits[index + 1: index + 5]

            if bits[index] == '0':
                subNumbers.append(int(value, 2))
                finished = True
            index += 5

        if parentLengthType == 0:
            remainingLengthOfPacket -= index - startIndex
    else:
        if packetType != -1:
            parentPacketStack.append([packetType, parentLengthType, remainingLengthOfPacket, subNumbers])

        packetType = childPacketType
        subNumbers = []

        parentLengthType = int(bits[index], 2)
        index += 1

        if parentLengthType == 0:
            remainingLengthOfPacket = int(bits[index:index + 15], 2)
            index += 15
        else:
            remainingLengthOfPacket = int(bits[index:index + 11], 2)
            index += 11

    for x in parentPacketStack:
        if x[1] == 0:
            x[2] -= index - startIndex

    while (parentLengthType == 0 and remainingLengthOfPacket == 0) or \
            (parentLengthType == 1 and remainingLengthOfPacket == len(subNumbers)):
        val = get_val(packetType, subNumbers)

        if 0 == len(parentPacketStack):
            produced = val
            subNumbers = []
        else:
            packetType, parentLengthType, remainingLengthOfPacket, subNumbers = parentPacketStack.pop(len(parentPacketStack) - 1)
            subNumbers.append(val)

print('part1', versionTotal)
print('part2', produced)
