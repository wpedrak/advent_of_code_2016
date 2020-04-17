def get_lines(filename='input'):
    f = open(f'{filename}.txt', 'r')
    return [line.rstrip("\n") for line in f.readlines()]


def supports_ssl(ip):
    balance = 0
    in_set = set()
    out_set = set()

    for idx, letter in enumerate(ip):
        if letter in '[]':
            balance += letter == '['
            balance -= letter == ']'
            continue

        next_three = ip[idx:idx + 3]

        if not is_aba(next_three):
            continue

        if balance == 0:
            out_set.add(next_three[:2])
            continue
        if balance > 0:
            in_set.add(next_three[1:])

    return len(in_set & out_set) > 0


def is_aba(text):
    if len(text) != 3:
        return False

    if not text.isalpha():
        return False

    return is_palindrome(text) and len(set(text)) == 2


def is_palindrome(text):
    return text == ''.join(reversed(text))


ips = get_lines()
ssl_ips = list(filter(
    supports_ssl,
    ips
))

print(len(ssl_ips))
