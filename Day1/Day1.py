
def parse_data(calorie, count, storage):
    if count in storage:
        storage[count] = storage[count] + calorie
    else:
        storage[count] = calorie
    return storage


def do_the_thing():
    storage = dict()
    count = 0
    with open('Day1.txt') as file:
        for line in file:
            line = line.strip('\n')
            if line == '':
                count += 1
                continue
            parse_data(int(line), count, storage)

    print(f'Part1: {storage[max(storage, key=storage.get)]}')

    cal = 0
    storage = sorted(storage.values(), reverse=True)
    for i in range(3):
        cal += storage[i]
    print(f'Part2: {cal}')


if __name__ == '__main__':
    do_the_thing()
