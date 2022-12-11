import math

with open('input/day11.txt') as f:
    data = [x.split('\n') for x in f.read().split('\n\n')]
    monkies_input = [[i.replace(":", "").replace('  Starting items ', '').replace('  Operation ', '').replace('  Test divisible by ', '').replace('    If true throw to monkey ','').replace('    If false throw to monkey ', '').replace(' ', '').replace('new=', '') for i in j]  for j in data]


class Monkey:
    def __init__(self, items, change_worry, divisible, if_yes, if_no):
        self.items = items
        self.change_worry = change_worry
        self.divisible = divisible
        self.if_yes = if_yes
        self.if_no = if_no
        self.inspections = 0

    def describe(self):
        print(self.items, self.change_worry, self.divisible, self.if_yes, self.if_no)

    def change_items(self):
        self.items = [math.floor(eval(self.change_worry)/3) for old in self.items]
        self.inspections += len(self.items)

    def change_items_pt_2(self):
        self.items = [eval(self.change_worry)%9699690 for old in self.items]
        self.inspections += len(self.items)

    def receive(self, item):
        self.items.append(item)

    def throw_items(self):
        for i in self.items:
            if i%self.divisible == 0:
                monkies[self.if_yes].receive(i)
            else:
                monkies[self.if_no].receive(i)
        self.items.clear()

    def give_inspections(self):
        return self.inspections

monkies = []

def part1():
    for i in monkies_input:
        monkies.append(Monkey(items=[int(x) for x in i[1].split(',')],
                              change_worry=i[2],
                              divisible=int(i[3]),
                              if_yes=int(i[4]),
                              if_no=int(i[5])))
    for _ in range(20):
        for monkey in monkies:
            monkey.change_items()
            monkey.throw_items()
    return math.prod(sorted([i.give_inspections() for i in monkies], reverse=True)[:2])

def part2():
    for i in monkies_input:
        monkies.append(Monkey(items=[int(x) for x in i[1].split(',')],
                              change_worry=i[2],
                              divisible=int(i[3]),
                              if_yes=int(i[4]),
                              if_no=int(i[5])))
    for i in range(10000):
        for monkey in monkies:
            monkey.change_items_pt_2()
            monkey.throw_items()
    return math.prod(sorted([i.give_inspections() for i in monkies], reverse=True)[:2])

print(part1(), part2())
