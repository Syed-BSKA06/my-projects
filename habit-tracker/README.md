# Habit Tracker

A simple command-line habit tracker written in Python. Track daily habits, mark them as done, and watch your streaks grow.

## Requirements

- Python 3.10+

## Usage

Run the app from the `habit-tracker` directory:

```bash
python habits.py
```

## Commands

| Command | Description |
|---|---|
| `add <habit>` | Add a new habit to track |
| `done <habit>` | Mark a habit as completed for today |
| `list` | Show all habits, whether they're done today, and their current streak |
| `remove <habit>` | Remove a habit and all its history |
| `help` | Show available commands |
| `quit` / `exit` | Exit the app |

## Example Session

```
Habit Tracker — type 'help' for commands.
> add Morning run
Added habit: 'Morning run'
> add Read 30 minutes
Added habit: 'Read 30 minutes'
> done Morning run
Marked 'Morning run' as done for 2026-03-30. Current streak: 1 day(s).
> list

Habit                          Done Today   Streak
----------------------------------------------------
Morning run                    Yes          1 day(s)
Read 30 minutes                No           0 day(s)
```

## Data Storage

Habit data is saved automatically to `habits.json` in the same directory. The file is created on first use.

## Streak Rules

- A streak counts consecutive days a habit was completed.
- A streak is active if the habit was completed today or yesterday.
- Missing a day resets the streak to 0.
