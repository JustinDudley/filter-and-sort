


def is_bad_pattern_when_capitalized(alg):
    alg = alg.upper()
    alg = alg.replace(" ", "")

    alg = alg.replace("2", "")
    alg = alg.replace("'", "")

    print(alg)

    #TX, XT, TY, YT, TZ, Zt are trickier because WCR ARE okay at the beginning or end with a T




    for bad_pattern in ["HT", "TH", "DT", "TD", "FT", "TF", "ST", "TS", "BT", "TB"]:    # left out RT, TR, LT, TL because their presence would indicate a larger problem, one that I'd like to know about
        if alg.find(bad_pattern) >= 0:
            return True
   

    for bad_pattern in ["TS", "ST", "US", "SU", "HS", "SH", "DS", "SD"]:    # LS is okay      # left out FS, SF, BS, SB because their presence would indicate a larger problem, one that I'd like to know about
        if alg.find(bad_pattern) >= 0:
            return True  
   
    for bad_pattern in ["RR", "LL", "UU", "DD", "FF", "BB", "RL", "LR", "UD", "DU", "FB", "BF"]:     # tri-turns
        if alg.find(bad_pattern) >= 0:
            return True
        
    # needs testing!!


    return False
