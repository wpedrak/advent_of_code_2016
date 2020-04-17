def get_lines(filename='input'):
    f = open(f'{filename}.txt', 'r')
    return [line.rstrip("\n") for line in f.readlines()]

def get_triplets():
    triplets = []
    for line in get_lines():
        triplet = [int(x) for x in line.split()]
        triplets.append(triplet)

    return triplets

def is_valid_triangle(edges):
    a, b, c = sorted(edges)

    return a + b > c

valid_triangles_number = sum(map(
    is_valid_triangle,
    get_triplets()
))

print(valid_triangles_number)
