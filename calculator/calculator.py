#!/usr/bin/env python3


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def modulo(a, b):
    if b == 0:
        raise ValueError("Cannot modulo by zero.")
    return a % b


def power(a, b):
    return a ** b


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": modulo,
    "**": power,
}


def parse_number(s: str) -> float:
    try:
        return float(s)
    except ValueError:
        raise ValueError(f"'{s}' is not a valid number.")


def print_help():
    print("""
Calculator Commands:
  <num> <op> <num>   Perform a calculation
  Supported ops: + - * / % **
  history            Show calculation history
  clear              Clear history
  help               Show this message
  quit / exit        Exit
""")


def format_result(value: float) -> str:
    if value == int(value) and abs(value) < 1e15:
        return str(int(value))
    return f"{value:.10g}"


def main():
    history = []
    print("Basic Calculator — type 'help' for commands.")

    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not raw:
            continue

        if raw.lower() in ("quit", "exit"):
            print("Goodbye!")
            break

        if raw.lower() == "help":
            print_help()
            continue

        if raw.lower() == "history":
            if not history:
                print("No calculations yet.")
            else:
                for entry in history:
                    print(f"  {entry}")
            continue

        if raw.lower() == "clear":
            history.clear()
            print("History cleared.")
            continue

        # Parse expression: support two-token ops like **
        parts = raw.split()
        if len(parts) == 3:
            num_a_str, op, num_b_str = parts
        elif len(parts) == 4 and parts[1] == "*" and parts[2] == "*":
            num_a_str, _, _, num_b_str = parts
            op = "**"
        else:
            print("Usage: <number> <operator> <number>  (e.g. 10 + 5)")
            continue

        try:
            a = parse_number(num_a_str)
            b = parse_number(num_b_str)
        except ValueError as e:
            print(f"  Error: {e}")
            continue

        fn = OPERATIONS.get(op)
        if fn is None:
            print(f"  Unknown operator '{op}'. Supported: + - * / % **")
            continue

        try:
            result = fn(a, b)
        except ValueError as e:
            print(f"  Error: {e}")
            continue

        result_str = format_result(result)
        expr = f"{format_result(a)} {op} {format_result(b)} = {result_str}"
        history.append(expr)
        print(f"  = {result_str}")


if __name__ == "__main__":
    main()
