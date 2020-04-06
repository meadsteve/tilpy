import pytest

from tilpy import Til


def test_construction_from_numbers():
    assert Til(2, 7, 8) == Til(2, 7, 8)


def test_conversion_to_list():
    assert Til(2, 7, 8).as_list() == [2, 7, 8]


def test_adding_elements_is_immutable():
    start = Til(3)
    end = start.append(5).append(7)
    assert start == Til(3)
    assert end == Til(3, 5, 7)


def test_the_lists_are_homogenous():
    with pytest.raises(TypeError):
        Til(1, 2, "three")


def test_the_type_of_the_list_can_be_set_explicitly():
    with pytest.raises(TypeError):
        Til("three", element_type=int)


def test_new_elements_are_type_checked():
    start = Til(3)
    with pytest.raises(TypeError):
        start.append("steve")


def test_tils_are_iterable():
    assert [x for x in Til(1, 2, 4)] == [1, 2, 4]


def test_tils_are_containers():
    assert 2 in Til(1, 2, 4)
