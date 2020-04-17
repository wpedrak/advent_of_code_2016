def get_lines(filename='input'):
    f = open(f'{filename}.txt', 'r')
    return [line.rstrip("\n") for line in f.readlines()]


def get_triplets():
    triplets = []
    lines = get_lines()
    for idx in range(0, len(lines), 3):
        triplet1 = [int(x) for x in lines[idx].split()]
        triplet2 = [int(x) for x in lines[idx+1].split()]
        triplet3 = [int(x) for x in lines[idx+2].split()]

        current_triplets = [
            triplet1,
            triplet2,
            triplet3
        ]

        triplets.append([triplet[0] for triplet in current_triplets])
        triplets.append([triplet[1] for triplet in current_triplets])
        triplets.append([triplet[2] for triplet in current_triplets])

    return triplets


def is_valid_triangle(edges):
    a, b, c = sorted(edges)

    return a + b > c


valid_triangles_number = sum(map(
    is_valid_triangle,
    get_triplets()
))

print(valid_triangles_number)
