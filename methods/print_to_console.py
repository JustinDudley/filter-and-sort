
def print_to_console(algs, isTest):


    known_edge_alg_from_test_input = "R S R' U2 r S' r' U2 r2 S' r2"
    known_corner_alg_from_test_input = "F2 U Z' l F' U' F' l' F' R2 U2 L2 D L F L U2 F2 r2"
    test_input_algs_subset = [known_edge_alg_from_test_input, known_corner_alg_from_test_input]


    # if the variable "algs" is from the test input file, it will include the two algs above. Obviously,
    # the user (me) is running a test. But I've forgotten to set isTest to TRUE. So my results are going to be garbage.
    if set(test_input_algs_subset).issubset(algs) and not isTest:
        print("\n\nYOUR TEST WILL FAIL\n" \
        "YOUR TEST WILL FAIL\n" \
        "YOUR TEST WILL FAIL\n"
        "  --because you haven't set isTest to TRUE\n  --Your results will be garbage\n\n")

    if not set(test_input_algs_subset).issubset(algs) and isTest:
        print("\n\nToo SLOW?  Try turning isTest to FALSE")





