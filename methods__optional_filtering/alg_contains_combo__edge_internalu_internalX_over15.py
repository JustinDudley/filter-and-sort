
def alg_contains_combo__edge_internalu_internalX_over15(alg_dict):

    if alg_dict["isEdgeAlg"]:
        if alg_dict["alg_contains_internal_u"]:
            if alg_dict["alg_contains_internal_X"]:
                if alg_dict["alg_length"] > 15:
                    return True
                

    return False
