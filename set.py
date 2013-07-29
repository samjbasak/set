#!/usr/bin/python3

# Cards are defined with a 4-tuple as follows:
#
# (number, colour, shape, fill)
# number        1, 2 or 3 (1-length strings)
# colour        G - Green
#               R - Red
#               P - Purple
# shape         D - Diamond
#               O - Oval
#               S - Squiggle
# fill          E - Empty
#               H - Hatched
#               F - Filled

CARD_ORDERING = '123GRPDOSEHF'

CARD_PROPERTY_MAP = {'1': 'number', '2': 'number', '3': 'number',
                     'G': 'colour', 'R': 'colour', 'P': 'colour',
                     'D': 'shape', 'O': 'shape', 'S': 'shape',
                     'E': 'fill', 'H': 'fill', 'F': 'fill'}


def card(description):
    if len(description) != 4:
        raise ValueError("Cards must have 4 properties.")
    for x in description:
        if x not in CARD_ORDERING:
            raise ValueError("Card must have valid property")
    if len({CARD_PROPERTY_MAP[x] for x in description}) != 4:
        raise ValueError("Cards must have 4 properties.")
    sorted_description = sorted(
        description,
        key=lambda prop: CARD_ORDERING.index(prop)
    )
    return tuple(sorted_description)


def third_property(first_property, second_property):
    if CARD_PROPERTY_MAP[first_property] != CARD_PROPERTY_MAP[second_property]:
        raise ValueError("Properties must be the same")
    property_type = CARD_PROPERTY_MAP[first_property]
    properties_in_set = set()
    for key, value in CARD_PROPERTY_MAP.items():
        if value == property_type:
            properties_in_set.add(key)
    properties_in_set.remove(first_property)
    properties_in_set.remove(second_property)
    # Difficult to return value when in a set so convert to list
    return list(properties_in_set)[0]


def third_card_in_game_set(first_card, second_card):
    third_card = []
    for i in range(4):
        if first_card[i] == second_card[i]:
            third_card.append(first_card[i])
        else:
            third_card.append(third_property(first_card[i], second_card[i]))
    return  tuple(third_card)
