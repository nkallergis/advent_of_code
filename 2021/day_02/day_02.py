#!/usr/bin/env python
from dataclasses import dataclass
from submarine import Submarine


def read_input(input: str) -> list:
    """Read input from file"""
    with open(input) as f:
        commands = [line.rstrip() for line in f.readlines()]
    return commands


def part1(commands: list) -> int:
    """Returns result for part 1"""
    sub = Submarine()
    last_position = sub.tracepath(commands)
    result = last_position["forward"] * last_position["depth"]
    return result


def part2(commands: list) -> int:
    """Returns result for part 2"""
    sub = Submarine(move_with_aim=True)
    last_position = sub.tracepath(commands)
    result = last_position["forward"] * last_position["depth"]
    return result


if __name__ == "__main__":
    commands = read_input("input.txt")
    print(f"Part 1: {part1(commands)}")
    print(f"Part 2: {part2(commands)}")
