import pytest

from src.keyboard import Keyboard


@pytest.fixture
def kb():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_init1(kb):
    assert str(kb) == "Dark Project KD87A"


def test_init2(kb):
    assert repr(kb) == "Keyboard('Dark Project KD87A', 9600, 5, EN)"


def test_init3(kb):
    assert kb.language == 'EN'


def test_change_lang1(kb):
    kb.change_lang()
    assert str(kb.language) == "RU"


def test_change_lang2(kb):
    kb.change_lang()
    assert str(kb.language) == "EN"


def test_change_lang3(kb):
    with pytest.raises(AttributeError):
        kb.language = 'CH'