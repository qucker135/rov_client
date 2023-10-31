from typing import Optional


class Model:
    def __init__(self, data: list[list[str]]) -> None:
        self.data = data

    def get_data(self) -> list[list[str]]:
        return self.data

    def set_data(self, data: list[list[str]]) -> None:
        self.data = data

    @property
    def pos(self) -> Optional[tuple[int, int]]:
        for row in self.data:
            for col in row:
                if col == "r":
                    return (self.data.index(row), row.index(col))
        return None

    @pos.setter
    def pos(self, pos: tuple[int, int]) -> None:
        old_pos = self.pos
        self.data[old_pos[0]][old_pos[1]] = " "
        self.data[pos[0]][pos[1]] = "r"
