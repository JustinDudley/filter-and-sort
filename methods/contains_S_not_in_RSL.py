
def contains_S_not_in_RSL(alg):     # RSR is great, LSL is okay, LSR and RSL are permitted for now

    alg = alg.upper()
    for extra in [" ", "2", "'"]:
        alg = alg.replace(extra, "")


    #SX, XS, SY, YS, SZ, ZS are trickier because leading and trailing WCR's ARE allowed with S.   (Same for T-turns)
    
    for bad_pattern in ["TS", "ST", "US", "SU", "HS", "SH", "DS", "SD"]:    # LS is okay      # left out FS, SF, BS, SB because their presence would indicate a larger problem, one that I'd like to know about
        if alg.find(bad_pattern) >= 0:
            return True  


    return False
    
   
    # needs testing!!

