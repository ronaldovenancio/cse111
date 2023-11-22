"""
Verify that the make_full_name, extract_family_name,
and extract_given_name functions work correctly.
"""

from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest


def test_make_full_name():
    assert make_full_name("Marie", "Toussaint") == "Toussaint;Marie"
    assert make_full_name("George", "Washington") == "Washington;George"
    assert make_full_name("Olivier", "Toussaint-Smith") == "Toussaint-Smith;Olivier"
    assert make_full_name("Martha", "Washington-Smith") == "Washington-Smith;Martha"
    assert make_full_name("Ava", "Smith-Jones") == "Smith-Jones;Ava"
    assert make_full_name("James", "Madison") == "Madison;James"
    assert make_full_name("J", "Ng") == "Ng;J"
    assert make_full_name("","") == ";"


def test_extract_family_name():
     """Verify that the test_extract_family_name function works correctly.
     Parameters: none
     Return: nothing
     """
     assert extract_family_name("Smith-Jones; Ava") == "Smith-Jones"
     assert extract_family_name("Madison; James") == "Madison"
     assert extract_family_name("Ng; J") == "Ng"
     assert extract_family_name("; ") == ""



def test_extract_given_name():
     """Verify that the test_extract_given_name function works correctly.
     Parameters: none
     Return: nothing
     """
     assert extract_given_name("Smith-Jones; Ava") == "Ava"
     assert extract_given_name("Madison; James") == "James"
     assert extract_given_name("Ng; J") == "J"
     assert extract_given_name("; ") == ""














# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])