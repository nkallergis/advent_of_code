#!/usr/bin/env python
from dataclasses import dataclass


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

