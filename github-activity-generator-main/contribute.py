#!/usr/bin/env python

import argparse
import os
import random
import subprocess
import sys
from datetime import datetime, timedelta


def run(commands):
    return subprocess.run(commands, check=True)


def message(date, index):
    return f"DEMO Activity #{index} - {date.strftime('%Y-%m-%d %H:%M')}"


def contribution_count():
    roll = random.random()

    if roll < 0.58:
        return random.randint(1, 8)
    elif roll < 0.84:
        return random.randint(9, 20)
    elif roll < 0.96:
        return random.randint(21, 50)
    else:
        return random.randint(51, 100)


def build_schedule(total, days, no_weekends):
    candidates = [
        day
        for day in days
        if not (no_weekends and day.weekday() >= 5)
    ]

    if not candidates:
        return {}, total

    random.shuffle(candidates)

    schedule = {}
    remaining = total

    for day in candidates:
        if remaining <= 0:
            break

        if random.random() < 0.14:
            continue

        count = contribution_count()
        count = min(count, remaining)

        schedule[day] = count
        remaining -= count

    if remaining > 0:
        active_days = list(schedule.keys())

        if not active_days:
            active_days = candidates

        while remaining > 0:
            day = random.choice(active_days)

            current = schedule.get(day, 0)

            if current >= 100:
                available_days = [
                    candidate
                    for candidate in candidates
                    if schedule.get(candidate, 0) < 100
                ]

                if not available_days:
                    return schedule, remaining

                day = random.choice(available_days)
                current = schedule.get(day, 0)

            add = min(
                random.randint(1, min(20, 100 - current)),
                remaining
            )

            schedule[day] = current + add
            remaining -= add

    return schedule, remaining


def contribute(date, index):
    with open("README.md", "a", encoding="utf-8") as file:
        file.write(message(date, index) + "\n\n")

    run(["git", "add", "README.md"])

    run(
        [
            "git",
            "commit",
            "-m",
            message(date, index),
            "--date",
            date.strftime("%Y-%m-%d %H:%M:%S"),
        ]
    )


def arguments(argsval):
    parser = argparse.ArgumentParser(
        description=(
            "Generate an irregular GitHub activity history "
            "for a demo/test repository."
        )
    )

    parser.add_argument(
        "--total_commits",
        type=int,
        default=5000,
        help="Target number of demo commits. Default: 5000.",
    )

    parser.add_argument(
        "--days_before",
        type=int,
        default=365,
        help="Number of days before today. Default: 365.",
    )

    parser.add_argument(
        "--days_after",
        type=int,
        default=0,
        help="Number of days after today. Default: 0.",
    )

    parser.add_argument(
        "--no_weekends",
        action="store_true",
        default=False,
        help="Avoid generating activity on weekends.",
    )

    parser.add_argument(
        "--repository",
        type=str,
        default=None,
        help=(
            "Remote repository URL. This demo script "
            "does not push automatically."
        ),
    )

    parser.add_argument(
        "--user_name",
        type=str,
        default=None,
        help="Git user.name for this repository.",
    )

    parser.add_argument(
        "--user_email",
        type=str,
        default=None,
        help="Git user.email for this repository.",
    )

    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Optional random seed for reproducible demo patterns.",
    )

    return parser.parse_args(argsval)


def main(def_args=sys.argv[1:]):
    args = arguments(def_args)

    if args.total_commits < 1:
        sys.exit("total_commits must be greater than 0")

    if args.days_before < 0:
        sys.exit("days_before must not be negative")

    if args.days_after < 0:
        sys.exit("days_after must not be negative")

    if args.seed is not None:
        random.seed(args.seed)

    current_date = datetime.now()

    directory = (
        "github-activity-demo-"
        + current_date.strftime("%Y-%m-%d-%H-%M-%S")
    )

    os.mkdir(directory)
    os.chdir(directory)

    run(["git", "init", "-b", "main"])

    if args.user_name:
        run(["git", "config", "user.name", args.user_name])

    if args.user_email:
        run(["git", "config", "user.email", args.user_email])

    with open("README.md", "w", encoding="utf-8") as file:
        file.write(
            "# GitHub Activity Generator Demo\n\n"
            "This repository contains generated activity for "
            "testing and demonstration purposes.\n"
        )

    run(["git", "add", "README.md"])

    run(
        [
            "git",
            "commit",
            "-m",
            "Initialize demo repository",
        ]
    )

    start_date = (
        current_date.replace(
            hour=20,
            minute=0,
            second=0,
            microsecond=0,
        )
        - timedelta(days=args.days_before)
    )

    total_days = args.days_before + args.days_after + 1

    days = [
        start_date + timedelta(days=n)
        for n in range(total_days)
    ]

    schedule, remaining = build_schedule(
        args.total_commits,
        days,
        args.no_weekends,
    )

    if remaining > 0:
        sys.exit(
            f"Could not distribute all commits. "
            f"{remaining} commits remained."
        )

    commit_index = 0
    ordered_days = sorted(schedule.keys())

    print()
    print("Generating demo activity...")
    print(f"Target commits: {args.total_commits}")
    print(f"Active days: {len(ordered_days)}")
    print()

    for day in ordered_days:
        daily_count = schedule[day]

        print(
            f"{day.strftime('%Y-%m-%d')} -> "
            f"{daily_count} commits"
        )

        for number in range(daily_count):
            commit_index += 1

            minutes = number * 7

            commit_time = day + timedelta(
                minutes=minutes
            )

            contribute(
                commit_time,
                commit_index,
            )

    print()
    print("=" * 55)
    print("DEMO GENERATION COMPLETED")
    print("=" * 55)
    print(f"Generated commits: {commit_index}")
    print(f"Target commits:    {args.total_commits}")
    print(f"Repository:        {os.getcwd()}")
    print()
    print(
        "This script intentionally does not push the "
        "generated history to a remote repository."
    )
    print("=" * 55)


if __name__ == "__main__":
    main()