NORTH = 'north'
SOUTH = 'south'
WEST = 'west'
EAST = 'east'
LEFT = 'L'
RIGHT = 'R'


def get_lines(filename='input'):
    f = open(f'{filename}.txt', 'r')
    return [line.rstrip("\n") for line in f.readlines()]


def get_directions():
    line = get_lines()[0]
    directions = line.split(', ')

    return [(d[0], int(d[1:])) for d in directions]


def final_position(position, directions):
    facing_direction = NORTH

    for turn_direction, distance in directions:
        facing_direction = turn(facing_direction, turn_direction)
        position = walk(position, facing_direction, distance)

    return position


def turn(current_direction, change):
    directions_order = [NORTH, EAST, SOUTH, WEST]
    changing_factor = 1 if change == RIGHT else -1
    current_idx = directions_order.index(current_direction)
    new_idx = (current_idx + changing_factor) % len(directions_order)

    return directions_order[new_idx]


def walk(position, direction, distance):
    delta = {
        NORTH: (0, 1),
        SOUTH: (0, -1),
        WEST: (-1, 0),
        EAST: (1, 0),
    }
    dx, dy = delta[direction]
    x, y = position
    return (x + dx * distance, y + dy * distance)


start_position = (0, 0)
directions = get_directions()
final_position = final_position(start_position, directions)
x, y = final_position
print(abs(x) + abs(y))
