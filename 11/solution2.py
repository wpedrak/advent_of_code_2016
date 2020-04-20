from collections import deque
import itertools

UP = 'UP'
DOWN = 'DOWN'


def bfs(start, neighbours):
    target_4th_floor = frozenset([f'{prefix}-{suffix}' for prefix in ['PO', 'TH', 'PR', 'RU', 'CO', 'EL', 'DI'] for suffix in ['G', 'M']])

    visited = set()
    to_visit = deque([start, 'UP'])
    dist = 0

    while len(to_visit) > 1:
        current = to_visit.popleft()

        if current == 'UP':
            to_visit.append('UP')
            dist += 1
            print(dist)
            continue

        if current in visited:
            continue

        visited.add(current)

        floor4 = current[4]

        if floor4 == target_4th_floor:
            return dist

        to_visit += filter(
            lambda n: n not in visited,
            neighbours(current)
        )

    raise Exception('Final state not reached')


def generate_states(state):
    states = []

    for direction in [UP, DOWN]:
        for number_of_items in [1, 2]:
            states += move_elevator(state, number_of_items, direction)

    return list(filter(
        is_valid_state,
        states
    ))


def is_valid_state(state):
    for idx in range(1, 4 + 1):
        floor = state[idx]
        if not is_valid_floor(floor):
            return False

    return True


def is_valid_floor(floor):
    if not have_generator(floor):
        return True

    for item in floor:
        if not is_safe(item, floor):
            return False

    return True


def is_safe(item, floor):
    if is_generator(item):
        return True

    prefix = item[:2]
    matching_generator = f'{prefix}-G'

    return matching_generator in floor


def have_generator(floor):
    return any(map(
        is_generator,
        floor
    ))


def is_generator(item):
    return item[-1] == 'G'


def move_elevator(state, items_number, direction):
    elevator = state[0]
    direction_indicator = 1 if direction == UP else -1
    new_row_idx = elevator + direction_indicator

    if not 0 < new_row_idx < len(state):
        return []

    current_row = state[elevator]
    new_row = state[new_row_idx]

    states = []

    for items in itertools.combinations(current_row, items_number):
        items_in_set = frozenset(items)
        mutable_state = list(state)

        mutable_state[0] = new_row_idx
        mutable_state[elevator] = current_row - items_in_set
        mutable_state[new_row_idx] = new_row | items_in_set

        tupled_state = tuple(mutable_state)
        states.append(tupled_state)

    return states


start_state = (
    1,
    frozenset(['PO-G', 'TH-G', 'TH-M', 'PR-G', 'RU-G', 'RU-M', 'CO-G', 'CO-M', 'EL-G', 'EL-M', 'DI-G', 'DI-M']),
    frozenset(['PO-M', 'PR-M']),
    frozenset(),
    frozenset()
)

result = bfs(start_state, generate_states)
# for state in generate_states(start_state):
#     print(state)

print(result)
