

def alg_contains_combo__edge_S_WCR_over14(alg_dict):

    if alg_dict["isEdgeAlg"]:
        if alg_dict["alg_contains_S"]:
            if alg_dict["alg_contains_WCR"]:
                if alg_dict["alg_length"] > 14:
                    return True


    return False
