def check_brackets(expr):
    """Return True if brackets are balanced, else False."""
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in expr:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack

# Example usage
tests = [
    "(a + b) * [c - {d / e}]",
    "(a + b] * c",
    "{[()]}",
    "((())",
    "([)]",
    "][",
]

for expr in tests:
    result = check_brackets(expr)
    print(f"Expression: {expr} -> Balanced: {result}")