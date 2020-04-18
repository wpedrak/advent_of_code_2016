from collections import defaultdict


class Bot:
    def __init__(self):
        self.chips = []
        self.low_target = None
        self.high_target = None
        self.id = None

    def add_chip(self, chip):
        self.chips.append(chip)
        self.chips.sort()
        if len(self.chips) > 2:
            raise Exception('Too many chips')

    def set_behaviour(self, low_target, high_target):
        self.low_target = low_target
        self.high_target = high_target

    def set_id(self, id):
        self.id = id

    def is_active(self):
        return len(self.chips) == 2

    def action(self, bot_map, outputs):
        if not self.is_active():
            raise Exception('Action on non active bot')

        low, high = self.chips

        self.give_chip(bot_map, outputs, low, *self.low_target)
        self.give_chip(bot_map, outputs, high, *self.high_target)
        self.chips = []

    def give_chip(self, bot_map, outputs, chip, target_type, target_id):
        if target_type == 'output':
            outputs[target_id] = chip
            return

        if target_type == 'bot':
            bot = bot_map[target_id]
            bot.add_chip(chip)
            return

        raise Exception('Unexpected target_type')


def get_lines(filename='input'):
    input_file = open(f'{filename}.txt', 'r')
    return [line.rstrip("\n") for line in input_file.readlines()]


def get_bots_description():
    starters = []
    behaviour = []

    for line in get_lines():
        splited = line.split()
        if splited[0] == 'bot':
            bot_id, bot_behaviour = parse_behaviour(splited)
            behaviour.append((bot_id, bot_behaviour))
            continue

        if splited[0] == 'value':
            bot_id, chip = parse_starter(splited)
            starters.append((bot_id, chip))
            continue

        raise Exception('Unexpected input')

    return starters, behaviour


def parse_behaviour(behaviour_line):
    bot_id = int(behaviour_line[1])
    low = [behaviour_line[5], int(behaviour_line[6])]
    high = [behaviour_line[10], int(behaviour_line[11])]

    return bot_id, (low, high)


def parse_starter(starter_line):
    bot_id = int(starter_line[5])
    chip = int(starter_line[1])
    return bot_id, chip


def create_bots():
    bots = defaultdict(Bot)
    starters, behaviour = get_bots_description()

    for bot_id, starter_value in starters:
        bot = bots[bot_id]
        bot.add_chip(starter_value)

    for bot_id, bot_behaviour in behaviour:
        bot = bots[bot_id]
        bot.set_id(bot_id)
        bot.set_behaviour(*bot_behaviour)

    return bots


def work(bots_map):
    bots = list(bots_map.values())
    outputs = {}

    while True:
        active_bots = list(filter(lambda b: b.is_active(), bots))

        if not active_bots:
            break

        for bot in active_bots:
            bot.action(bots_map, outputs)

    print(outputs[0] * outputs[1] * outputs[2])

bots = create_bots()
work(bots)
