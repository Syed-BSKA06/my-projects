# Basic Calculator

A simple command-line calculator that supports arithmetic operations with a running history.

## Usage

```bash
python3 calculator.py
```

## Supported Operations

| Operator | Operation      | Example       |
|----------|----------------|---------------|
| `+`      | Addition       | `10 + 5`      |
| `-`      | Subtraction    | `10 - 5`      |
| `*`      | Multiplication | `10 * 5`      |
| `/`      | Division       | `10 / 5`      |
| `%`      | Modulo         | `10 % 3`      |
| `**`     | Power          | `2 ** 8`      |

## Commands

- `<num> <op> <num>` — perform a calculation
- `history` — show past calculations
- `clear` — clear history
- `help` — show help
- `quit` / `exit` — exit the app

## Example Session

```
Basic Calculator — type 'help' for commands.
> 10 + 5
  = 15
> 2 ** 8
  = 256
> 100 / 3
  = 33.33333333
> history
  10 + 5 = 15
  2 ** 8 = 256
  100 / 3 = 33.33333333
> exit
Goodbye!
```
