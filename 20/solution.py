BEGIN = 'B'
END = 'E'

def get_lines(filename='input'):
    input_file = open(f'{filename}.txt', 'r')
    return [line.rstrip("\n") for line in input_file.readlines()]


def get_ranges():
    ranges = []
    for line in get_lines():
        begin, end = line.split('-')
        ranges.append((int(begin), int(end)))

    return ranges


def lowest_not_blocked(ip_ranges):
    points = []
    for begin, end in ip_ranges:
        points.append((begin, BEGIN))
        points.append((end + 1, END))

    points.sort()

    balance = 0

    for value, direction in points:
        balance += direction == BEGIN
        balance -= direction == END

        if balance == 0:
            return value

    raise Exception('No ip available')

ranges = get_ranges()
lowest_ip = lowest_not_blocked(ranges)

print(lowest_ip)
