
# Note:  Slice comps should never come into play. Alg-slice-and-widen has already removed them


def contains_RL_tri_turn_AND_Leading_X(alg, is_RL_forbidden_for_Leading_X_algs):   
    
    for extra in [" ", "2", "'"]:
        alg = alg.replace(extra, "")

    
    
    if is_RL_forbidden_for_Leading_X_algs:              # condition 1: if RL/Leading_X combo is forbidden
        if alg[0] == "X":                               # condition 2: if alg has a Leading_X
            for X_pair in ["RR", "LL", "RL", "LR"]:     
                if alg.upper().find(X_pair) >= 0:       # condition 3: if alg has a tri-turn in the X-axis (RL, rL, R'l'...)
                    return True  
    

    # the method defaults to a return of False (or, "it's all okay, don't add anything to the bad list") if no code blocks above return True which would exit the method before getting to here
    return False