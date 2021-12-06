#!/usr/bin/env python
from dataclasses import dataclass


def read_input(input: str) -> list:
    """Read input from file"""
    with open(input) as f:
        movements = [line.rstrip() for line in f.readlines()]
    return movements


@dataclass
class Submarine:
    forward: int = 0
    depth: int = 0
    aim: int = 0
    move_with_aim: bool = False

    def move_forward(self, x: int):
        self.forward += x
        if self.move_with_aim:
            self.depth += x * self.aim

    def move_down(self, x: int):
        if not (self.move_with_aim):
            self.depth += x
        else:
            self.aim += x

    def move_up(self, x: int):
        if not (self.move_with_aim):
            self.depth -= x
        else:
            self.aim -= x

    def move(self, command: str):
        command = command.split()
        move_command = getattr(self, "move_" + command[0])
        move_command(int(command[1]))

    def tracepath(self, commands: list, move_with_aim: bool = False) -> dict:
        for command in commands:
            self.move(command)
        position = {"forward": self.forward, "depth": self.depth}
        return position


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
    commands = read_input("day_02/example_input.txt")
    print(f"Part 1: {part1(commands)}")
    print(f"Part 2: {part2(commands)}")
