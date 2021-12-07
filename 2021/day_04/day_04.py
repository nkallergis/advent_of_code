#!/usr/bin/env python
from dataclasses import dataclass
from more_itertools import grouper
import numpy as np


def read_input(input: str) -> list:
    """Read input from file"""
    with open(input) as f:
        diagnostics = [line.rstrip() for line in f.readlines()]
    return diagnostics


@dataclass
class Extended_board:
    values_board: list
    marked_board: list
    transpose_board: list

    def mark(self, number):
        for row in range(5):
            for col in range(5):
                if self.values_board[row][col] == number:
                    self.marked_board[row][col] = True
                    self.transpose_board[col][row] = True
                    break
            else:
                continue
            break

    def check(self):
        """Check if board wins"""

        # Check rows
        marked_board = np.array(self.marked_board)
        for row in marked_board:
            if np.product(row):
                return True

        # Check columns
        transpose_board = marked_board.transpose()
        for row in transpose_board:
            if np.product(row):
                return True

    def sum_unmarked(self):
        """Return the sum of unmarked cells"""
        result = 0
        for row in range(5):
            for col in range(5):
                if not self.marked_board[row][col]:
                    result += int(self.values_board[row][col])
        return result


def bingo_parse(bingo_data: str) -> tuple:
    """Parse bingo data into numbers and boards"""
    bingo_numbers = bingo_data[0].split(",")
    bingo_boards = grouper([line.split() for line in bingo_data[1:] if line], 5)
    return bingo_numbers, bingo_boards


def create_extended_boards(bingo_boards: list) -> list:
    """Returns the list of extended boards"""
    extended_boards = []
    for bingo_board in bingo_boards:
        extended_board = Extended_board(
            values_board=bingo_board,
            marked_board=[[False for i in range(5)] for j in range(5)],
            transpose_board=[[False for i in range(5)] for j in range(5)],
        )
        extended_boards.append(extended_board)
    return extended_boards


def bingo_play_round(number: str, extended_boards: list) -> list:
    """Returns the result for this round"""
    result = []
    for extended_board in extended_boards:
        extended_board.mark(number)
        if extended_board.check():
            result.append(extended_board)
    return result


def bingo_play_game(bingo_numbers: list, bingo_boards: list, get_last=False) -> int:
    """Return the ordered list of winning boards"""
    extended_boards = create_extended_boards(bingo_boards)
    
    for number in bingo_numbers:
        winners = bingo_play_round(number, extended_boards)
        if winners:
            if get_last and (len(extended_boards) > 1):
                for winner in winners:
                    extended_boards.remove(winner)
            else:
                result = winners[0].sum_unmarked() * int(number)
                return result
    print(len(extended_boards))


def part1(bingo_input: tuple) -> int:
    """Returns result for part 1"""
    bingo_data = bingo_parse(bingo_input)
    result = bingo_play_game(*bingo_data)
    return result


def part2(bingo_input: list) -> int:
    """Returns result for part 2"""
    bingo_data = bingo_parse(bingo_input)
    result = bingo_play_game(*bingo_data, get_last=True)
    return result


if __name__ == "__main__":
    bingo_input = read_input("input.txt")
    print(f"Part 1: {part1(bingo_input)}")
    print(f"Part 2: {part2(bingo_input)}")
