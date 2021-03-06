import pytest

from tilpy import Til


class ParentType:
    pass


class ChildType(ParentType):
    pass


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


def test_child_types_are_fine():
    child_element = ChildType()
    assert child_element in Til(ParentType(), child_element, ParentType())


def test_child_types_may_be_fine_but_parent_types_arent():
    with pytest.raises(TypeError):
        Til(ParentType(), element_type=ChildType)


def test_the_type_of_the_list_can_be_set_explicitly():
    with pytest.raises(TypeError):
        Til("three", element_type=int)


def test_empty_lists_must_have_a_type():
    with pytest.raises(SyntaxError):
        Til()


def test_new_elements_are_type_checked():
    start = Til(3)
    with pytest.raises(TypeError):
        start.append("steve")


def test_tils_are_iterable():
    assert [x for x in Til(1, 2, 4)] == [1, 2, 4]


def test_tils_are_containers():
    assert 2 in Til(1, 2, 4)


def test_tils_have_a_length():
    assert len(Til(2, 7, 8)) == 3


def test_tils_are_reversible():
    assert reversed(Til(2, 7, 8)) == Til(8, 7, 2)
