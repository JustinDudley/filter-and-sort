
from methods.helper_methods import (
    does_alg_contain_S, 
    does_alg_contain_T, 
    does_alg_contain_internal_YorZ, 
    does_alg_contain_internal_udfb, 
    does_alg_contain_rL, 
    does_alg_have_leading_X, 
    get_length_without_WCRs
    )




def create_alg_dict(alg, isCornerAlg):
    alg_dict = {
        "alg": alg,
        "isCornerAlg": isCornerAlg,
        "isEdgeAlg": not isCornerAlg,
        "alg_length": get_length_without_WCRs(alg),
        "alg_has_leading_X" : does_alg_have_leading_X(alg),
        "alg_contains_rL": does_alg_contain_rL(alg),
        "alg_contains_T": does_alg_contain_T(alg),
        "alg_contains_S": does_alg_contain_S(alg),
        "alg_contains_internal_YorZ": does_alg_contain_internal_YorZ(alg),
        "alg_contains_internal_udfb": does_alg_contain_internal_udfb(alg),
    }

    return alg_dict
