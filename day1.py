with open("input/day1.txt") as f:
    data = [line.strip() for line in f]
    data = ['0' if item == '' else item for item in data]
    data = [int(i) for i in data]
    data.append(0)

def part1_and_2():
    calories = []
    calorie = 0
    for i in data:
        if i != 0:
            calorie += i
        else:
            calories.append(calorie)
            calorie = 0
    print(calories)

    return max(calories), sum(sorted(calories, reverse=True)[:3])

print(part1_and_2())


