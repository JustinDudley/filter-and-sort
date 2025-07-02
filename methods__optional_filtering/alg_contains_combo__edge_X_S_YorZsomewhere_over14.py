

def alg_contains_combo__edge_X_S_YorZsomewhere_over14(alg_dict):

    if alg_dict["isEdgeAlg"]:
        if alg_dict["alg_has_leading_X"]:
            if alg_dict["alg_contains_S"]:
                if alg_dict["alg_contains_Y_or_Z_somewhere"]:
                    if alg_dict["alg_length"] > 14:
                        return True


    return False
