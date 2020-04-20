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


def run(instructions, program, env):
    env[IP] = 0

    while 0 <= env[IP] < len(program):
        instruction_pointer = env[IP]
        name, args = program[instruction_pointer]
        instruction = instructions[name]
        instruction(env, *args)


instructions = {
    'cpy': cpy,
    'inc': inc,
    'dec': dec,
    'jnz': jnz
}

program = get_program()
env = {reg: 0 for reg in 'abcd'}
env['c'] = 1
run(instructions, program, env)
result = env['a']

print(result)
