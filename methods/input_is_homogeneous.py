
from methods.find_pattern import find_pattern

# the alg input list:  Does every alg in the list create the same pattern on the cube?  (This is the normal way to use this app)
# or am I running a test list, or doing something unusual, where the list is heterogeneous, and different algs do different things to the cube?



def input_is_homogeneous(input_algs):
    patterns = list(map(find_pattern, input_algs[:500]))       # Take the first 500 algs in the input list. Map each one to the pattern it creates on the cube. Now we have a list of 500 patterns. 
    if len(list(set(map(tuple,patterns)))) > 1:                # if EVERY alg in the input list creates the same pattern on the cube (which is the normal situation), this value will be 1. If the algs create DIFFERENT patterns, such as the case with my test input file, this number will be greater than 1. This line of code is the familiar <list(set(my_list))> snippet that removes duplicates from a list
        return False
    

    return True
