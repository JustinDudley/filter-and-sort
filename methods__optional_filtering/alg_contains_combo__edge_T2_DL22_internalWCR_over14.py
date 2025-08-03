
def alg_contains_combo__edge_T2_DL22_internalWCR_over14(alg_dict):

    if alg_dict["isEdgeAlg"]:
        if alg_dict["number_of_instances_of_T"] >=2:
            if alg_dict["alg_contains_2D_and_2L"]:
                if alg_dict["alg_contains_internal_WCR"]:
                    if alg_dict["alg_length"] > 14:
                        return True

    return False

