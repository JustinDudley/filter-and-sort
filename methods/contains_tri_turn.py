
# Note:  Slice comps should never come into play. Alg-slice-and-widen has already removed them


def contains_tri_turn(alg, is_RL_allowed):   
    
    for extra in [" ", "2", "'"]:
        alg = alg.replace(extra, "")
    




    # All tri-turns in Y and Z axes -- Add them to the "bad" list no matter what
    for bad_pattern in ["UU", "DD", "FF", "BB", "UD", "DU", "FB", "BF"]:     
        if alg.upper().find(bad_pattern) >= 0:
            return True
    

    # All tri-turns in X axis -- Add them to the "bad" list IF the boolean is set that way
    if not is_RL_allowed:
        for bad_pattern in ["RR", "LL", "RL", "LR"]:     
            if alg.upper().find(bad_pattern) >= 0:
                return True  
    

    # Yeah, we're not allowing EVERY X-axis tri-turn, even if the boolean says we are! -- Add rl and lr to the "bad" list too! (If the boolean says RL is not allowed at all, rl and lr will have been added to bad list already, along with all RR, LL, RL, LR, in the code block directly above)
    if is_RL_allowed:
        for bad_pattern in ["rl", "lr"]:  
            if alg.find(bad_pattern) >= 0:
                return True



    return False