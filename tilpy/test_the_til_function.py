import pytest

from tilpy import Til, til


def test_comprehension_style_construction():
    assert til(x for x in range(0, 3)) == Til(0, 1, 2)


def test_comprehensions_can_be_used_for_filtering_etc():
    start = Til(1, 2, 3, 4)
    assert til(x for x in start if x != 3) == Til(1, 2, 4)


def test_the_til_function_also_takes_elements():
    assert til(1, 2, 3) == Til(1, 2, 3)


def test_the_til_function_also_passes_on_explicit_typing():
    with pytest.raises(TypeError):
        til(1, 2, 3, element_type=float)
