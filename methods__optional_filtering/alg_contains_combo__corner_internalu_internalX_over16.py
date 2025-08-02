
def alg_contains_combo__corner_internalu_internalX_over16(alg_dict):

    if alg_dict["isCornerAlg"]:
        if alg_dict["alg_contains_internal_u"]:
            if alg_dict["alg_contains_internal_X"]:
                if alg_dict["alg_length"] > 16:
                    return True
                

    return False

