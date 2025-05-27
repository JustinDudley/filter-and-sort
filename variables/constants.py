
# Python doesn't support constants, but by convention UPPERCASE vars are understood to be constants



SOLVED_PATTERN_LETTERS = ["wht", "grn", "red", "blu", "ora", "yel", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x"]


# This app, unlike alg-slice-and-widen, handled FINISHED algs as inputs. The core is already
# rotated, so the edge and corner stickers are in their original positions (except for those that are swapped)
# But the CORNERS are now shifted around, and these are the stickers that indicate the group number

STICKERS_SITTING_IN_CORNER_POSITIONS_ABCDUVWX__ALL_GROUPS = ["A", "B", "C", "D", "U", "V", "W", "X"]


STICKERS_SITTING_IN_CENTER_POSITIONS__GROUP_1 = ["yel", "ora", "blu", "red", "grn", "wht"]
STICKERS_SITTING_IN_CENTER_POSITIONS__GROUP_2 = ["yel", "red", "grn", "ora", "blu", "wht"]
STICKERS_SITTING_IN_CENTER_POSITIONS__GROUP_3 = ["blu", "yel", "ora", "wht", "red", "grn"]
STICKERS_SITTING_IN_CENTER_POSITIONS__GROUP_4 = ["grn", "wht", "ora", "yel", "red", "blu"]
STICKERS_SITTING_IN_CENTER_POSITIONS__GROUP_5 = ["red", "blu", "wht", "grn", "yel", "ora"]
STICKERS_SITTING_IN_CENTER_POSITIONS__GROUP_6 = ["ora", "blu", "yel", "grn", "wht", "red"]




REPLACEMENTS_DICT = {
"2'": "2",
"M ": "T' ",
"M2": "T2",
"M'": "T",
"E ": "H' ",
"E2": "H2",
"E'": "H",
"x": "X",
"y": "Y",
"z": "Z",
"(": " ",
")": " ",
"[": " ",
"]": " "
}


HEADER = {
    "I": "I",
    "X": "X",
    "X2": "X2",
    "X'": "X'",
    "X0": "X0",
    "Y": "Y",
    "Y2": "Y2",
    "Y'": "Y'",
    "Y0": "Y0",
    "Z": "Z",
    "Z2": "Z2",
    "Z'": "Z'",
    "Z0": "Z0",
    "R": "R",
    "R2": "R2",
    "R'": "R'",
    "L": "L",
    "L2": "L2",
    "L'": "L'",
    "T": "T",
    "T2": "T2",
    "T'": "T'",
    "r": "r-lower",
    "r'": "r'-lower",
    "r2": "r2-lower",
    "l": "l-lower",
    "l'": "l'-lower",
    "l2": "l2-lower",
    "RL'": "RL'",
    "R2L2": "R2L2",
    "R'L": "R'L",
    "U": "U",
    "U2": "U2",
    "U'": "U'",
    "D": "D",
    "D2": "D2",
    "D'": "D'",
    "H": "H",
    "H2": "H2",
    "H'": "H'",
    "u": "u-lower",
    "u'": "u'-lower",
    "u2": "u2-lower",
    "d": "d-lower",
    "d'": "d'-lower",
    "d2": "d2-lower",
    "UD'": "UD'",
    "U2D2": "U2D2",
    "U'D": "U'D",
    "F": "F",
    "F2": "F2",
    "F'": "F'",
    "B": "B",
    "B2": "B2",
    "B'": "B'",
    "S": "S",
    "S2": "S2",
    "S'": "S'",
    "f": "f-lower",
    "f'": "f'-lower",
    "f2": "f2-lower",
    "b": "b-lower",
    "b'": "b'-lower",
    "b2": "b2-lower",
    "FB'": "FB'",
    "F2B2": "F2B2",
    "F'B": "F'B"
}

