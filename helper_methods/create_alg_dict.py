

def get_length_without_WCRs(alg):
    for uncounted in [" ", "2", "'", "X", "Y", "Z"]:
        alg = alg.replace(uncounted, "")
    return len(alg)


def does_alg_contain_rL(alg):
    for extra in [" ", "2", "'"]:
        alg = alg.replace(extra, "")
    for X_axis_pair in ["RR", "LL", "RL", "LR"]:     
        if alg.upper().find(X_axis_pair) >= 0:
            return True 
    return False

    



def create_alg_dict(alg):

    alg_length = get_length_without_WCRs(alg)

    # alg_dict = {
    #     "alg": alg,
    #     "alg_length": alg_length
    #     "alg_contains_rL": does_alg_contain_rL(alg)
        
    # }

    # return alg_dict
    return None