#!/usr/bin/env python
from dataclasses import dataclass


def read_input(input: str) -> list:
    """Read input from file"""
    with open(input) as f:
        diagnostics = [line.rstrip() for line in f.readlines()]
    return diagnostics


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


def part1(diag_report: list) -> int:
    """Returns result for part 1"""
    diag = Diagnostics(diag_report)
    result = diag.power_consumption
    return result


def part2(diagnostics_report: list) -> int:
    """Returns result for part 2"""
    diag = Diagnostics(diagnostics_report)
    result = diag.life_support
    return result


if __name__ == "__main__":
    # diag_report = read_input("day_03/example_input.txt")
    diag_report = read_input("day_03/input.txt")
    print(f"Part 1: {part1(diag_report)}")
    print(f"Part 2: {part2(diag_report)}")
