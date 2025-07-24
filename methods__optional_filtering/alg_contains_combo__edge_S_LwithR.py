
def alg_contains_combo__edge_S_LwithR(alg_dict):

    if alg_dict["isEdgeAlg"]:
        if alg_dict["number_of_instances_of_S"] > 0:
            if alg_dict["alg_contains_LwithR"]:
                return True


    return False
