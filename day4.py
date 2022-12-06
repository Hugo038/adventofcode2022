with open('input/day3.txt') as f:
    data = [x for x in f.read().split('\n')]

def split_sacks():
    sacks_split = []
    for i in data:
        half = len(i)//2
        sacks_split.append([i[:half], i[half:]])
    return sacks_split

def letter_to_number(letter):
    if letter.isupper():
        return ord(letter)-38
    if letter.islower():
        return ord(letter)-96

def part1():
    items = []
    for i in split_sacks():
        items.append(list(set(i[0]) & set(i[1])))
    items = [letter_to_number(j) for k in items for j in k]
    return sum(items)

def part2():
    items_pt2 = []
    groups_of_3 = [data[i: i + 3] for i in range(0, len(data), 3)]
    for i in groups_of_3:
        items_pt2.append(list(set(i[0]) & set(i[1]) & set(i[2])))
    items = [letter_to_number(j) for k in items_pt2 for j in k]
    return sum(items)

print(part2())