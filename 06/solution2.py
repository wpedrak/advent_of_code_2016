from collections import defaultdict


def get_lines(filename='input'):
    f = open(f'{filename}.txt', 'r')
    return [line.rstrip("\n") for line in f.readlines()]


def get_message(messages):
    size = len(messages[0])
    frequences = [defaultdict(lambda: 0) for _ in range(size)]

    for message in messages:
        for idx, letter in enumerate(message):
            frequences[idx][letter] += 1

    result = []

    for freq in frequences:
        best_letter = min(freq.items(), key=lambda x: x[1])[0]
        result.append(best_letter)

    return ''.join(result)


messages = get_lines()
message = get_message(messages)

print(message)
