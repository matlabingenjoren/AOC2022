import numpy as np


def view_around(result, trees):
    view_north(result, trees)
    view_east(result, trees)
    view_south(result, trees)
    view_west(result, trees)

    return int(sum(sum(result)))


def view_north(result, trees):
    rn = len(trees[0])
    for x in range(rn):
        curr_height = -1
        for y in range(rn):
            if trees[y][x] > curr_height:
                result[y][x] = 1
                curr_height = int(trees[y][x])
    return result


def view_east(result, trees):
    rn = len(trees[0])
    for y in range(rn):
        curr_height = -1
        for x in range(rn):
            if trees[y][-(x+1)] > curr_height:
                result[y][-(x+1)] = 1
                curr_height = int(trees[y][-(x+1)])
    return result


def view_south(result, trees):
    rn = len(trees[0])
    for x in range(rn):
        curr_height = -1
        for y in range(rn):
            if trees[-(y+1)][x] > curr_height:
                result[-(y+1)][x] = 1
                curr_height = int(trees[-(y+1)][x])
    return result


def view_west(result, trees):
    rn = len(trees[0])
    for y in range(rn):
        curr_height = -1
        for x in range(rn):
            if trees[y][x] > curr_height:
                result[y][x] = 1
                curr_height = int(trees[y][x])
    return result


def look_around(x, y, result, trees):
    look_up(x, y, result, trees)
    look_down(x, y, result, trees)
    look_left(x, y, result, trees)
    look_right(x, y, result, trees)
    return


def look_up(x, y, result, trees):   # klar
    curr_height = trees[y][x]
    seen = 0
    if y == 0:
        result[y][x] *= seen
        return result

    for tmp_y in range(y-1, -1, -1):
        seen += 1
        if trees[tmp_y][x] >= curr_height:
            break

    result[y][x] *= seen
    return result


def look_down(x, y, result, trees):
    rn = len(trees[0])
    curr_height = trees[y][x]
    seen = 0
    if y == rn:
        result[y][x] *= seen
        return result

    for tmp_y in range(y + 1, rn):
        seen += 1
        if trees[tmp_y][x] >= curr_height:
            break

    result[y][x] *= seen
    return result


def look_left(x, y, result, trees):
    curr_height = trees[y][x]
    seen = 0
    if x == 0:
        result[y][x] *= seen
        return result

    for tmp_x in range(x-1, -1, -1):
        seen += 1
        if trees[y][tmp_x] >= curr_height:
            break

    result[y][x] *= seen
    return result


def look_right(x, y, result, trees):
    rn = len(trees[0])
    curr_height = trees[y][x]
    seen = 0
    if x == rn:
        result[y][x] *= seen
        return result

    for tmp_x in range(x+1, rn):
        seen += 1
        if trees[y][tmp_x] >= curr_height:
            break

    result[y][x] *= seen
    return result


def parse_data():
    flag = True
    with open('day8.txt') as file:
        for y, treeline in enumerate(file):
            treeline = treeline.strip('\n')
            if flag:
                result1 = np.zeros((len(treeline), len(treeline)))
                result2 = np.zeros((len(treeline), len(treeline)))+1
                trees = np.zeros((len(treeline), len(treeline)))
                flag = False

            for x, tree in enumerate(treeline):
                trees[y][x] = int(tree)

    part1 = view_around(result1, trees)
    print(f'Part 1: {part1}')

    for y, treeline in enumerate(trees):
        for x, tree in enumerate(treeline):
            look_around(x, y, result2, trees)

    part2 = int(result2.max())
    print(f'Part 2: {part2}')


if __name__ == '__main__':
    parse_data()
