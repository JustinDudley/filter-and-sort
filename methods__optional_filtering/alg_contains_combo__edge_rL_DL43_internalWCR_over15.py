
def alg_contains_combo__edge_rL_DL43_internalWCR_over15(alg_dict):

    if alg_dict["isEdgeAlg"]:
        if alg_dict["number_of_instances_of_rL"] > 0:
            if alg_dict["alg_contains_4D_and_3L_OR_3D_and_4L"]:
                if alg_dict["alg_contains_internal_WCR"]:
                    if alg_dict["alg_length"] > 15:
                        return True

    return False

