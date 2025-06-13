
YorZ_turns = ["Y", "Z"]
XorYorZ_turns = ["X", "Y", "Z"]
udbf_turns = ["u", "d", "b", "f"]



def get_length_without_WCRs(alg):
    for uncounted in [" ", "2", "'", "X", "Y", "Z"]:
        alg = alg.replace(uncounted, "")
    return len(alg)


def does_alg_have_leading_X(alg):
    if alg[0] == "X":
        return True
    return False


def does_alg_contain_rL(alg):
    for extra in [" ", "2", "'"]:
        alg = alg.replace(extra, "")
    for X_axis_pair in ["RR", "LL", "RL", "LR"]:     
        if alg.upper().find(X_axis_pair) >= 0:
            return True 
    return False


def does_alg_contain_T(alg):
    if "T" in alg:
        return True
    return False


def does_alg_contain_S(alg):
    if "S" in alg:
        return True
    return False




def final_letter(alg):
    index_final_whitespace = alg.rfind(" ")
    return alg[index_final_whitespace + 1]


def first_letter_other_than_X(alg):
    if "X" in alg:
        alg = " ".join(alg.split()[1:-1])  # the substring beginning after the first whitespace and going to the end of the alg
    return alg[0]


def does_alg_contain_internal_YorZ(alg):
    for WCR in YorZ_turns:
        if WCR in alg:
            if not first_letter_other_than_X(alg) == WCR and not final_letter(alg) == WCR:
                return True
    return False


def does_alg_contain_internal_udfb(alg):
    for turn in udbf_turns:
        if turn in alg:
            if not first_letter_other_than_X(alg) == turn and not final_letter(alg) == turn:
                return True
    return False





def create_alg_dict(alg, isCornerAlg):
    alg_dict = {
        "alg": alg,
        "isCornerAlg": isCornerAlg,
        "isEdgeAlg": not isCornerAlg,
        "alg_length": get_length_without_WCRs(alg),
        "alg_has_leading_X" : does_alg_have_leading_X(alg),
        "alg_contains_rL": does_alg_contain_rL(alg),
        "alg_contains_T": does_alg_contain_T(alg),
        "alg_contains_S": does_alg_contain_S(alg),
        "alg_contains_internal_YorZ": does_alg_contain_internal_YorZ(alg),
        "alg_contains_internal_udfb": does_alg_contain_internal_udfb(alg),
    }

    return alg_dict
