from collections import deque

WALL = '#'
EMPTY = '.'


def get_lines(filename='input'):
    input_file = open(f'{filename}.txt', 'r')
    return [line.rstrip("\n") for line in input_file.readlines()]


def get_map():
    return [list(line) for line in get_lines()]


def is_wall(hvac_map, position):
    x, y = position
    return hvac_map[y][x] == WALL


def is_empty(hvac_map, position):
    return not is_wall(hvac_map, position)


def get_neighbours(position):
    x, y = position
    neighbours = [
        (x+1, y),
        (x-1, y),
        (x, y+1),
        (x, y-1)
    ]

    return neighbours


def optimize_map(hvac_map):
    optimized_map = [row[:] for row in hvac_map]

    for _ in range(20):
        for y in range(1, len(optimized_map) - 1):
            for x in range(1, len(optimized_map[0]) - 1):
                position = (x, y)
                if is_wall(optimized_map, position) or optimized_map[y][x].isnumeric():
                    continue
                neighbours = get_neighbours(position)
                walls_number = sum(map(
                    lambda n: is_wall(optimized_map, n),
                    neighbours
                ))
                if walls_number > 2:
                    optimized_map[y][x] = WALL

    return optimized_map


def print_map(hvac_map):
    for row in hvac_map:
        print(''.join(row))


def find_in_map(hvac_map, lookup_item):
    for y, row in enumerate(hvac_map):
        for x, item in enumerate(row):
            if item == lookup_item:
                return x, y

    raise Exception(f'{lookup_item} not found')


def bfs(start_position, hvac_map, neighbours):
    to_visit = deque([((start_position, frozenset('0')), 0)])
    visited = set()
    all_keys = get_all_keys(hvac_map)

    while to_visit:
        current_state, dist = to_visit.popleft()
        _, keys = current_state

        if keys == all_keys:
            return dist

        for neighbour in neighbours(hvac_map, current_state):
            if neighbour in visited:
                continue

            visited.add(neighbour)
            to_visit.append((neighbour, dist + 1))

    raise Exception(f'{start_position} not found')


def get_all_keys(hvac_map):
    fields = set()
    for row in hvac_map:
        fields |= set(row)

    return frozenset(fields - set('#'))


def neighbours_on_map(hvac_map, state):
    position, keys = state
    neighbours = get_neighbours(position)
    empty_neighbours = list(filter(
        lambda p: is_empty(hvac_map, p),
        neighbours
    ))

    return [
        ((x, y), keys | set([hvac_map[y][x]]))
        for x, y in empty_neighbours
    ]


hvac_map = optimize_map(get_map())
# hvac_map = get_map()
# print_map(hvac_map)
start_position = find_in_map(hvac_map, '0')
min_dist = bfs(start_position, hvac_map, neighbours_on_map)

print(min_dist)

# 472 too high
