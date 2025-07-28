
def alg_contains_combo__edge_LwithR_over15(alg_dict):

    if alg_dict["isEdgeAlg"]:
        if alg_dict["alg_contains_LwithR"]:
            if alg_dict["alg_length"] > 15:
                return True


    return False
