
def alg_contains_combo__edge_internalu_T_over14(alg_dict):

    if alg_dict["isEdgeAlg"]:
        if alg_dict["alg_contains_internal_u"]:
            if alg_dict["alg_contains_T"]:
                if alg_dict["alg_length"] > 14:
                    return True
                

    return False
