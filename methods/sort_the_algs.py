
def sort_the_algs(algs):

    YorZ_turns = ["Y", "Z"]
    udbf_turns = ["u", "d", "b", "f"]


    # this is called from within the sort below. Even though I don't obviously iterate through the algs, the 
    # sort method does look at each alg, and calls this method
    def calculate_alg_length(alg):
        compacted_alg = alg.replace("'", "").replace("2", "").replace(" ", "").replace("Y","").replace("Z","")
        alg_length = len(compacted_alg)
       
        return alg_length





    # The following method contains a block of 8 comma-separarted sort criteria. Order matters
    # The first one, for S algs, will divide all the algs into 2 groups (with and without S algs)
    # After this division, many of the remaining criteria are mutually exclusive, so the effect within each of the two 
    # subdivisions (with and without S algs) should be to divide the algs neatly into the categories specified by 
    # the criteria




    sorted_algs = sorted(algs, key=lambda alg: (
        "S" not in alg,  # Yes, this was successful in getting ALL non-S algs at the top
        not any(turn in alg for turn in YorZ_turns) and not any(turn in alg for turn in udbf_turns), # alg has neither  Y,Z  nor  u,d,b,f. The only algs like this will be in the subdivision that includes S turns. They will rise to the top of that subdivision
        
        alg[0] in YorZ_turns,
        alg[len(alg)-1] == "Y" or alg[len(alg)-2] == "Y" or alg[len(alg)-1] == "Z" or alg[len(alg)-2] == "Z",   # Trailiing YorZ.  Sloppy, but this should cover an alg that ends in Y,Y', Y2, Z, Z' or Z2.  (-1  and -2  because Y could be the last OR second-to-last character)
        any(turn in alg for turn in YorZ_turns), # internal YorZ
        
        alg[0] in udbf_turns,
        alg[len(alg)-1] == "u" or alg[len(alg)-2] == "u" or alg[len(alg)-1] == "d" or alg[len(alg)-2] == "d" or alg[len(alg)-1] == "b" or alg[len(alg)-2] == "b" or alg[len(alg)-1] == "f" or alg[len(alg)-2] == "f",  # Trailiing udbf.  Ooof! 
        any(turn in alg for turn in udbf_turns), # The built-in 'any' function is used to check whether any members of a list are included in a given string

        "T" not in alg,
        "T'" not in alg,
        "D" not in alg,

        calculate_alg_length(alg)

        ), reverse = True)

    return sorted_algs