

def special_prohibitions_T_S_rL(alg, isCornerAlg, is_T_rL_length16_notIsCornerAlg_forbidden_when_together, is_S_rL_length15_notIsCornerAlg_forbidden_when_together):
    
    
    # prepare to count alg
    uncounted_symbols = ["2", "'", " ", "X", "Y", "Z"]
    for uncounted_symbol in uncounted_symbols:
        alg = alg.replace(uncounted_symbol, "")   # alg is now easily countable


    # check if alg contains an X-axis tri-turn  (Note alg has been truncated in previous step)
    alg_contains_rL = False
    for X_pair in ["RR", "LL", "RL", "LR"]:
         if alg.upper().find(X_pair) >= 0:
             alg_contains_rL = True





    if not isCornerAlg and is_T_rL_length16_notIsCornerAlg_forbidden_when_together:
        if "T" in alg and alg_contains_rL and len(alg) >= 16:
            return True


    if not isCornerAlg and is_S_rL_length15_notIsCornerAlg_forbidden_when_together:
            if "S" in alg and alg_contains_rL and len(alg) >=15:
                 return True




    return False