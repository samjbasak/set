from set import card
from nose.tools import assert_equal, assert_raises

def test_card_works():
    assert_equal(card('1GDE'), ('1', 'G', 'D', 'E'))

def test_card_ordering():
    assert_equal(card('EDG1'), ('1', 'G', 'D', 'E'))

def test_card_invalid_property_rejected():
    assert_raises(ValueError, card, 'XGDE')

def test_card_incorrect_length_rejected():
    assert_raises(ValueError, card, '1GD')

def test_card_two_of_same_property():
    assert_raises(ValueError, card, '1GRE')
