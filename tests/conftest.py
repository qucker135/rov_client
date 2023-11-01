import pytest
from src.model import Model
from src.controller import Controller
from src.finder import Finder


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


@pytest.fixture
def controller():
    return Controller()


@pytest.fixture
def server_addr():
    return "http://localhost:8000/"


@pytest.fixture
def server_response():
    return {
        "game_state": [
            [" ", "o", " ", "o", " ", " ", " ", " ", "o", "o"],
            ["o", " ", " ", " ", "o", " ", "o", "o", "o", "o"],
            [" ", "o", " ", "x", "o", " ", " ", "o", " ", " "],
            ["o", " ", "r", " ", " ", " ", " ", " ", " ", "o"],
            [" ", " ", " ", "o", " ", " ", " ", " ", " ", " "],
            [" ", "o", "o", " ", " ", " ", "o", " ", " ", " "],
            [" ", " ", "o", " ", " ", " ", "o", "o", "o", " "],
            [" ", "o", " ", " ", " ", " ", " ", " ", "o", " "],
            ["o", " ", "o", " ", " ", " ", "o", " ", " ", " "],
            ["o", "o", " ", " ", " ", " ", " ", " ", " ", " "]
        ]
    }


@pytest.fixture
def post_response1():
    return {
        "result": 1
    }


@pytest.fixture
def post_response2():
    return {
        "result": 2
    }


@pytest.fixture
def post_response3():
    return {
        "result": 3
    }


@pytest.fixture
def finder():
    return Finder()
