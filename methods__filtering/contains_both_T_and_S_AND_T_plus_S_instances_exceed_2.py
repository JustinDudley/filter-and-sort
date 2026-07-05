
def contains_both_T_and_S_AND_T_plus_S_instances_exceed_2(alg):  
    
    if alg.find("T") >= 0 and alg.find("S") >= 0:
        if alg.count("T") > 1 or alg.count("S") > 1:
            return True
    
    return False