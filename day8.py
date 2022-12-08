import pandas as pd

with open('input/day8.txt') as f:
    data = [[int(i) for i in x] for x in f.read().split('\n')]
    df = pd.DataFrame(data)

def check_if_highest(x,y):
    height = df.loc[x,y]
    column = list(df.loc[x, :])
    row = list(df.loc[:, y])
    if all(height > i for i in row[:y]) or all(height > i for i in row[(y+1):]):
        return True
    if all(height > i for i in column[:x]) or all(height > i for i in column[(x + 1):]):
        return True
    else:
        return False

def check_view(x,y):
    height = df.loc[x, y]
    e, w, n, s = 0, 0, 0, 0
    for i in range(1, len(df)+1):
        try:
            boom = df.loc[x, y-i]
            w += 1
            if height > boom:
                pass
            else:
                break
        except:
            break
    for i in range(1, len(df)+1):
        try:
            boom = df.loc[x, y+i]
            e += 1
            if height > boom:
                pass
            else:
                break
        except:
            break
    for i in range(1, len(df)+1):
        try:
            boom = df.loc[x-i, y]
            n += 1
            if height > boom:
                pass
            else:
                break
        except:
            break
    for i in range(1, len(df)+1):
        try:
            boom = df.loc[x+i, y]
            s += 1
            if height > boom:
                pass
            else:
                break
        except:
            break
    return w*s*e*n

def part1():
    visible_trees = 0
    for x in range(len(df)):
        for y in range(len(df)):
            if check_if_highest(x,y):
                visible_trees += 1
    return visible_trees

def part2():
    views = []
    for x in range(len(df)):
        for y in range(len(df)):
            views.append(check_view(x,y))
    return max(views)



print(part1(), part2())