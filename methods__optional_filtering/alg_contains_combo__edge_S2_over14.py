

def alg_contains_combo__edge_S2_over14(alg_dict):

    if alg_dict["isEdgeAlg"]:
        if alg_dict["number_of_instances_of_S"] > 1:
            if alg_dict["alg_length"] > 14:
                return True


    return False