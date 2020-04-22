import itertools


def get_lines(filename='input'):
    input_file = open(f'{filename}.txt', 'r')
    return [line.rstrip("\n") for line in input_file.readlines()]


def get_instructions():
    instructions = []
    for line in get_lines():
        splited = line.split()
        instructions.append((' '.join(splited[:2]), splited[2:]))

    return instructions


def scramble(operations, instructions, password):
    list_pasword = list(password)
    for name, args in instructions:
        operation = operations[name]
        list_pasword = operation(list_pasword, args)

    return ''.join(list_pasword)


def swap_pos(password, args):
    pos1 = int(args[0])
    pos2 = int(args[3])
    password[pos1], password[pos2] = password[pos2], password[pos1]

    return password


def swap_letter(password, args):
    pos1 = password.index(args[0])
    pos2 = password.index(args[3])
    password[pos1], password[pos2] = password[pos2], password[pos1]

    return password


def rotate_left(password, args):
    shift = int(args[0])
    return rotate(password, shift, -1)


def rotate_right(password, args):
    shift = int(args[0])
    return rotate(password, shift, 1)


def rotate(password, shift, direction):
    return [password[(idx - (direction * shift)) % len(password)] for idx in range(len(password))]


def rotate_based(password, args):
    letter = args[4]
    idx = password.index(letter)
    shift = 1 + idx + (idx >= 4)
    return rotate(password, shift, 1)


def reverse_positions(password, args):
    start = int(args[0])
    end = int(args[2])
    password[start:end+1] = reversed(password[start:end+1])

    return password


def move_position(password, args):
    move_from = int(args[0])
    move_to = int(args[3])

    item = password[move_from]
    del password[move_from]
    password.insert(move_to, item)

    return password


def unscramble(operations, instructions, scrambled_password):
    time = 0
    for password in itertools.permutations('abcdefgh', 8):
        time += 1
        if time % 1000 == 0:
            print(time)
        current_scrambled_password = scramble(operations, instructions, password)
        if current_scrambled_password == scrambled_password:
            return ''.join(password)

    raise Exception('Not found')


operations = {
    'swap position': swap_pos,
    'swap letter': swap_letter,
    'rotate left': rotate_left,
    'rotate right': rotate_right,
    'rotate based': rotate_based,
    'reverse positions': reverse_positions,
    'move position': move_position,
}

scrambled_password = 'fbgdceah'
instructions = get_instructions()
password = unscramble(operations, instructions, scrambled_password)


print(password)
