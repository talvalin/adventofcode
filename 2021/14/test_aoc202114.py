# test_aoc202113.py

import pathlib
import pytest
import aoc202114 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

@pytest.fixture
def actual_data():
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    return aoc.parse(puzzle_input)

def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1[0] == "NNCB"
    assert example1[1] == dict(CH='B',
        HH='N',
        CB='H',
        NH='C',
        HB='C',
        HC='B',
        HN='C',
        NN='C',
        BH='H',
        NC='B',
        NB='B',
        BN='B',
        BB='N',
        BC='B',
        CC='N',
        CN='C',
    )

def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1, 10) == 1588

def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc.part2(example1, 10) == 1588

def test_part2_example1_2(example1):
    """Test part 2 on example input"""
    assert aoc.part2(example1, 40) == 2188189693529

def test_part2_actual_data_10_steps(actual_data):
    """Test part 2 on example input"""
    assert aoc.part2(actual_data, 10) == 3697