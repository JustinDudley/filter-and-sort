
def contains_T_not_in_UTU(alg):  

    # TX, XT, TY, YT, TZ, ZT are trickier because leading and trailing WCR's ARE allowed with T.   (Same for S-turns)
    # So, these cases are covered in a different method
    # I'm leaving out RT, TR, LT, TL below because their presence would indicate a larger problem, one that I'd like to know about
   

    for extra in [" ", "2", "'"]:
        alg = alg.replace(extra, "")

    for bad_pattern in ["uT", "Tu", "DT", "TD", "dT", "Td", "BT", "TB", "bT", "Tb", "FT", "TF", "fT", "Tf", "HT", "TH", "ST", "TS"]:    
        if alg.find(bad_pattern) >= 0:
            return True
    

    return False