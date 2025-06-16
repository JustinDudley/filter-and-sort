
# Note:  Slice comps should never come into play. Alg-slice-and-widen has already removed them


def contains_tri_turn__UD_FB_rl(alg):   
    
    for extra in [" ", "2", "'"]:
        alg = alg.replace(extra, "")
    



    # All tri-turns in Y and Z axes -- Add them to the "to-trash" list no matter what ANY booleans say
    for pair in ["UU", "DD", "FF", "BB", "UD", "DU", "FB", "BF"]:     
        if alg.upper().find(pair) >= 0:
            return True


    # rl and lr pairs -- Add them to the "to-trash" list no matter what ANY booleans say.  These are not allowed, even if RL, Rl, etc. ARE allowed
    for rl_pair in ["rl", "lr"]:  
        if alg.find(rl_pair) >= 0:
            return True


    return False