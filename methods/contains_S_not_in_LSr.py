
def contains_S_not_in_LSr(alg):   
    # RSR is great, LSL is okay,   LSR and RSr are no longer permitted

    for extra in [" ", "2", "'"]:
        alg = alg.replace(extra, "")




    # step 1, get rid of unpleasant grip-shifting turns within X-axis, such as RSL
    for bad_pattern in [ "RSr", "RSL", "rSR", "rSl", "LSl", "LSR", "lSL", "lSr"]:
        if alg.find(bad_pattern) >= 0:
            return True  




    # step 2, get rid of turns not even IN X-axis, such as SU (and get rid ot TS)
    # Note: SX, XS, SY, YS, SZ, ZS are trickier because leading and trailing WCR's ARE allowed with S.   (Same for T-turns)
    alg = alg.upper()
    
    for bad_pattern in ["TS", "ST", "US", "SU", "HS", "SH", "DS", "SD"]:    # LS is okay      # left out FS, SF, BS, SB because their presence would indicate a larger problem, one that I'd like to know about
        if alg.find(bad_pattern) >= 0:
            return True  


    return False

