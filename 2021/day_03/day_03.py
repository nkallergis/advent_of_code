#!/usr/bin/env python
from dataclasses import dataclass
from submarine import Submarine


def read_input(input: str) -> list:
    """Read input from file"""
    with open(input) as f:
        diagnostics = [line.rstrip() for line in f.readlines()]
    return diagnostics


def part1(diag_report: list) -> int:
    """Returns result for part 1"""
    sub = Submarine()
    sub.read_report(diag_report)
    result = sub.power_consumption
    return result


def part2(diag_report: list) -> int:
    """Returns result for part 2"""
    sub = Submarine()
    sub.read_report(diag_report)
    result = sub.life_support
    return result


if __name__ == "__main__":
    diag_report = read_input("input.txt")
    print(f"Part 1: {part1(diag_report)}")
    print(f"Part 2: {part2(diag_report)}")
