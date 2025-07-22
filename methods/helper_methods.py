
import copy
from variables.constants import YorZ_turns, udfb_turns


def get_length_without_WCRs(alg):
    for uncounted in [" ", "2", "'", "X", "Y", "Z"]:
        alg = alg.replace(uncounted, "")
    return len(alg)


def does_alg_have_leading_X(alg):
    if alg[0] == "X":
        return True
    return False


def does_alg_contain_rL(alg):  # still used by SORT
    for extra in [" ", "2", "'"]:
        alg = alg.replace(extra, "")
    for X_axis_pair in ["RR", "LL", "RL", "LR"]:     
        if alg.upper().find(X_axis_pair) >= 0:
            return True 
    return False


def number_of_instances_of_rL(alg):  # used to build alg_dict
    for extra in [" ", "2", "'"]:
        alg = alg.replace(extra, "")
    
    alg_upper_without_rL = copy.deepcopy(alg.upper())
    for X_axis_pair in ["RR", "LL", "RL", "LR"]:
        alg_upper_without_rL = alg_upper_without_rL.replace(X_axis_pair, "")
    number_of_instances = (len(alg) - len(alg_upper_without_rL)) / 2     # each undesirable substring (RR, RL, etc.) has length 2

    return number_of_instances


def number_of_instances_of_S(alg):  # used to build alg_dict
    for extra in [" ", "2", "'"]:
        alg = alg.replace(extra, "")
    alg_without_S = alg.replace("S", "")
    number_of_instances = len(alg) - len(alg_without_S) 
    return number_of_instances


def does_alg_contain_T(alg):
    if "T" in alg:
        return True
    return False


def does_alg_contain_S(alg):
    if "S" in alg:
        return True
    return False


def does_alg_contain_Y_or_Z_somewhere(alg):
    if "Y" in alg or "Z" in alg:
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


def does_alg_contain_internal_X(alg):
    if "X" in alg and not alg[0] == "X":
        return True
    return False


def does_alg_contain_internal_udfb(alg):
    for turn in udfb_turns:
        if turn in alg:
            if not first_letter_other_than_X(alg) == turn and not final_letter(alg) == turn:
                return True
    return False
