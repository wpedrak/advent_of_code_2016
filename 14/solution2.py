from collections import defaultdict, deque
import hashlib
import re


def generate_pad(salt):
    idx = 0

    last_five = defaultdict(lambda: -float('inf'))
    to_check = deque()
    keys = set()

    while True:
        while to_check and to_check[0][1] == idx:
            items, _ = to_check.popleft()
            if is_key(items, last_five, idx):
                keys.add(idx)
                print(len(keys))
            if len(keys) == 64:
                print(idx - 1001)
                return

        current_hash = get_hash_with_stretching(f'{salt}{idx}')
        threes = get_in_row(3, current_hash)[:1]
        fives = get_in_row(5, current_hash)

        to_check.append((threes, idx + 1001))

        for item in fives:
            last_five[item] = idx

        idx += 1


def is_key(items, last_five, idx):
    my_idx = idx - 1001
    for item in items:
        if my_idx < last_five[item] <= my_idx + 1000:
            return True

    return False


def get_in_row(occurences, text):
    expresion = r'(\w)' + r'\1' * (occurences - 1)
    return re.findall(expresion, text)


def get_hash_with_stretching(text):
    for _ in range(2017):
        text = hashlib.md5(text.encode()).hexdigest()

    return text

def get_hash(text):
    return hashlib.md5(text.encode()).hexdigest()


salt = 'yjdafjpo'
generate_pad(salt)
