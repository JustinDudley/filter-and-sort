
def contains_internal_TY_or_ZT(alg):  

    alg = alg.upper()
    for extra in [" ", "2", "'"]:
        alg = alg.replace(extra, "")




    for leading_YorZ_substring in ["YT", "ZT"]:
        if alg.find(leading_YorZ_substring) == 0:
            return False


    for trailing_YorZ_substring in ["TY", "TZ"]:
        if alg.find(trailing_YorZ_substring) >= 0:   # check substring exists. rindex() throws error if substring not there
            if alg.rindex(trailing_YorZ_substring) == len(alg) - 2:   #rindex() gives final index of a given substring
                return False         
            
       

    for internal_YorZ_substring in ["YT", "ZT", "TY", "TZ"]:
        if alg.find(internal_YorZ_substring) >= 0:
            return True
        

    return False
