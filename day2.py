with open('input/day2.txt') as f:
    data = [x.split(" ") for x in f.read().split('\n')]

def part1():
    points = 0
    for i in data:
        match i:
            case ['A', 'X']:
                points += 4
            case ['A', 'Y']:
                points += 8
            case ['A', 'Z']:
                points += 3
            case ['B', 'X']:
                points += 1
            case ['B', 'Y']:
                points += 5
            case ['B', 'Z']:
                points += 9
            case ['C', 'X']:
                points += 7
            case ['C', 'Y']:
                points += 2
            case ['C', 'Z']:
                points += 6
    return points

def part2():
    points = 0
    for i in data:
        match i:
            case ['A', 'X']:
                points += 3
            case ['A', 'Y']:
                points += 4
            case ['A', 'Z']:
                points += 8
            case ['B', 'X']:
                points += 1
            case ['B', 'Y']:
                points += 5
            case ['B', 'Z']:
                points += 9
            case ['C', 'X']:
                points += 2
            case ['C', 'Y']:
                points += 6
            case ['C', 'Z']:
                points += 7
    return points


print(part1(), part2())
