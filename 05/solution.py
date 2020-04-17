import hashlib

def get_hash(string):
    return hashlib.md5(string.encode()).hexdigest()

def get_password(prefix):
    result = []
    suffix = 0

    for _ in range(8):
        digit, suffix = get_digit(prefix, suffix)
        result.append(digit)
        print(''.join(result))

    return ''.join(result)

def get_digit(prefix, suffix):

    while True:
        string = prefix + str(suffix)
        current_hash = get_hash(string)
        suffix += 1
        if not starts_with_five_zeros(current_hash):
            continue

        return current_hash[5], suffix

def starts_with_five_zeros(string):
    return string[:5] == '00000'

get_password('reyedfim')
