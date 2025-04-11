"""ex03 tests"""

__author__: str = "730656365"

import pytest as pytest
from dictionary import invert


def test_invert_use_case1() -> None:
    """first use test of the invert function"""
    assert invert(({"a": "z", "b": "y", "c": "x"})) == {"z": "a", "y": "b", "x": "c"}


def test_invert_use_case2() -> None:
    """second use test of the invert function"""
    assert invert(({"apple": "cat"})) == {"cat": "apple"}


def test_invert_edge_case() -> None:
    """invert function edge test"""
    with pytest.raises(KeyError):
        my_dictionary = {"kris": "jordan", "michael": "jordan"}
        invert(my_dictionary)


from dictionary import count


def test_count_use_case_1() -> None:
    """first use test of count function"""
    assert count(["cat", "dog", "pig", "dog", "cat"]) == {"cat": 2, "dog": 2, "pig": 1}


def test_count_use_case2() -> None:
    """second use test of count function"""
    assert count(["cat", "cat", "cat", "cat"]) == {"cat": 4}


def test_count_edge_case() -> None:
    """edge test of count function"""
    assert count(["", ""]) == {"": 2}


from dictionary import favorite_color


def test_favorite_color_use_case_1() -> None:
    """first use test of favorite_color function"""
    assert (
        favorite_color({"bob": "green", "mike": "blue", "kim": "red", "bill": "blue"})
        == "blue"
    )


def test_favorite_color_use_case_2() -> None:
    """second use test of favorite_color function"""
    assert favorite_color({"bob": "green", "mike": "blue"}) == "green"


def test_favorite_color_edge_case() -> None:
    """edge test of favorite_color function"""
    assert favorite_color({"bob": "", "mike": ""}) == ""


from dictionary import bin_len


def test_bin_len_use_case_1() -> None:
    """use test 1 of bin len function"""
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_use_case_2() -> None:
    """use test 2 of bin len function"""
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}


def test_bin_len_edge_case() -> None:
    """edge test of bin len function"""
    assert bin_len(["", "", ""]) == {0: {""}}
