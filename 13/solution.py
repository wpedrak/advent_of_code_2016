from collections import deque

FAVOURITE_NUMBER = 1358


def bfs(start, target, neighbours):
    to_visit = deque([(start, 0)])
    visited = set()

    while to_visit:
        current, dist = to_visit.popleft()

        if current == target:
            return dist

        for neighbour in neighbours(current):
            if neighbour not in visited:
                visited.add(neighbour)
                to_visit.append((neighbour, dist+1))

    raise Exception(f'{target} not found')


def get_neighbours(point):
    x, y = point
    potential_neighbours = [
        (x+1, y),
        (x-1, y),
        (x, y+1),
        (x, y-1),
    ]

    nonnegative_neighbours = filter(
        lambda p: p[0] >= 0 and p[1] >= 0,
        potential_neighbours
    )

    open_neighbours = filter(
        is_open_space,
        nonnegative_neighbours
    )

    return list(open_neighbours)


def is_open_space(point):
    x, y = point
    number = x*x + 3*x + 2*x*y + y + y*y + FAVOURITE_NUMBER
    binary_repr = f'{number:b}'
    sum_of_ones = sum(map(int, binary_repr))
    return sum_of_ones % 2 == 0


start = (1, 1)
target = (31, 39)
result = bfs(start, target, get_neighbours)

print(result)
