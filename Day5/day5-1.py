def CrateMover_9001(amt, fro, to, container):
    #tmp = []
    tmp = container[fro][-amt:]
    for each in tmp:
        container[to].append(each)
    for i in range(amt):
        container[fro].pop()

    return container


def parse_data(container):
    flag = True
    with open('day5.txt') as file:
        for line in file:
            line = line.strip('\n')

            if line == '':
                flag = False
                continue
            elif flag:
                continue
            args = line.replace('move ', '').replace('from ', '').replace('to ', '')
            args = args.split(' ')
            CrateMover_9001(int(args[0]), int(args[1])-1, int(args[2])-1, container)
    x = ''
    for i in range(9):
        if container[i]== []:
            continue
        x += container[i][-1].strip('[').strip(']')
    print(x)


if __name__ == '__main__':
    contain = [['[Z]', '[J]', '[G]'], ['[Q]', '[L]', '[R]', '[P]', '[W]', '[F]', '[V]', '[C]'], ['[F]', '[P]', '[M]', '[C]', '[L]', '[G]', '[R]'], ['[L]', '[F]', '[B]', '[W]', '[P]', '[H]', '[M]'], ['[G]', '[C]', '[F]', '[S]', '[V]', '[Q]'], ['[W]', '[H]', '[J]', '[Z]', '[M]', '[Q]', '[T]', '[L]'],['[H]', '[F]', '[S]', '[B]', '[V]'], ['[F]', '[J]', '[Z]', '[S]'],['[M]', '[C]', '[D]', '[P]', '[F]', '[H]', '[B]', '[T]']]

    #contain = [['Z', 'N'], ['M', 'C', 'D'], ['P']]

    parse_data(contain)
