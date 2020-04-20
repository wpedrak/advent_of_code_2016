def produce_data(initial_data, data_length):
    data = initial_data
    while len(data) < data_length:
        second_part = ''.join(reversed(data))
        second_part = negate(second_part)
        data = data + '0' + second_part

    return data[:data_length]


def negate(string):
    return ''.join(str((int(c) + 1) % 2) for c in string)


def get_checksum(data):
    checksum = data

    while checksum and len(checksum) % 2 == 0:
        checksum = iterate_checksum(checksum)

    return checksum


def iterate_checksum(data):
    checksum = []
    for idx in range(0, len(data), 2):
        first, second = data[idx:idx+2]
        next_digit = '1' if first == second else '0'
        checksum.append(next_digit)

    return ''.join(checksum)


initial_data = '10010000000110000'
disk_length = 272

data = produce_data(initial_data, disk_length)
checksum = get_checksum(data)

print(checksum)
