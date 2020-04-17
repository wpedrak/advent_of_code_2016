def get_line(filename='input'):
    f = open(f'{filename}.txt', 'r')
    return [line.rstrip("\n") for line in f.readlines()][0]


def size_of_expanded(string):
    # print(string)
    size = 0
    idx = 0

    while idx < len(string):
        letter = string[idx]
        if letter != '(':
            size += 1
            idx += 1
            continue

        matching_bracket_idx = string.find(')', idx)
        marker = string[idx + 1:matching_bracket_idx]
        number_of_letters, repetition = parse_marker(marker)
        after_marker_idx = matching_bracket_idx + 1
        concerning_substring = string[after_marker_idx:after_marker_idx + number_of_letters]
        size += size_of_expanded(concerning_substring) * repetition
        idx = after_marker_idx + number_of_letters

    return size


def parse_marker(marker):
    # print(marker)
    return [int(x) for x in marker.split('x')]


string = get_line()
result = size_of_expanded(string)
print(result)
