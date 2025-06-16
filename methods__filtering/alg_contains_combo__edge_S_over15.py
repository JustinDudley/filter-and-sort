

def alg_contains_combo__edge_S_over15(alg_dict):


    if alg_dict["isEdgeAlg"]:
        if alg_dict["alg_contains_S"]:
            if alg_dict["alg_length"] > 15:
                return True


    return False