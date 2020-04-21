def check_next_rows(row, number_of_next_rows):
    number_of_safe = count_safe(row)

    for _ in range(number_of_next_rows):
        row = next_row(row)
        number_of_safe += count_safe(row)

    return number_of_safe


def count_safe(row):
    return sum(map(
        lambda t: t == '.',
        row
    ))


def next_row(row):
    row = ['.'] + row + ['.']
    next_row = []

    for idx in range(len(row) - 2):
        left = row[idx]
        right = row[idx + 2]
        next_tile = '^' if left != right else '.'
        next_row.append(next_tile)

    return next_row


first_row = list('.^^^^^.^^^..^^^^^...^.^..^^^.^^....^.^...^^^...^^^^..^...^...^^.^.^.......^..^^...^.^.^^..^^^^^...^.')
number_of_next_rows = 400000 - 1
number_of_safe_tiles = check_next_rows(first_row, number_of_next_rows)

print(number_of_safe_tiles)
