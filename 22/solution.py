import itertools


def get_lines(filename='input'):
    input_file = open(f'{filename}.txt', 'r')
    return [line.rstrip("\n") for line in input_file.readlines()]


def get_nodes():
    return [parse_node(line) for line in get_lines()[2:]]


def parse_node(line):
    splited = line.split()
    name = splited[0]
    size = parse_int_with_suffix(splited[1])
    used = parse_int_with_suffix(splited[2])
    available = parse_int_with_suffix(splited[3])
    use_percent = parse_int_with_suffix(splited[4])

    return (name, size, used, available, use_percent)


def parse_int_with_suffix(string):
    return int(string[:-1])


def count_viable_pairs(nodes):
    count = 0
    for node_a, node_b in itertools.product(nodes, repeat=2):
        name_a, _, used_a, _, _ = node_a
        name_b, _, _, available_b, _ = node_b

        if used_a == 0:
            continue

        if name_a == name_b:
            continue

        count += used_a <= available_b

    return count


nodes = get_nodes()
count = count_viable_pairs(nodes)

print(count)

# 882 is too high
