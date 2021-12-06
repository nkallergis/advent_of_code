#!/usr/bin/env python
from itertools import tee
from more_itertools import sliding_window


def pairwise(iterable: list) -> tuple:
    """s -> (s0,s1), (s1,s2), (s2, s3), ..."""
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def read_input(input: str) -> list:
    """Read input from file"""
    with open(input) as f:
        measurements = [int(x) for x in f.readlines()]
    return measurements


def compare_sliding_window_sums(iterable: list, window_size: int) -> int:
    """Returns how many times the sum of window X is larger than window X-1"""
    sliding_windows = sliding_window(iterable, window_size)
    result = sum([1 for a, b in pairwise(sliding_windows) if sum(b) > sum(a)])
    return result


def part1(measurements: list) -> int:
    """Returns result for part 1"""
    result = compare_sliding_window_sums(measurements, 1)
    return result


def part2(measurements: list) -> int:
    """Returns result for part 2"""
    result = compare_sliding_window_sums(measurements, 3)
    return result


if __name__ == "__main__":
    measurements = read_input("day_01/input.txt")
    print(f"Part 1: {part1(measurements)}")
    print(f"Part 2: {part2(measurements)}")
