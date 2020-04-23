IP = '_IP'


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


def is_register(arg):
    return arg.isalpha()


def cpy(env, arg1_raw, arg2):
    env[IP] += 1
    if not is_register(arg2):
        return
    arg1 = evaluate(env, arg1_raw)
    env[arg2] = arg1


def inc(env, arg1):
    env[IP] += 1
    if not is_register(arg1):
        return
    env[arg1] += 1


def dec(env, arg1):
    env[IP] += 1
    if not is_register(arg1):
        return
    env[arg1] -= 1


def jnz(env, arg1_raw, arg2_raw):
    arg1 = evaluate(env, arg1_raw)
    arg2 = evaluate(env, arg2_raw)

    if arg1 != 0:
        env[IP] += arg2
        return

    env[IP] += 1


def tgl(env, program, arg1_raw):
    arg1 = evaluate(env, arg1_raw)
    target_ip = env[IP] + arg1
    env[IP] += 1

    if not 0 <= target_ip < len(program):
        return

    name, args = program[target_ip]
    toogle = {
        'inc': 'dec',
        'dec': 'inc',
        'tgl': 'inc',
        'jnz': 'cpy',
        'cpy': 'jnz'
    }

    program[target_ip] = (toogle[name], args)

def print_env(env):
    friendly_env = list(sorted(env.items()))
    print(friendly_env)

def run(instructions, program, env):
    while 0 <= env[IP] < len(program):
        instruction_pointer = env[IP]
        name, args = program[instruction_pointer]
        instruction = instructions[name]
        # print_env(env)
        if name == 'tgl':
            print('tgl', env[args[0]])
            print_env(env)
            instruction(env, program, *args)
            continue
        instruction(env, *args)


instructions = {
    'cpy': cpy,
    'inc': inc,
    'dec': dec,
    'jnz': jnz,
    'tgl': tgl
}

program = get_program()
env = {reg: 0 for reg in 'abcd'}
env['a'] = 132
env['b'] = 10
env['c'] = 20
for shift in range(20, 0, -2):
    env[IP] = 16
    tgl(env, program, shift)
    env['a'] *= env['b']
    env['b'] -= 1
    env['c'] -= 2

run(instructions, program, env)
result = env['a']

print(result)
