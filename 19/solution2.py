class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def append(self, node):
        self.next = node
        node.prev = self

    def remove(self):
        prev_node = self.prev
        next_node = self.next

        prev_node.next = next_node
        next_node.prev = prev_node

        return next_node

    def skip(self, n=1):
        current = self
        while n:
            current = current.next
            n -= 1

        return current

    def get_by_value(self, value):
        if value == self.value:
            return self

        return self.next.get_by_value(value)


def solve(number_of_elves):
    first_elf = build_circle(number_of_elves)
    dist_to_move = (number_of_elves // 2)
    elf = first_elf.skip(n=dist_to_move)

    actions = ['remove', 'remove', 'skip']

    current_action = 1

    while elf != elf.next:
        action = actions[current_action]
        if action == 'remove':
            elf = elf.remove()
        elif action == 'skip':
            elf = elf.skip()
        else:
            raise Exception('Wrong action')

        current_action = (current_action + 1) % len(actions)

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
