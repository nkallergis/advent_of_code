import pytest
import day_02

@pytest.fixture
def read_example_input() -> list:
    """Read example input data"""
    return(day_02.read_input("example_input.txt"))

def test_example(read_example_input: list) -> bool:
    """Test that input is read properly"""
    assert read_example_input == ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

def test_part1(read_example_input: list) -> bool:
    """Test solution for example input, part 1"""
    assert day_02.part1(read_example_input) == 150

def test_part2(read_example_input: list) -> bool:
    """Test solution for example input, part 2"""
    assert day_02.part2(read_example_input) == 900