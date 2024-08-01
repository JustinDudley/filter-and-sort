
def contains_tri_turn(alg):    # Note:  Slice comps should never come into play. Alg-slice-and-widen has already removed them

    alg = alg.upper()
    for extra in [" ", "2", "'"]:
        alg = alg.replace(extra, "")
    


    for bad_pattern in ["RR", "LL", "UU", "DD", "FF", "BB", "RL", "LR", "UD", "DU", "FB", "BF"]:     # tri-turns
        if alg.find(bad_pattern) >= 0:
            return True
        

    return False