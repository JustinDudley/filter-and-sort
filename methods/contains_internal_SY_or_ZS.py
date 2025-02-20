
def contains_internal_SY_or_ZS(alg):  

    alg = alg.upper()
    for extra in [" ", "2", "'"]:
        alg = alg.replace(extra, "")




    for leading_YorZ_substring in ["YS", "ZS"]:
        if alg.find(leading_YorZ_substring) == 0:   # if True, then alg DOES begin with YS or ZS, so it contains no internal YorZ, and the alg is acceptable
            return False


    for trailing_YorZ_substring in ["SY", "SZ"]:
        if alg.find(trailing_YorZ_substring) >= 0:   # check substring exists. rindex() throws error if substring not there
            if alg.rindex(trailing_YorZ_substring) == len(alg) - 2:   #rindex() gives final index of a given substring
                return False   # if alg ends with SY or SZ, it's acceptable. Remove it from consideration for being filtered out. It doesn't have an INTERNAL SY or SZ.       
            
       

    for internal_YorZ_substring in ["YS", "ZS", "SY", "SZ"]:
        if alg.find(internal_YorZ_substring) >= 0:
            return True
        

    return False
