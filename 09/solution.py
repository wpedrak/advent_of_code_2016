def get_line(filename='input'):
    f = open(f'{filename}.txt', 'r')
    return [line.rstrip("\n") for line in f.readlines()][0]


def expand(string):
    current_expansion = []
    idx = 0

    while idx < len(string):
        letter = string[idx]
        if letter != '(':
            current_expansion.append(letter)
            idx += 1

        matching_bracket_idx = string.find(')', idx)
        marker = string[idx + 1:matching_bracket_idx]
        number_of_letters, repetition = parse_marker(marker)
        after_marker_idx = matching_bracket_idx + 1
        concerning_substring = string[after_marker_idx:after_marker_idx + number_of_letters]
        current_expansion.append(concerning_substring * repetition)
        idx = after_marker_idx + number_of_letters

    return ''.join(current_expansion)


def parse_marker(marker):
    return [int(x) for x in marker.split('x')]


string = get_line()
expanded_string = expand(string)
print(len(expanded_string))
