

def alg_contains_combo__edge_over16(alg_dict):

    if alg_dict["isEdgeAlg"]:
        if alg_dict["alg_length"] > 16:
            return True


    return False