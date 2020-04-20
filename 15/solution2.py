discs = [
    [13, 10],
    [17, 15],
    [19, 17],
    [7, 1],
    [5, 0],
    [3, 1],
    [11, 0]
]

for time, disc in enumerate(discs):
    disc[1] += time + 1

propositions = [0] * int(10**7)

for disc in discs:
    period, shift = disc
    start = period - shift

    for idx in range(start, len(propositions), period):
        propositions[idx] += 1

result = propositions.index(len(discs))
print(result)
