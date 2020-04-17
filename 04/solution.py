from collections import Counter


def get_lines(filename='input'):
    f = open(f'{filename}.txt', 'r')
    return [line.rstrip("\n") for line in f.readlines()]


def parse_rooms():
    return [parse_room(line) for line in get_lines()]


def parse_room(line):
    last_hyphen_idx = line.rfind('-')
    name_part = line[:last_hyphen_idx]
    opening_square_bracket_idx = line.find('[')
    id = int(line[last_hyphen_idx + 1: opening_square_bracket_idx])
    closing_square_bracket_idx = line.find(']')
    checksum = line[opening_square_bracket_idx + 1: closing_square_bracket_idx]

    return name_part, id, checksum


def is_room_real(name, checksum):
    counts = Counter(name)
    counts['-'] = 0

    sorted_by_letters = sorted(counts.items(), key=lambda t: t[0])
    sorted_by_occurences = sorted(
        sorted_by_letters, key=lambda t: t[1], reverse=True)

    first_five = sorted_by_occurences[:5]

    return ''.join([t[0] for t in first_five]) == checksum


def flip(dublet):
    return tuple(reversed(dublet))


rooms = parse_rooms()
real_rooms = list(filter(
    lambda r: is_room_real(r[0], r[2]),
    rooms
))

sum_of_ids = sum([r[1] for r in real_rooms])

print(sum_of_ids)
