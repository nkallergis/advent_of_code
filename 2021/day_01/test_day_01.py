import pytest
import day_01


@pytest.fixture
def read_example_input() -> list:
    """Read example input data"""
    return day_01.read_input("example_input.txt")


def test_example(read_example_input: list) -> bool:
    """Test that input is read properly"""
    assert read_example_input == [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def test_part1(read_example_input: list) -> bool:
    """Test solution for example input, part 1"""
    assert day_01.part1(read_example_input) == 7


def test_part2(read_example_input: list) -> bool:
    """Test solution for example input, part 2"""
    assert day_01.part2(read_example_input) == 5
