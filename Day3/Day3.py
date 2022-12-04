def letter_to_number(letter):
    alphabet = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    score = alphabet.index(letter)
    return score + 1


def comp_string(comp1, comp2):
    for l1 in comp1:
        for l2 in comp2:
            if l1 == l2:
                return l1


def parse_data():
    score = 0
    with open('Day3.txt') as file:
        for line in file:
            line = line.strip('\n')
            length = int(len(line) / 2)
            comp1 = line[0:length]
            comp2 = line[length:]

            letter = comp_string(comp1, comp2)
            score += letter_to_number(letter)
    print(score)


if __name__ == '__main__':
    parse_data()
