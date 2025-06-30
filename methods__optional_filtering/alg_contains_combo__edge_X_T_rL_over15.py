

def alg_contains_combo__edge_X_T_rL_over15(alg_dict):


    if alg_dict["isEdgeAlg"]:
        if alg_dict["alg_has_leading_X"]:
             if alg_dict["alg_contains_T"]:
                if alg_dict["number_of_instances_of_rL"] > 0:
                    if alg_dict["alg_length"] > 15:
                        return True


    return False

   
    
