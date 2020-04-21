from collections import deque
import hashlib

UP = 'U'
DOWN = 'D'
LEFT = 'L'
RIGHT = 'R'


def bfs(passcode, neighbours):
    start = (0, 0)
    target = (3, 3)
    to_visit = deque([(start, '')])

    while to_visit:
        current, path = to_visit.popleft()

        if current == target:
            return path

        for neighbour, direction in neighbours(current, passcode, path):
            to_visit.append((neighbour, path + direction))

    raise Exception('Path not found')


def get_neighbours(position, passcode, path):
    x, y = position
    neighbours = [
        ((x+1, y), RIGHT),
        ((x-1, y), LEFT),
        ((x, y+1), DOWN),
        ((x, y-1), UP),
    ]
    bounded_neighbours = list(filter(
        lambda n: 0 <= n[0][0] <= 3 and 0 <= n[0][1] <= 3,
        neighbours
    ))
    open_doors = get_open_doors(passcode + path)

    open_neighbours = list(filter(
        lambda n: n[1] in open_doors,
        bounded_neighbours
    ))

    return open_neighbours


def get_open_doors(path_id):
    doors_info = get_hash(path_id)[:4]
    directions_order = [UP, DOWN, LEFT, RIGHT]

    open_doors = []
    for idx, info in enumerate(doors_info):
        if info > 'a':
            open_doors.append(directions_order[idx])

    return open_doors


def get_hash(text):
    return hashlib.md5(text.encode()).hexdigest()


passcode = 'ioramepc'
path = bfs(passcode, get_neighbours)
print(path)
