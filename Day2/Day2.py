def part1():
    score = 0
    with open('Day2.txt') as file:
        for line in file:
            line = line.strip('\n')
            opp, you = line.split(' ')
            score = game(you, opp, score)

    print(score)


def part2():
    score = 0
    with open('Day2.txt') as file:
        for line in file:
            line = line.strip('\n')
            opp, you = line.split(' ')
            you = how_to_move(you, opp)
            score = game(you, opp, score)

    print(score)


# x = loose,    y = draw      z = win
def how_to_move(gamestate, opp):
    if gamestate == 'Y':
        if opp == 'A':
            return 'X'
        elif opp == 'B':
            return 'Y'
        else:
            return 'Z'

    if opp == 'A' and gamestate == 'X':
        return 'Z'

    elif opp == 'A' and gamestate == 'Z':
        return 'Y'

    elif opp == 'B' and gamestate == 'X':
        return 'X'

    elif opp == 'B' and gamestate == 'Z':
        return 'Z'

    elif opp == 'C' and gamestate == 'X':
        return 'Y'

    elif opp == 'C' and gamestate == 'Z':
        return 'X'


def game(you, opp, score):
    if you == 'X':  # rock
        score += 1
        you = 'A'

    elif you == 'Y':  # paper
        score += 2
        you = 'B'

    else:
        score += 3  # scissors
        you = 'C'

    if you > opp or (you == 'A' and opp == 'C'):
        if you == 'C' and opp == 'A':
            score += 0
        else:
            score += 6

    elif you == opp:
        score += 3

    else:
        score += 0

    return score


if __name__ == '__main__':
    # part1()
    part2()
