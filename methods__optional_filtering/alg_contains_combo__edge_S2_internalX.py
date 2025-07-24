
def alg_contains_combo__edge_S2_internalX(alg_dict):

    if alg_dict["isEdgeAlg"]:
        if alg_dict["number_of_instances_of_S"] > 1:
            if alg_dict["alg_contains_internal_X"]:
                return True


    return False
