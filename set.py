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

def card(description):
    if len(description) != 4:
        raise ValueError("Cards must have 4 properties.")
    sorted_description = sorted(
        description,
        key=lambda prop: CARD_ORDERING.index(prop)
    )
    return tuple(sorted_description)

