
from methods.helper_methods import does_alg_contain_rL, final_letter, first_letter_other_than_X, get_length_without_WCRs
from variables.constants import YorZ_turns, udfb_turns, XorYorZ_turns


def sort_the_algs(algs):

    # The following method contains a block of many COMMA-SEPARATED sort criteria. Order matters
    # The first one, for S algs, will divide all the algs into 2 groups (with and without S algs)
    # After this division, many of the remaining criteria are mutually exclusive, so the effect within each of the two 
    # subdivisions (with and without S algs) should be to divide the algs neatly into the categories specified by 
    # the criteria


    sorted_algs = sorted(algs, key=lambda alg: (
        "S" not in alg,  # ALL non-S algs at the top
        not any(turn in alg for turn in XorYorZ_turns) and not any(turn in alg for turn in udfb_turns), # alg has neither  X,Y,Z  nor  u,d,b,f. The only algs like this will be in the subdivision that includes S turns. They will rise to the top of that subdivision
        "Y" in alg or "Z" in alg,  # There are NO algs with members in both YorZ AND udfb (eg. none with both Z and d), so this places ALL YorZ algs above ALL udfb algs


        # The first two lines below separate algs into 3 groups:  Leading Y,Z (udfb),  Trailing Y,Z (udfb),  Internal Y,Z (udfb)
        first_letter_other_than_X(alg) in YorZ_turns or first_letter_other_than_X(alg) in udfb_turns, 
        final_letter(alg) in YorZ_turns or final_letter(alg) in udfb_turns, 
        "X" not in alg,     # For each of the 3 groups created above: Move leading_X algs to bottom
        "X2" not in alg,    # Orders the leading_X algs:  X, X', X2


        "T" not in alg,
        "T'" not in alg,
        alg.count("T") < 2,  # alg has fewer than 2 instances of T
        "D" not in alg,


        100 - get_length_without_WCRs(alg),
        not does_alg_contain_rL(alg),
        "Y" in alg,  # algs with Y above algs with Z, within each of the smallest divisions


        # final micro-sort, starting with making the u,d,f,b regions cleaner...
        # The following 4 lines, along with "Y in alg" above, are the only sort criteria that AREN'T identified by labels or conditional formatting in the Excel file
        "u" in alg,
        "d" in alg,
        "f" in alg,
        "b" in alg,


        ), reverse = True)

    return sorted_algs