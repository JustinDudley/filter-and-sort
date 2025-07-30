
from methods.helper_methods import (
    does_alg_contain_LwithR,
    does_alg_contain_S, 
    does_alg_contain_T,
    does_alg_contain_Y_or_Z_somewhere,
    does_alg_contain_internal_WCR,
    does_alg_contain_internal_X, 
    does_alg_contain_internal_YorZ, 
    does_alg_contain_internal_udfb,
    does_alg_contain_u, 
    does_alg_have_leading_X, 
    get_length_without_WCRs,
    number_of_instances_of_S,
    number_of_instances_of_rL
    )




def create_alg_dict(alg, isCornerAlg):
    alg_dict = {
        "alg": alg,
        "isCornerAlg": isCornerAlg,
        "isEdgeAlg": not isCornerAlg,
        #  7 potentially bad attributes below (in 5 categories, considering that T/S are related, and the internals are related):
        "alg_length": get_length_without_WCRs(alg),
        "alg_has_leading_X" : does_alg_have_leading_X(alg),
        "number_of_instances_of_rL": number_of_instances_of_rL(alg),
        "alg_contains_LwithR": does_alg_contain_LwithR(alg),
        "alg_contains_T": does_alg_contain_T(alg),
        "alg_contains_S": does_alg_contain_S(alg),
        "alg_contains_u": does_alg_contain_u(alg),
        "number_of_instances_of_S": number_of_instances_of_S(alg),
        "alg_contains_internal_X": does_alg_contain_internal_X(alg),
        "alg_contains_internal_YorZ": does_alg_contain_internal_YorZ(alg),
        "alg_contains_internal_WCR": does_alg_contain_internal_WCR(alg),
        "alg_contains_internal_udfb": does_alg_contain_internal_udfb(alg),
        "alg_contains_Y_or_Z_somewhere": does_alg_contain_Y_or_Z_somewhere(alg),
    }

    return alg_dict
