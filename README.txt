This program looks at a list of final algs and filters them. For instance, it removes all algs that contain B.


INPUT:  A list of final algs, presumably the output of alg-slice-and-widen
OUTPUT:  A much shorter list with no B, no S2, no T unless surrounded by U, etc.   The algs are also sorted.


2-21-2025:  Added f2 and u2 to the list of unacceptable turns

3-3-2025:  Any alg containing BOTH T and S now gets removed


