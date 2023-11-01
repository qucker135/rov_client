import responses
from src.model import Model
from src.utils import Direction, State


def test_model_creation(model_data1):
    model_local = Model(model_data1)
    assert model_local.get_data() == model_data1


def test_model_get_data(model1, model_data1):
    assert model1.get_data() == model_data1


def test_model_set_data(model_data1, model_data2):
    model_local = Model(model_data1)
    model_local.set_data(model_data2)
    assert model_local.get_data() == model_data2


def test_model_pos1(model1):
    assert model1.pos == (9, 7)


def test_model_pos2(model_data2):
    model_local = Model(model_data2)
    assert model_local.pos == (0, 9)


def test_model_pos3(model_data4):
    model_local = Model(model_data4)
    assert model_local.pos is None


def test_model_pos_setter1(model1):
    model1.pos = (0, 0)
    assert model1.pos == (0, 0)


def test_model_pos_setter2(model_data2):
    model_local = Model(model_data2)
    model_local.pos = (0, 0)
    assert model_local.pos == (0, 0)


@responses.activate
def test_controller_get(controller, model1, server_response, server_addr):
    responses.add(
        responses.GET,
        server_addr,
        json=server_response,
        status=200
    )
    controller.get_data(model1, server_addr)
    assert model1.get_data() == server_response["game_state"]


@responses.activate
def test_controller_post1(controller, server_addr, post_response1):
    responses.add(
        responses.POST,
        server_addr,
        json=post_response1,
        status=200
    )
    assert controller.post_command(server_addr, Direction.UP) == State.SUCCESS


@responses.activate
def test_controller_post2(controller, server_addr, post_response2):
    responses.add(
        responses.POST,
        server_addr,
        json=post_response2,
        status=200
    )
    assert controller.post_command(server_addr, Direction.UP) == State.LOSS


@responses.activate
def test_controller_post3(controller, server_addr, post_response3):
    responses.add(
        responses.POST,
        server_addr,
        json=post_response3,
        status=200
    )
    assert controller.post_command(
        server_addr, Direction.UP
        ) == State.IN_PROGRESS


def test_finder_find_path1(model1, finder):
    assert finder.find_path(model1) == [
        (9, 7), (8, 7), (8, 6), (7, 6),
        (6, 6), (6, 5), (5, 5), (4, 5),
        (3, 5), (3, 6), (3, 7), (3, 8),
        (2, 8), (1, 8), (0, 8), (0, 9)
    ]


def test_finder_find_path2(model_data2, finder):
    model_local = Model(model_data2)
    assert finder.find_path(model_local) == [
        (0, 9), (1, 9), (2, 9), (3, 9),
        (3, 8), (3, 7), (3, 6), (3, 5),
        (4, 5), (5, 5), (5, 4), (5, 3),
        (5, 2), (5, 1)
    ]


def test_finder_find_path3(model_data3, finder):
    model_local = Model(model_data3)
    assert finder.find_path(model_local) == []
