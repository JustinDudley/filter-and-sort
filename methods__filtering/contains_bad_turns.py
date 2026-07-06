
def contains_bad_turns(alg):  

    for turn_letter in ["b2", "f2", "u2", "H", "S2"]:
        if alg.find(turn_letter) >= 0:
            return True
    
    
    return False