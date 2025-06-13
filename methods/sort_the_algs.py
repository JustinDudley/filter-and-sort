
import copy


def sort_the_algs(algs):

    YorZ_turns = ["Y", "Z"]
    XorYorZ_turns = ["X", "Y", "Z"]
    udfb_turns = ["u", "d", "f", "b"]


    def calculate_alg_length(alg):
        compacted_alg = alg.replace("'", "").replace("2", "").replace(" ", "").replace("X","").replace("Y","").replace("Z","")
        alg_length = len(compacted_alg)
        return alg_length

    # def second_letter(alg):
    #     substring_following_first_whitespace = " ".join(alg.split()[1:-1])
    #     return substring_following_first_whitespace[0]

    def final_letter(alg):
        index_final_whitespace = alg.rfind(" ")
        return alg[index_final_whitespace + 1]
    
    def first_letter_other_than_X(alg):
        if "X" in alg:
            alg = " ".join(alg.split()[1:-1])  # the substring beginning after the first whitespace and going to the end of the alg
        return alg[0]

    def is_rL_in_alg(alg):
        extra_symbols = ["2", "'", " "]
        for extra_symbol in extra_symbols:
            alg = alg.replace(extra_symbol, "")
        for X_pair in ["RR", "LL", "RL", "LR"]:
            if alg.upper().find(X_pair) >= 0:
                return True
        return False


    # The following method contains a block of many comma-separared sort criteria. Order matters
    # The first one, for S algs, will divide all the algs into 2 groups (with and without S algs)
    # After this division, many of the remaining criteria are mutually exclusive, so the effect within each of the two 
    # subdivisions (with and without S algs) should be to divide the algs neatly into the categories specified by 
    # the criteria



    sorted_algs = sorted(algs, key=lambda alg: (
        "S" not in alg,  # Yes, this was successful in getting ALL non-S algs at the top
        not any(turn in alg for turn in XorYorZ_turns) and not any(turn in alg for turn in udfb_turns), # alg has neither  X,Y,Z  nor  u,d,b,f. The only algs like this will be in the subdivision that includes S turns. They will rise to the top of that subdivision
        

        "Y" in alg or "Z" in alg,  # There are NO algs with members in both YorZ AND udfb (eg. none with both Z and d), so this places ALL YorZ algs above ALL udfb algs


        first_letter_other_than_X(alg) in YorZ_turns or final_letter(alg) in YorZ_turns or first_letter_other_than_X(alg) in udfb_turns or final_letter(alg) in udfb_turns,    # disregarding X:  algs that lead or end with Y or Z, or algs that lead or end with u,d,f,b
        "X" not in alg,
        first_letter_other_than_X(alg) in YorZ_turns or first_letter_other_than_X(alg) in udfb_turns,


        "T" not in alg,
        "T'" not in alg,
        alg.count("T") < 2,  # alg has fewer than 2 instances of T
        "D" not in alg,


        100 - calculate_alg_length(alg),
        not is_rL_in_alg(alg),
        "Y" in alg,  # algs with Y above algs with Z, within each of the smallest divisions


        # final micro-sort, starting with making the u,d,f,b regions cleaner...
        "u" in alg,
        "d" in alg,
        "f" in alg,
        "b" in alg,


        ), reverse = True)

    return sorted_algs