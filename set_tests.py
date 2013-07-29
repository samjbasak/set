from set import card, third_card_in_game_set, third_property
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


def test_third_card_in_game_set():
    assert_equal(third_card_in_game_set(card('1GDE'),
        card('2GDE')), card('3GDE'))


def test_third_property_correct():
    assert_equal(third_property('1', '2'), '3')


def test_third_property_error():
    assert_raises(ValueError, third_property, '1', 'G')
