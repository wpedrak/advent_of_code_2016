class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def append(self, node):
        self.next = node

    def skip_one(self):
        next_next_node = self.next.next
        self.next = next_next_node
        return next_next_node


def solve(number_of_elves):
    elf = build_circle(number_of_elves)
    while elf != elf.next:
        elf = elf.skip_one()

    return elf.value


def build_circle(size):
    first_node = Node(1)
    previous_node = first_node
    for idx in range(2, size + 1):
        current_node = Node(idx)
        previous_node.append(current_node)
        previous_node = current_node

    previous_node.append(first_node)

    return first_node


number_of_elves = 3017957
result = solve(number_of_elves)

print(result)
