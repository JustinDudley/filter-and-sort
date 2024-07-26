


def is_bad_pattern_when_capitalized(alg):
    alg = alg.upper()
    alg = alg.replace(" ", "")

    alg = alg.replace("2", "")
    alg = alg.replace("'", "")

    print(alg)

    for bad_pattern in ["RT", "TR", "LT", "TL", "FT", "TF", "ST", "TS", "BT", "TB", "HT", "TH", "DT", "TD"]:
        if alg.find(bad_pattern) >= 0:
            return True
        
        
    # needs testing!!


    return False
