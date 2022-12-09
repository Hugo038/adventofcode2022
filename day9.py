with open('input/day9.txt') as f:
    data = [x.split(' ') for x in f.read().split('\n')]

def check_is_next_or_on(H, T):
    if abs(H[0] - T[0]) in [0,1] and abs(H[1] - T[1]) in [0,1]:
        if H[0] == T[0] and H[1] == T[1]:
            return 'on'
        if H[0] == T[0] or H[1] == T[1]:
            return 'adjacent'
        else:
            return 'diagonal'
    else:
        return 'move_tail'

def give_options(T):
    return [[T[0], T[1] + 1], [T[0], T[1] - 1], [T[0] + 1, T[1]], [T[0] - 1, T[1]], [T[0] + 1, T[1] + 1], [T[0] + 1, T[1] - 1], [T[0] - 1, T[1] - 1], [T[0] - 1, T[1] + 1]]

def move_H(H,i):
    if i[0] == 'R':
        return [H[0]+1, H[1]]
    if i[0] == 'L':
        return [H[0]-1, H[1]]
    if i[0] == 'U':
        return [H[0], H[1]+1]
    if i[0] == 'D':
        return [H[0], H[1]-1]


def part1():
    H = [0,0]
    T = [0,0]
    tail_locations = [[0,0]]
    for x in data:
        for i in range(int(x[1])):
            H = move_H(H,x)
            if check_is_next_or_on(H, T) == 'move_tail':
                for i in give_options(T):
                    if check_is_next_or_on(H, i) == 'adjacent':
                        T = i
                        if T not in tail_locations:
                            tail_locations.append(T)
                        break
    return len(tail_locations)

print(part1())
