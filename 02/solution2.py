UP = 'U'
DOWN = 'D'
LEFT = 'L'
RIGHT = 'R'


def get_lines(filename='input'):
    f = open(f'{filename}.txt', 'r')
    return [line.rstrip("\n") for line in f.readlines()]


def get_code():
    result = ''

    position = (1, 3)
    keypad = [
        '0000000',
        '0001000',
        '0023400',
        '0567890',
        '00ABC00',
        '000D000',
        '0000000'
    ]

    for line in get_lines():
        position = final_position(line, position, keypad)
        x, y = position
        result += keypad[y][x]

    return result


def final_position(instructions, position, keypad):
    for instruction in instructions:
        potential_position = move(instruction, position)
        x, y = potential_position
        item = keypad[y][x]
        if item == '0':
            continue
        position = potential_position

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

    return (x + dx, y + dy)

code = get_code()

print(code)
