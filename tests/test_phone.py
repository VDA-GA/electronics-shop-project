import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def phone1():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_repr(phone1):
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str(phone1):
    assert str(phone1) == 'iPhone 14'


def test_number_of_sim_1(phone1):
    assert phone1.number_of_sim == 2


def test_number_of_sim_2(phone1):
    phone1.number_of_sim = 1
    assert phone1.number_of_sim == 1


def test_number_of_sim_invalid_1(phone1):
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0


def test_number_of_sim_invalid_2(phone1):
    with pytest.raises(ValueError):
        phone1.number_of_sim = 1.5


def test_number_of_sim_invalid_3(phone1):
    with pytest.raises(ValueError):
        phone1.number_of_sim = -5


def test_add_1(phone1):
    phone2 = Phone("iPhone 22", 190_000, 3, 4)
    assert phone1 + phone2 == 8


def test_add_2(phone1, item1):
    assert item1 + phone1 == 25


def test_add_3(phone1):
    with pytest.raises(ValueError):
        phone1 + 1000
