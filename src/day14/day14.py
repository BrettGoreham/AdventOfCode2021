
def find_polymerization_after_iteration(_iterations, _rules, _line):
    pairs = {}
    for x in range(1, len(_line)):
        pairs[_line[x - 1] + _line[x]] = pairs.get(_line[x - 1] + _line[x], 0) + 1

    for _ in range(_iterations):
        new_pairs = {}
        for _pair in pairs:
            count = pairs[_pair]
            value = rules[_pair]
            new_pairs[_pair[0] + value] = new_pairs.get(_pair[0] + value, 0) + count
            new_pairs[value + _pair[1]] = new_pairs.get(value + _pair[1], 0) + count
        pairs = new_pairs

    _letterCounter = {_line[len(_line) - 1]: 1}
    for _key in pairs:
        val = pairs[_key]
        _letterCounter[_key[0]] = _letterCounter.get(_key[0], 0) + val

    return max(_letterCounter.values()) - min(_letterCounter.values())


with open('day14Input.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

rules = {}
for x in range(2, len(content)):
    pair, result = content[x].split(' -> ')
    rules[pair] = result

print('part 1:', find_polymerization_after_iteration(10, rules, list(content[0])))
print('part 2:', find_polymerization_after_iteration(40, rules, list(content[0])))
