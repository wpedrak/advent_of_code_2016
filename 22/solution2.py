import itertools

EMPTY = '_'
REGULAR = '.'
BIG = '#'


class Node:
    def __init__(self, position, size, used, available):
        self.x = position[0]
        self.y = position[1]
        self.position = position
        self.size = size
        self.used = used
        self.available = available


def get_lines(filename='input'):
    input_file = open(f'{filename}.txt', 'r')
    return [line.rstrip("\n") for line in input_file.readlines()]


def get_nodes():
    return [parse_node(line) for line in get_lines()[2:]]


def parse_node(line):
    splited = line.split()
    splited_name = splited[0].split('-')
    position = tuple(int(c[1:]) for c in splited_name[1:])
    size = parse_int_with_suffix(splited[1])
    used = parse_int_with_suffix(splited[2])
    available = parse_int_with_suffix(splited[3])

    return Node(position, size, used, available)


def parse_int_with_suffix(string):
    return int(string[:-1])


def shortest_path(nodes):
    network_map = tokenize(nodes)
    # print_network(network_map)
    # printing grid shows us that we only need to go through wall of big nodes

    grid_x = max(network_map, key=lambda k: k[0])[0]

    empty_node = min(nodes, key=lambda n: n.used)
    steps_to_first_move = empty_node.x + empty_node.y + (grid_x - 1) + 1
    move_cost = 5
    moves_to_perform = grid_x - 1

    return steps_to_first_move + moves_to_perform * move_cost


def tokenize(nodes):
    threshold = find_big_node_threshold(nodes)
    network_map = {}

    for node in nodes:
        token = get_token(threshold, node)
        network_map[node.position] = token

    return network_map


def get_token(threshold, node):
    if node.used == 0:
        return EMPTY

    if node.size <= threshold:
        return REGULAR

    return BIG


def find_big_node_threshold(nodes):
    nodes_by_size = list(sorted(nodes, key=lambda n: n.size))
    previous_node = nodes_by_size[0]
    smallest_size = previous_node.size

    for node in nodes_by_size[1:]:
        if node.size - previous_node.size > smallest_size:
            return previous_node.size

        previous_node = node

    raise Exception('No big threshold')


def print_network(network):
    max_x = max(network, key=lambda k: k[0])[0]
    max_y = max(network, key=lambda k: k[1])[1]

    for y in range(max_y + 1):
        for x in range(max_x + 1):
            item = network[(x, y)]
            print(item, end='')

        print('')


nodes = get_nodes()
start_position = (35, 0)
target_position = (0, 0)
# remark 1: excluding empty node, none of nodes have enough available space to fit data from any other node
# max available: 30T
# min used: 64T
path_length = shortest_path(nodes)

print(path_length)

# 239 too low
