import requests
from .model import Model
from .utils import Direction, State


class Controller:
    def __init__(self) -> None:
        pass

    def get_data(self, model: Model, addr: str) -> None:
        response = requests.get(addr)
        model.set_data(response.json().get("game_state", [[]]))

    def post_command(self, addr: str, dir: Direction) -> State:
        post_body = {
            "action": dir.value
        }
        response = requests.post(addr, json=post_body)
        return State(response.json()["result"])
