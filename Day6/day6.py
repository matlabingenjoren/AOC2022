def find_marker(stream):
    buffer = []
    for index, char in enumerate(stream):
        if len(buffer) < 4: # filling the buffer
            buffer.append(char)

        if len(set(buffer)) == 4:
            return index
        else:
            buffer.pop(0)
            buffer.append(char)


def find_message(stream):
    buffer = []
    for index, char in enumerate(stream):
        if len(buffer) < 14: # filling the buffer
            buffer.append(char)

        if len(set(buffer)) == 14:
            return index
        else:
            buffer.pop(0)
            buffer.append(char)


def parse_data():
    with open('day6.txt') as file:
        for line in file:
            line = line.strip('\n')
    part_1 = find_marker(line)
    part_2 = find_message(line)
    print(f'Part 1: {part_1}')
    print(f'Part 2: {part_2}')


if __name__ == '__main__':
    parse_data()
