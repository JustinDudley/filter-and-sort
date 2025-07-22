
def alg_contains_combo__corner_internalX_over17(alg_dict):

    if alg_dict["isCornerAlg"]:
        if alg_dict["alg_contains_internal_X"]:
            if alg_dict["alg_length"] > 17:
                return True


    return False
