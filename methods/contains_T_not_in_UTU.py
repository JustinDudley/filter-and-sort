
def contains_T_not_in_UTU(alg):


    alg = alg.upper()
    for extra in [" ", "2", "'"]:
        alg = alg.replace(extra, "")


    #TX, XT, TY, YT, TZ, ZT are trickier because leading and trailing WCR's ARE allowed with T.   (Same for S-turns)

    for bad_pattern in ["HT", "TH", "DT", "TD", "FT", "TF", "ST", "TS", "BT", "TB"]:    # left out RT, TR, LT, TL because their presence would indicate a larger problem, one that I'd like to know about
        if alg.find(bad_pattern) >= 0:
            return True
    

    return False