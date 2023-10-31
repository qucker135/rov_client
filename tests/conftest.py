import pytest
from src.model import Model


@pytest.fixture
def model_data1():
    return [
        [' ', ' ', ' ', ' ', ' ', 'o', 'o', 'o', ' ', 'x'],
        [' ', ' ', ' ', ' ', ' ', ' ', 'o', ' ', ' ', ' '],
        [' ', 'o', ' ', ' ', ' ', 'o', ' ', 'o', ' ', ' '],
        [' ', ' ', ' ', 'o', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', 'o', ' ', ' ', ' ', ' ', 'o', ' ', 'o', 'o'],
        [' ', ' ', ' ', ' ', ' ', ' ', 'o', 'o', 'o', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'o', 'o', 'o'],
        [' ', ' ', ' ', ' ', ' ', 'o', ' ', 'o', 'o', ' '],
        ['o', 'o', ' ', ' ', ' ', ' ', ' ', ' ', 'o', 'o'],
        ['o', ' ', 'o', 'o', ' ', ' ', 'o', 'r', 'o', ' ']
    ]


@pytest.fixture
def model1(model_data1):
    return Model(model_data1)


@pytest.fixture
def model_data2():
    return [
        [' ', ' ', ' ', ' ', ' ', 'o', 'o', 'o', ' ', 'r'],
        [' ', ' ', ' ', ' ', ' ', ' ', 'o', ' ', ' ', ' '],
        [' ', 'o', ' ', ' ', ' ', 'o', ' ', 'o', ' ', ' '],
        [' ', ' ', ' ', 'o', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', 'o', ' ', ' ', ' ', ' ', 'o', ' ', 'o', 'o'],
        [' ', 'x', ' ', ' ', ' ', ' ', 'o', 'o', 'o', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', 'o', 'o', 'o'],
        [' ', ' ', ' ', ' ', ' ', 'o', ' ', 'o', 'o', ' '],
        ['o', 'o', ' ', ' ', ' ', ' ', ' ', ' ', 'o', 'o'],
        ['o', ' ', 'o', 'o', ' ', ' ', 'o', ' ', 'o', ' ']
    ]
