from collections import defaultdict


with open('input/day7.txt') as f:
    data = [x.split(' ') for x in f.read().split('\n')]

def part1_and_2():
    sizes = defaultdict(lambda: 0)
    root = []

    for cmd in data:
        match cmd:
            case ['$', 'cd', '/']:
                root.clear()
            case ['$', 'ls']:
                pass
            case ['dir', folder]:
                pass
            case ['$', 'cd', '..']:
                root.pop()
            case ['$', 'cd', folder]:
                root.append(folder)

            case [size, filename]:
                sizes[tuple(root)] += int(size)
                root_temp = root.copy()
                while len(root_temp) > 0:
                    root_temp.pop()
                    sizes[tuple(root_temp)] += int(size)
    ans1 = sum([i for i in sizes.values() if i<100000])

    delete_size = 30000000-(70000000-sizes[()])
    ans2 = sorted([i for i in sizes.values() if i > delete_size])[0]
    return ans1, ans2

print(part1_and_2())

