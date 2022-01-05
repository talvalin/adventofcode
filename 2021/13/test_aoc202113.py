# test_aoc202113.py

import pathlib
import pytest
import aoc202113 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

def test_parse_example1(example1):
    """Test that input is parsed properly"""
    points = set([(9, 10), (6, 12), (2, 14), (9, 0), (8, 4), (3, 4), (10, 4), (0, 13), (0, 3), (8, 10), (3, 0), (6, 10), (10, 12), (6, 0), (1, 10), (4, 11), (0, 14), (4, 1)])
    assert example1[0].difference(points) == set()
    assert example1[1] == [('y',7), ('x',5)]

def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == 17

@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc.part2(example1) == ...