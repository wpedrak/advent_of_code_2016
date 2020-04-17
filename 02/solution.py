UP = 'U'
DOWN = 'D'
LEFT = 'L'
RIGHT = 'R'


def get_lines(filename='input'):
    f = open(f'{filename}.txt', 'r')
    return [line.rstrip("\n") for line in f.readlines()]


def get_code():
    result = ''

    position = (1, 1)
    keypad = [
        '123',
        '456',
        '789'
    ]

    for line in get_lines():
        position = final_position(line, position)
        x, y = position
        result += keypad[y][x]

    return int(result)


def final_position(instructions, position):
    for instruction in instructions:
        position = move(instruction, position)

    return position


def move(direction, position):
    delta = {
        UP: (0, -1),
        DOWN: (0, 1),
        LEFT: (-1, 0),
        RIGHT: (1, 0)
    }

    dx, dy = delta[direction]
    x, y, = position

    return (limit(x + dx), limit(y + dy))

def limit(coordinate):
    return min(2, max(0, coordinate))

code = get_code()

print(code)
