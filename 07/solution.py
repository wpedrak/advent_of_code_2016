def get_lines(filename='input'):
    f = open(f'{filename}.txt', 'r')
    return [line.rstrip("\n") for line in f.readlines()]


def supports_tls(ip):
    balance = 0
    have_abba = False

    for idx, letter in enumerate(ip):
        if letter in '[]':
            balance += letter == '['
            balance -= letter == ']'
            continue

        next_four = ip[idx:idx + 4]
        next_four_is_abba = is_abba(next_four)
        if next_four_is_abba and balance == 0:
            have_abba = True
            continue

        if next_four_is_abba and balance > 0:
            return False

    return have_abba


def is_abba(text):
    if len(text) != 4:
        return False

    if not text.isalpha():
        return False

    return is_palindrome(text) and len(set(text)) == 2


def is_palindrome(text):
    return text == ''.join(reversed(text))


ips = get_lines()
tls_ips = list(filter(
    supports_tls,
    ips
))

print(len(tls_ips))
