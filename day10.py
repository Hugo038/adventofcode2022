with open('input/day10.txt') as f:
    data = [x.split(' ') for x in f.read().split('\n')]

def part1():
    X = 1
    Xvalues = []
    for i in data:
        match i:
            case ['addx', xvalue]:
                Xvalues.append(X)
                X += int(xvalue)
                Xvalues.append(X)
            case ['noop']:
                Xvalues.append(X)
    return sum(x*y for x,y in zip(list(range(20,len(Xvalues),40)), Xvalues[18::40]))

def lit_or_dark(pixel, sprite_middle, CRT):
    if pixel % 40 in [sprite_middle - 1, sprite_middle, sprite_middle + 1]:
        CRT.append('#')
    else:
        CRT.append('.')

def part2():
    sprite_middle = 1
    pixel = 0
    CRT = []
    for i in data:
        match i:
            case ['addx', value]:
                lit_or_dark(pixel, sprite_middle, CRT)
                pixel += 1
                lit_or_dark(pixel, sprite_middle, CRT)
                pixel += 1
                sprite_middle += int(value)
            case ['noop']:
                lit_or_dark(pixel, sprite_middle, CRT)
                pixel+=1
    for i in range(0,len(CRT), 40):
        print(''.join(CRT[i:i+40]))

print(part1())
print(part2())