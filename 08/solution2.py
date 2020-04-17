ON = '#'
OFF = ' '


def get_lines(filename='input'):
    f = open(f'{filename}.txt', 'r')
    return [line.rstrip("\n") for line in f.readlines()]


def display(screen):
    image = '\n'.join([''.join(row) for row in screen])
    print(image)


def get_instructions():
    lines = get_lines()
    return [get_instruction(line) for line in lines]


def get_instruction(line):
    splited = line.split()
    if splited[0] == 'rect':
        return 'rect', [int(x) for x in splited[1].split('x')]

    name = ' '.join(splited[:2])
    arg1 = int(splited[2][2:])
    arg2 = int(splited[-1])

    return name, [arg1, arg2]


def rect(screen, max_x, max_y):
    for y in range(max_y):
        for x in range(max_x):
            screen[y][x] = ON


def rotate_row(screen, row_idx, shift):
    row = screen[row_idx]
    row_size = len(row)
    new_row = [row[(idx - shift) % row_size] for idx in range(row_size)]
    screen[row_idx] = new_row


def rotate_column(screen, column_idx, shift):
    column_size = len(screen)
    shifted_column = [screen[(y - shift) % column_size][column_idx]
                      for y in range(column_size)]

    for y in range(column_size):
        screen[y][column_idx] = shifted_column[y]


def count_bits(screen):
    return sum(map(
        count_bits_in_row,
        screen
    ))


def count_bits_in_row(row):
    return sum(map(
        lambda x: x == ON,
        row
    ))


screen = [[OFF] * 50 for _ in range(6)]
instructions = {
    'rect': rect,
    'rotate row': rotate_row,
    'rotate column': rotate_column
}

for name, args in get_instructions():
    instruction = instructions[name]
    instruction(screen, *args)

display(screen)
