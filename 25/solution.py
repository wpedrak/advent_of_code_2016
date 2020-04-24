IP = '_IP'
OUT = 'out'


def get_lines(filename='input'):
    input_file = open(f'{filename}.txt', 'r')
    return [line.rstrip("\n") for line in input_file.readlines()]


def get_program():
    return [parse_line(line) for line in get_lines()]


def parse_line(line):
    splited = line.split()
    name = splited[0]
    args = []
    for arg in splited[1:]:
        parsed_arg = int(arg) if arg.lstrip('-').isnumeric() else arg
        args.append(parsed_arg)

    return name, args


def evaluate(env, arg):
    if arg in env:
        return env[arg]

    return arg


def cpy(env, arg1_raw, arg2):
    arg1 = evaluate(env, arg1_raw)
    env[arg2] = arg1
    env[IP] += 1


def inc(env, arg1):
    env[arg1] += 1
    env[IP] += 1


def dec(env, arg1):
    env[arg1] -= 1
    env[IP] += 1


def jnz(env, arg1_raw, arg2_raw):
    arg1 = evaluate(env, arg1_raw)
    arg2 = evaluate(env, arg2_raw)

    if arg1 != 0:
        env[IP] += arg2
        return

    env[IP] += 1


def out(env, arg1_raw):
    arg1 = evaluate(env, arg1_raw)
    env[OUT].append(arg1)
    env[IP] += 1


def run(instructions, program, env):
    while 0 <= env[IP] < len(program):
        instruction_pointer = env[IP]
        print_env(env)
        name, args = program[instruction_pointer]
        instruction = instructions[name]
        instruction(env, *args)
        if len(env[OUT]) == 8:
            return env[OUT]


def print_env(env):
    friendly_env = list(sorted(env.items()))
    print(friendly_env)


def fresh_env(initial_value):
    env = {x: 0 for x in 'abcd'}
    env['a'] = initial_value
    env[IP] = 0
    env[OUT] = []

    return env


def check_input():
    time = 1
    magic_number = 362 * 7
    while True:
        number = magic_number + time
        string_repr = ''.join(reversed(f'{number:b}'))
        if string_repr == '01' * (len(string_repr) // 2):
            return time

        time += 1


instructions = {
    'cpy': cpy,
    'inc': inc,
    'dec': dec,
    'jnz': jnz,
    'out': out
}

# program = get_program()
result = check_input()
print(result)
