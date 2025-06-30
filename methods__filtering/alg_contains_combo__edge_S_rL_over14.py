

def alg_contains_combo__edge_S_rL_over14(alg_dict):


    if alg_dict["isEdgeAlg"]:
        if alg_dict["alg_contains_S"]:
            if alg_dict["number_of_instances_of_rL"] > 0:
                if alg_dict["alg_length"] > 14:
                    return True


    return False