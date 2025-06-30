
def alg_contains_combo__corner_X_rL_over17(alg_dict):


    if alg_dict["isCornerAlg"]:
        if alg_dict["number_of_instances_of_rL"] > 0:
            if alg_dict["alg_has_leading_X"]:
                if alg_dict["alg_length"] > 17:
                    return True


    return False
