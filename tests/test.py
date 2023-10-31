from src.model import Model


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


def test_model_pos_setter1(model1):
    model1.pos = (0, 0)
    assert model1.pos == (0, 0)


def test_model_pos_setter2(model_data2):
    model_local = Model(model_data2)
    model_local.pos = (0, 0)
    assert model_local.pos == (0, 0)
