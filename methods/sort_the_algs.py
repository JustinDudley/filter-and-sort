
from methods.helper_methods import does_alg_contain_rL, final_letter, first_letter_other_than_X, get_length_without_WCRs, number_of_ZY_pairs, number_of_ZY_sandwiches
from variables.constants import YorZ_turns, udfb_turns, XorYorZ_turns


def sort_the_algs(algs):

    # The following method contains a block of many COMMA-SEPARATED sort criteria. Order matters
    # The first one, for S algs, will divide all the algs into 2 groups (with and without S algs)
    # After this division, many of the remaining criteria are mutually exclusive, so the effect within each of the two 
    # subdivisions (with and without S algs) should be to divide the algs neatly into the categories specified by 
    # the criteria


    sorted_algs = sorted(algs, key=lambda alg: (
        "S" not in alg,  # ALL non-S algs at the top
        not any(turn in alg for turn in XorYorZ_turns) and not any(turn in alg for turn in udfb_turns), # alg has neither  X,Y,Z  nor  u,d,b,f. The only algs like this will be in the subdivision that includes S turns. They will rise to the top of that subdivision (and are currently highlighted yellow in my spreadsheet's conditional formatting)
        "Y" in alg or "Z" in alg,  # There are NO algs with members in both YorZ AND udfb (eg. none with both Z and d), so this places ALL YorZ algs above ALL udfb algs


        # The first two lines below separate algs into 3 groups:  Leading Y,Z (& leading udfb),  Trailing Y,Z (& trailing udfb),  Internal Y,Z (& internal udfb)
        first_letter_other_than_X(alg) in YorZ_turns or first_letter_other_than_X(alg) in udfb_turns, 
        final_letter(alg) in YorZ_turns or final_letter(alg) in udfb_turns, 


        # the three TRELLIS criteria go here. These criteria are unique to THIS branch of the app
        # For the Repo_2 spreadsheet doc, putting these criteria here means that within a highlighted color, trellis and near-trellis algs appear at the top regardless of length, leading_X, or anything else.
        number_of_ZY_pairs(alg) == 0,  # the true TRELLIS algs. Nothing but alternating X and non-X turns (except: internal whole-cube-rotations DO muck things up.)
        number_of_ZY_pairs(alg) == 1,  # There exists just one pair such as U F, and other than that the alg is a trellis alg
        number_of_ZY_sandwiches(alg) == 1 and number_of_ZY_pairs == 2,  # There exists one ZYZ or YZY sandwich. For instance, U F U'. The pairs clause is included because overlapping sandwiches such as U F U' F are counted as two sandwiches as currently coded, and we don't want those.


        # for YorZ and for udfb:  Start with non-X algs, then go to leading_X algs
        "X" not in alg,
        alg[0] == "X",

        # will apply only to the leading YorZ area. Want these bad prep moves at the bottom
        "X2 Y" not in alg,  
        "X2 Z" not in alg, 


        "T" not in alg,
        "T'" not in alg,
        alg.count("T") < 2,  # alg has fewer than 2 instances of T


        100 - get_length_without_WCRs(alg),
        not does_alg_contain_rL(alg),


        "L" not in alg and "l" not in alg,
        "D" not in alg,


        # At the low-ish micro-level, list X first, then X' then X2
        "X " in alg,   # X with a space. So, not X' or X2
        "X'" in alg,
        "X2" in alg,


        # final micro-sort, starting with making the u,d,f,b regions cleaner...
        # The following 4 lines are examples of sort criteria that AREN'T identified by labels or conditional formatting in the Excel file
        "b" in alg,
        "f" in alg,
        "d" in alg,
        "u" in alg,


        # Make D and L pretty. Fewest L's first.  Within each L possibility, fewest D first
        100 - (alg.count("L") + alg.count("l")),
        100 - alg.count("D"),
        "Y" in alg,  # algs with Y above algs with Z, within each of the smallest divisions


        ), reverse = True)

    return sorted_algs