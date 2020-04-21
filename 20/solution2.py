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


def count_whitelisted(ip_ranges):
    points = []
    for begin, end in ip_ranges:
        points.append((begin, BEGIN))
        points.append((end + 1, END))

    points.sort()

    balance = 0
    last_end = 0
    count = 0

    for value, direction in points:
        balance += direction == BEGIN
        balance -= direction == END

        if direction == END:
            last_end = value
            continue

        if balance == 1 and direction == BEGIN:
            count += value - last_end

    count += 2**32 - last_end

    return count


ranges = get_ranges()
number_of_whitelisted_ips = count_whitelisted(ranges)

print(number_of_whitelisted_ips)
