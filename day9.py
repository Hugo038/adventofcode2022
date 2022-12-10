with open('input/day9.txt') as f:
    data = [x.split(' ') for x in f.read().split('\n')]

def check_if_move(H, T):
    if abs(H[0] - T[0]) in [0,1] and abs(H[1] - T[1]) in [0,1]:
        if H[0] == T[0] and H[1] == T[1]:
            return 'on'
        elif H[0] == T[0] or H[1] == T[1]:
            return 'adjacent'
        else:
            return 'diagonal'
    else:
        return 'move'

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
        for _ in range(int(x[1])):
            H_old = H.copy()
            H = move_H(H,x)
            if check_if_move(H, T) == 'move':
                T = H_old
                if T not in tail_locations:
                    tail_locations.append(T)
    return len(tail_locations)

def part2():
    snake = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
    tail_locations = [[0, 0]]
    for x in data:
        for _ in range(int(x[1])):
            snake[0] = move_H(snake[0], x)
            if check_if_move(snake[0], snake[1]):
                for i in range(1,10):
                    if check_if_move(snake[i], snake[i-1]) == 'move':
                        if any ([check_if_move(snake[i-1], x) == 'adjacent' for x in give_options(snake[i])]):
                            for option in give_options(snake[i]):
                                if check_if_move(snake[i-1], option) == 'adjacent':
                                    snake[i] = option
                        else:
                            for option in give_options(snake[i]):
                                if check_if_move(snake[i-1], option) == 'diagonal':
                                    snake[i] = option
            if snake[-1] not in tail_locations:
                    tail_locations.append(snake[-1])
    return len(tail_locations)

print(part1())
print(part2())
