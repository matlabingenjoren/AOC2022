def letter_to_number(letter):
    alphabet = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    score = alphabet.index(letter)
    return score + 1


def comp_string(pack1, pack2, pack3):
    for l1 in pack1:
        for l2 in pack2:
            for l3 in pack3:
                if l1 == l2 == l3:
                    return l1


def parse_data():
    score = 0
    with open('Day3.txt') as file:
        pack1 = pack2 = pack3 = ''

        for line in file:

            line = line.strip('\n')
            if pack1 == '':
                pack1 = line
                continue
            elif pack2 == '':
                pack2 = line
                continue
            else:
                pack3 = line

            letter = comp_string(pack1, pack2, pack3)
            score += letter_to_number(letter)
            pack1 = pack2 = pack3 = ''

    print(score)


if __name__ == '__main__':
    parse_data()
