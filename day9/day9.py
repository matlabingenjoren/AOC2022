def move_it(direction, length, pos_h, pos_t, visited):
    if direction == 'U': # [0, 1]
        for _ in range(length):
            pos_h[1] += 1
            solve_tail(pos_h, pos_t, visited)

    elif direction == 'D': # [0, -1]
        for _ in range(length):
            pos_h[1] -= 1
            solve_tail(pos_h, pos_t, visited)

    elif direction == 'R': # [1, 0]
        for _ in range(length):
            pos_h[0] += 1
            solve_tail(pos_h, pos_t, visited)

    else: # direction == 'L'  [-1, 0]
        for _ in range(length):
            pos_h[0] -= 1
            solve_tail(pos_h, pos_t, visited)

    return visited


def solve_tail(pos_h, pos_t, visited):
    if (abs(pos_h[0]-pos_t[0])==2 and abs(pos_h[1]-pos_t[1])==1) or (abs(pos_h[0]-pos_t[0])==1 and abs(pos_h[1]-pos_t[1])==2): #need diagonal snap
        if pos_h[0]-pos_t[0] > 0:
            pos_t[0] += 1
        else:
            pos_t[0] -= 1

        if pos_h[1] - pos_t[1] > 0:
            pos_t[1] += 1
        else:
            pos_t[1] -= 1

    if abs(pos_h[0]-pos_t[0])==2: # needs left or right snap
        if pos_h[0]-pos_t[0] > 0:
            pos_t[0] += 1
        else:
            pos_t[0] -= 1

    if abs(pos_h[1]-pos_t[1])==2: # need up or down snap
        if pos_h[1]-pos_t[1] > 0:
            pos_t[1] += 1
        else:
            pos_t[1] -= 1

    visited.add((pos_t[0], pos_t[1]))

    return visited, pos_t


def parse_data():
    visited = set()
    pos_h = [0, 0]
    pos_t = [0, 0] # [x,y]

    with open('day9.txt') as file:
        for line in file:
            line = line.strip('\n')
            direction, length = line.split()
            move_it(direction, int(length), pos_h, pos_t, visited)

    print(len(visited))


if __name__ == '__main__':
    parse_data()
