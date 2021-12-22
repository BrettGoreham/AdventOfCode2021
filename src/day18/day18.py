import math

global countUpdates
countUpdates = 1


class SnailNumber:

    def __init__(self, parent):
        self.parent = parent
        self.value = None
        self.leftChild = None
        self.rightChild = None

    def get_value(self):
        return self.value

    def add_value(self, value):
        self.value = value

    def add_left_child(self, snail_number):
        self.leftChild = snail_number
        snail_number.parent = self

    def add_right_child(self, snail_number):
        self.rightChild = snail_number
        snail_number.parent = self

    def get_right_child(self):
        return self.rightChild

    def get_left_child(self):
        return self.leftChild

    def set_parent(self, snail_number):
        self.parent = snail_number


with open('day18Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

snailNumberList = []


def parse_child(_line, index, parent_snail):
    index += 1
    child = SnailNumber(parent_snail)

    if _line[index] == '[':
        left_child, index = parse_child(_line, index, child)
        child.add_left_child(left_child)
    else:
        left_child = SnailNumber(child)
        number_end = _line.index(',', index)
        left_child.value = int(_line[index: number_end])
        child.add_left_child(left_child)
        index = number_end+1

    if _line[index] == '[':
        right_child, index = parse_child(_line, index, child)
        child.add_right_child(right_child)
    else:
        right_child = SnailNumber(child)
        number_end = _line.index(']', index)
        s = _line[index: number_end]
        right_child.value = int(s)
        child.add_right_child(right_child)
        index = number_end + 1

    if child.parent.rightChild is None:
        index += 1
    else:
        index += 2
    return child, index


def parse_to_snail_number(_line):
    parent_snail = SnailNumber(None)
    index = 1
    if _line[index] == '[':
        left_child, index = parse_child(_line, index, parent_snail)
        parent_snail.add_left_child(left_child)
    else:
        left_child = SnailNumber(parent_snail)
        number_end = _line.index(',', index)
        s = _line[index: number_end]
        left_child.value = int(s)
        parent_snail.add_left_child(left_child)
        index = number_end + 1

    if _line[index] == '[':
        right_child, index = parse_child(_line, index, parent_snail)
        parent_snail.add_right_child(right_child)
    else:
        right_child = SnailNumber(parent_snail)
        number_end = _line.index(']', index)
        s = _line[index: number_end]
        right_child.value = int(s)
        parent_snail.add_right_child(right_child)


    return parent_snail


#returns true if parent explodes
def explode_left(parent, child, value, depth):
    if parent.leftChild is not child and parent.leftChild.value is not None:
        parent.leftChild.value += value
        if parent.leftChild.value >= 10:
            split(parent.leftChild)
    elif parent.leftChild is not child:
        rightChild = parent.leftChild.rightChild
        depth += 2
        while rightChild.rightChild is not None:
            rightChild = rightChild.rightChild
            depth += 1
        rightChild.value += value
        if rightChild.value >= 10:
            split(rightChild)
    elif parent.parent is not None:
        explode_left(parent.parent, parent, value, depth-1)


def explode_right(parent, child, value, depth):

    if parent.rightChild is not child and parent.rightChild.value is not None:
        parent.rightChild.value += value
        if parent.rightChild.value >= 10:
            split(parent.rightChild)
    elif parent.rightChild is not child:
        leftChild = parent.rightChild.leftChild
        depth += 2
        while leftChild.leftChild is not None:
            leftChild = leftChild.leftChild
            depth+1

        leftChild.value += value
        if leftChild.value >= 10:
            split(leftChild)

    elif parent.parent is not None:
        explode_right(parent.parent, parent, value, depth-1)


def split(parent):
    global countUpdates
    print('split', parent.value)
    left_child = SnailNumber(parent)
    left_child.value = math.floor((parent.value / 2))
    parent.add_left_child(left_child)
    right_child = SnailNumber(parent)
    right_child.value = math.ceil((parent.value / 2))
    parent.add_right_child(right_child)
    countUpdates = countUpdates + 1
    parent.value = None


def check_depth(parent: SnailNumber, parent_depth):
    global countUpdates
    a = ""
    if parent.value is not None:
        if parent.value >= 10:
            split(parent, parent_depth)

    if parent_depth >= 4 and parent.value is None and \
            parent.leftChild.value is not None and \
            parent.rightChild.value is not None:
        print('yeehaa lets explode', parent.leftChild.value, parent.rightChild.value)
        explode_left(parent.parent, parent, parent.leftChild.value, parent_depth)
        explode_right(parent.parent, parent, parent.rightChild.value, parent_depth)
        return True
    else:
        if parent.leftChild is not None and check_depth(parent.leftChild, parent_depth + 1):
            countUpdates = countUpdates + 1
            parent.leftChild.value = 0
            parent.leftChild.leftChild = None
            parent.leftChild.rightChild = None

        if parent.rightChild is not None and check_depth(parent.rightChild, parent_depth + 1):
            countUpdates = countUpdates + 1
            parent.rightChild.value = 0
            parent.rightChild.leftChild = None
            parent.rightChild.rightChild = None
    return False


for line in content:
    snailNumberList.append(parse_to_snail_number(line))

for snail in snailNumberList:
    check_depth(snail, 0)


print('start addin')

start = snailNumberList[0]

for snailnum in range(1, len(snailNumberList)):
    newParent = SnailNumber(None)
    newParent.add_left_child(start)
    newParent.add_right_child(snailNumberList[snailnum])

    countUpdates = 1
    while countUpdates > 0:
        print('loops')
        countUpdates = 0
        check_depth(newParent, 0)

    start = newParent


a = 's'
