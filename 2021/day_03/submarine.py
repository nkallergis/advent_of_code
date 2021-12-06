#!/usr/bin/env python
from dataclasses import dataclass


@dataclass
class Submarine:
    forward: int = 0
    depth: int = 0
    aim: int = 0

    power_consumption: int = 0
    life_support: int = 0

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

    def read_report(self, diag_report):
        dr = Diagnostics(diag_report)
        self.power_consumption = dr.power_consumption
        self.life_support = dr.life_support


@dataclass
class Diagnostics:
    diag_report: list

    gamma_rate: int = 0
    epsilon_rate: int = 0
    power_consumption: int = 0

    o2_rate: int = 0
    co2_rate: int = 0
    life_support: int = 0

    @staticmethod
    def calc_mf_bit(iterable, position, bit) -> str:
        """Calculates if `bit` is the most frequent value in `position`"""
        bit_count = sum([1 for i in iterable if i[position] == bit])
        if bit_count / len(iterable) == 0.5:
            result = bit
        else:
            result = str(int(round(bit_count / len(iterable))))
        return result

    def calc_rate(self, iterable, bit, life_rate=False) -> int:
        i_copy = iterable.copy()
        d_length = len(iterable[0])
        mf_bits = []

        for position in range(d_length):
            mf_bit = self.calc_mf_bit(i_copy, position, bit)
            if life_rate:
                i_copy = [i for i in i_copy if i[position] == mf_bit]
                if len(i_copy) == 1:
                    rate_binary = i_copy[0]
                    break
            else:
                mf_bits.append(mf_bit)
                rate_binary = "".join(mf_bits)
        result = int(rate_binary, 2)
        return result

    def __post_init__(self):
        self.gamma_rate = self.calc_rate(self.diag_report, "1")
        self.epsilon_rate = self.calc_rate(self.diag_report, "0")
        self.power_consumption = self.gamma_rate * self.epsilon_rate

        self.o2_rate = self.calc_rate(self.diag_report, "1", life_rate=True)
        self.co2_rate = self.calc_rate(self.diag_report, "0", life_rate=True)
        self.life_support = self.o2_rate * self.co2_rate
