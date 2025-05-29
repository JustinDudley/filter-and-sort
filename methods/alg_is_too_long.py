

def alg_is_too_long(alg, isCornerAlg, edgeAlgMaxLength, edgeAlg_with_S_turns_MaxLength):

    # alg length does not include WCR's, that is, any form of X,Y, or Z



    # As of today at least, corner algs are NOT length limited
    if not isCornerAlg:
        uncounted_symbols = ["2", "'", " ", "X", "Y", "Z"]
        for uncounted_symbol in uncounted_symbols:
            alg = alg.replace(uncounted_symbol, "")
        
        
        if len(alg) > edgeAlgMaxLength:
            return True
        
        if "S" in alg and len(alg) > edgeAlg_with_S_turns_MaxLength:
            return True

    

    return False