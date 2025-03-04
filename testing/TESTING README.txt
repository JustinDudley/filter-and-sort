TESTING README


################
2-21-2025:  Added f2 and u2 to the list of unacceptable turns
Did not test this nor make any changes to the testing files!! I'm confident the program works, but the testing files are
no longer accurate.
################

################
3-3-2025:  Removed any alg that contains BOTH  T and S.
Tested it.
Again, the six original individual test files are out of date. But the program as a whole has been tested.
AND, I made a new test output file, that goes with the same input file I used the first time. 
The new output file is called "KEEP__test_output_UPDATED_with_f2_u2_removed_and_also_T_with_S_removed"
The new output file, as compared to the old one, can be seen to also remove f2 and T/S.  Unfortunately, the original input
file didn't contain any u2, so that functionality is not reflected in the official test files. But I tested for u2 when
I wrote that code.
################


There is a test_algs file with 180 test algs. There is a folder full of outputs, one for each method.

This has already been done: I tested each method individually (each method filters something undesireable). I ran
the program and got the output file. I put the input and output files in 2 columns of an excel spreadsheet, then used
conditional formatting to find unique values. The main thing is to ensure that each alg that gets filtered out has
been filtered out WITH CAUSE. We don't want to lose valuable algs. (But it's not the end of the world if a few bad algs 
get through).

Then I tested two methods in tandem to make sure nothing weird happened.



test_algs:  Algs that SHOULD SURVIVE THE FILTER are on top. Three algs, "D R D", which will never be filtered out, are 
placed below these good algs to demarcate them from the ones below, which may or may not survive the filtering
