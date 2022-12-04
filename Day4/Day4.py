def taskmaster(elf1, elf2):
    a = int(elf1[0])
    b = int(elf1[1])

    c = int(elf2[0])
    d = int(elf2[1])

    if a <= c <= d <= b:
        return 1
    elif c <= a <= b <= d:
        return 1
    else:
        return 0


def taskmaster_2(elf1, elf2):
    a = int(elf1[0])
    b = int(elf1[1])

    c = int(elf2[0])
    d = int(elf2[1])

    if (a <= c <= b) or (a <= d <= b):
        return 1
    elif (c <= a <= d) or (c <= b <= d):
        return 1
    else:
        return 0


def parse_data():
    score_1 = 0
    score_2 = 0
    with open('day4.txt') as file:
        for line in file:

            line = line.strip('\n')
            elf1, elf2 = line.split(',')
            elf1 = elf1.split('-')
            elf2 = elf2.split('-')

            score_1 += taskmaster(elf1, elf2)
            score_2 += taskmaster_2(elf1, elf2)

    print(score_1)
    print(score_2)


if __name__ == '__main__':
    parse_data()
