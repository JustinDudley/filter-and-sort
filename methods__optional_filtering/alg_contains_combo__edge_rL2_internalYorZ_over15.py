
def alg_contains_combo__edge_rL2_internalYorZ_over15(alg_dict):


    if alg_dict["isEdgeAlg"]:
        if alg_dict["number_of_instances_of_rL"] > 1:
            if alg_dict["alg_contains_internal_YorZ"]:
                if alg_dict["alg_length"] > 15:
                    return True


    return False



