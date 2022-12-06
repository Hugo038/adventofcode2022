import re

with open('input/day5.txt') as f:
    data = [x for x in f.read().split('\n')]
    instructions = [re.split(' from | to ', i.replace("move ", "")) for i in data]
    instructions = [[int(j) for j in i] for i in instructions]

crates = [['W', 'D', 'G', 'B', 'H', 'R', 'V'],
          ['J', 'N', 'G', 'C', 'R', 'F'],
          ['L', 'S', 'F', 'H', 'D', 'N', 'J'],
          ['J', 'D', 'S', 'V'],
          ['S', 'H', 'D', 'R', 'Q', 'W', 'N', 'V'],
          ['P', 'G', 'H', 'C', 'M'],
          ['F', 'J', 'B', 'G', 'L', 'Z', 'H', 'C'],
          ['S', 'J', 'R'],
          ['L', 'G', 'S', 'R', 'B', 'N', 'V', 'M']]

def part1():
    for i in instructions:
        for _ in range(i[0]):
            last_crate = crates[i[1]-1].pop()
            crates[i[2]-1].append(last_crate)
    anslist = [i[-1] for i in crates]
    return ''.join(anslist)

def part2():
    for i in instructions:
        last_crate = crates[i[1]-1][-i[0]:]
        del crates[i[1]-1][-i[0]:]
        for j in last_crate:
            crates[i[2]-1].append(j)
    anslist = [i[-1] for i in crates]
    return ''.join(anslist)

print(part1(), part2())


