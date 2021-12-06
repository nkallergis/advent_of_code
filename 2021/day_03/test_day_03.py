import pytest
import day_03

@pytest.fixture
def read_example_input() -> list:
    """Read example input data"""
    return(day_03.read_input("example_input.txt"))

def test_example(read_example_input: list) -> bool:
    """Test that input is read properly"""
    assert read_example_input == ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]

def test_part1(read_example_input: list) -> bool:
    """Test solution for example input, part 1"""
    assert day_03.part1(read_example_input) == 198

def test_part2(read_example_input: list) -> bool:
    """Test solution for example input, part 2"""
    assert day_03.part2(read_example_input) == 230