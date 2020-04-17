import hashlib

def get_hash(string):
    return hashlib.md5(string.encode()).hexdigest()

def get_password(prefix):
    result = ['_'] * 8
    suffix = 0

    while '_' in result:
        position, digit, suffix = get_digit(prefix, suffix)
        if position >= len(result) or result[position] != '_':
            continue

        result[position] = digit

        print(''.join(result))

    return ''.join(result)

def get_digit(prefix, suffix):

    while True:
        string = prefix + str(suffix)
        current_hash = get_hash(string)
        suffix += 1
        if not starts_with_five_zeros(current_hash):
            continue


        return int(current_hash[5], base=16), current_hash[6], suffix

def starts_with_five_zeros(string):
    return string[:5] == '00000'

get_password('reyedfim')
