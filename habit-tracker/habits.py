#!/usr/bin/env python3

import json
import os
from datetime import date, timedelta

DATA_FILE = os.path.join(os.path.dirname(__file__), "habits.json")


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"habits": {}}


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


def calculate_streak(completions: list[str]) -> int:
    if not completions:
        return 0
    dates = sorted(set(completions), reverse=True)
    today = date.today().isoformat()
    yesterday = (date.today() - timedelta(days=1)).isoformat()

    # Streak must include today or yesterday to be active
    if dates[0] not in (today, yesterday):
        return 0

    streak = 1
    for i in range(1, len(dates)):
        expected = (date.fromisoformat(dates[i - 1]) - timedelta(days=1)).isoformat()
        if dates[i] == expected:
            streak += 1
        else:
            break
    return streak


def add_habit(data, name: str):
    if name in data["habits"]:
        print(f"Habit '{name}' already exists.")
        return
    data["habits"][name] = {"completions": []}
    save_data(data)
    print(f"Added habit: '{name}'")


def mark_done(data, name: str):
    if name not in data["habits"]:
        print(f"Habit '{name}' not found.")
        return
    today = date.today().isoformat()
    if today in data["habits"][name]["completions"]:
        print(f"'{name}' already marked done for today.")
        return
    data["habits"][name]["completions"].append(today)
    save_data(data)
    streak = calculate_streak(data["habits"][name]["completions"])
    print(f"Marked '{name}' as done for {today}. Current streak: {streak} day(s).")


def list_habits(data):
    if not data["habits"]:
        print("No habits tracked yet. Use 'add' to create one.")
        return
    today = date.today().isoformat()
    print(f"\n{'Habit':<30} {'Done Today':<12} {'Streak'}")
    print("-" * 52)
    for name, info in data["habits"].items():
        completions = info["completions"]
        done_today = "Yes" if today in completions else "No"
        streak = calculate_streak(completions)
        print(f"{name:<30} {done_today:<12} {streak} day(s)")
    print()


def remove_habit(data, name: str):
    if name not in data["habits"]:
        print(f"Habit '{name}' not found.")
        return
    del data["habits"][name]
    save_data(data)
    print(f"Removed habit: '{name}'")


def print_help():
    print("""
Habit Tracker Commands:
  add <habit>       Add a new habit
  done <habit>      Mark a habit as completed today
  list              Show all habits with streaks
  remove <habit>    Remove a habit
  help              Show this help message
  quit / exit       Exit the app
""")


def main():
    data = load_data()
    print("Habit Tracker — type 'help' for commands.")

    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not raw:
            continue

        parts = raw.split(maxsplit=1)
        cmd = parts[0].lower()
        arg = parts[1] if len(parts) > 1 else ""

        if cmd in ("quit", "exit"):
            print("Goodbye!")
            break
        elif cmd == "add":
            if not arg:
                print("Usage: add <habit name>")
            else:
                add_habit(data, arg)
        elif cmd == "done":
            if not arg:
                print("Usage: done <habit name>")
            else:
                mark_done(data, arg)
        elif cmd == "list":
            list_habits(data)
        elif cmd == "remove":
            if not arg:
                print("Usage: remove <habit name>")
            else:
                remove_habit(data, arg)
        elif cmd == "help":
            print_help()
        else:
            print(f"Unknown command: '{cmd}'. Type 'help' for available commands.")


if __name__ == "__main__":
    main()
