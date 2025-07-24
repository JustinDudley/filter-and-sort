
def alg_contains_combo__edge_rL_T_u_internalX_over15(alg_dict):

    if alg_dict["isEdgeAlg"]:
        if alg_dict["number_of_instances_of_rL"] > 0:
            if alg_dict["alg_contains_T"]:
                 if alg_dict["alg_contains_u"]:
                    if alg_dict["alg_contains_internal_X"]:
                        if alg_dict["alg_length"] > 15:
                            return True


    return False
