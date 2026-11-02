def parse_expr(expr):

    # operator priority (higher = stronger)
    prec = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    # operator functions (Search: lambda functions in Python)
    ops_func = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
        '^': lambda a, b: a ** b
    }

    nums = []  # number stack
    ops = []  # operator stack
    i = 0

    def apply():
        """Helper to pop and apply one operator."""
        b, a, op = nums.pop(), nums.pop(), ops.pop()
        nums.append(ops_func[op](a, b))

    while i < len(expr):
        c = expr[i]

        if c.isspace(): # c = ' '
            i += 1
            continue

        if c.isdigit():
            # parse number (multi-digit)
            j = i
            while j < len(expr) and expr[j].isdigit():
                j += 1
            nums.append(int(expr[i:j]))
            i = j
            continue

        if c == '(':
            ops.append(c)
        elif c == ')':
            while ops and ops[-1] != '(':
                apply()
            ops.pop()  # remove '('
        else:  # operator
            while (ops and ops[-1] != '(' and
                    (prec[ops[-1]] > prec[c] or
                    (prec[ops[-1]] == prec[c] and c != '^'))):
                apply()
            ops.append(c)
        i += 1

    # finish remaining
    while ops:
        apply()

    return nums[-1]

tests = [
    "3 + 5",
    "10 + 2 * 6",
    "100 * 2 + 12",
    "100 * ( 2 + 12 )",
    "100 * ( 2 + 12 ) / 14",
    "3 + 5 * (2 ^ 3) - 4 / 2"
]

for test in tests:
    print(f"{test} = {parse_expr(test)}")
    
