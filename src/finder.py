from src.model import Model
import copy


class Finder:
    def __init__(self) -> None:
        pass

    def find_path(self, model: Model) -> list[tuple[int, int]]:
        # backward stage
        rov_pos = model.pos

        data = copy.deepcopy(model.get_data())

        target_pos = None
        for row in data:
            for col in row:
                if col == "x":
                    target_pos = (data.index(row), row.index(col))
                    break

        data[target_pos[0]][target_pos[1]] = 0

        target_dist = 1
        keep_looping = True
        while data[rov_pos[0]][rov_pos[1]] == "r" and keep_looping:
            keep_looping = False
            for i_row, row in enumerate(data):
                for i_col, col in enumerate(row):
                    if (data[i_row][i_col] == ' ' or
                            data[i_row][i_col] == 'r') and (
                            (
                                i_row != 0 and
                                data[i_row - 1][i_col] == target_dist - 1
                            ) or
                            (
                                i_row != len(data) - 1 and
                                data[i_row + 1][i_col] == target_dist - 1
                            ) or
                            (
                                i_col != 0 and
                                data[i_row][i_col - 1] == target_dist - 1
                            ) or
                            (
                                i_col != len(data[i_row]) - 1 and
                                data[i_row][i_col + 1] == target_dist - 1
                            )
                            ):
                        data[i_row][i_col] = target_dist
                        keep_looping = True
            target_dist += 1

        # no path from rov to target
        if not keep_looping:
            return []

        # forward stage
        cur_pos = rov_pos
        path = [rov_pos]
        while cur_pos != target_pos:
            if cur_pos[0] != 0 and \
                    data[cur_pos[0] - 1][cur_pos[1]] == \
                    data[cur_pos[0]][cur_pos[1]] - 1:
                cur_pos = (cur_pos[0] - 1, cur_pos[1])
            elif cur_pos[0] != len(data) - 1 and \
                    data[cur_pos[0] + 1][cur_pos[1]] == \
                    data[cur_pos[0]][cur_pos[1]] - 1:
                cur_pos = (cur_pos[0] + 1, cur_pos[1])
            elif cur_pos[1] != 0 and \
                    data[cur_pos[0]][cur_pos[1] - 1] == \
                    data[cur_pos[0]][cur_pos[1]] - 1:
                cur_pos = (cur_pos[0], cur_pos[1] - 1)
            elif cur_pos[1] != len(data[cur_pos[0]]) - 1 and \
                    data[cur_pos[0]][cur_pos[1] + 1] == \
                    data[cur_pos[0]][cur_pos[1]] - 1:
                cur_pos = (cur_pos[0], cur_pos[1] + 1)
            path.append(cur_pos)
        return path
