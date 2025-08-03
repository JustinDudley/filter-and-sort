TESTING README

Newest material:
The input file has all sorts of alg examples designed to trip up the 
app if the app isn't built right. Does it have enough variety to really catch everything?  Probably not. But it's close.

The FIRST test output file is a BASELINE output file, for the existing baseline (non-optional) tests. If I add more restrictions to the baseline,
I'll need to change the output file. 

The SECOND test output file includes optional filters.  Here is how the filter booleans are set for the test. (These are the 
filters I used to generate the 72 repo_2 files which I HOPE will turn out to be the final published files)

****************
this_combo_is_trash__3__corner_X_rL_over17 = True  
this_combo_is_trash__4__edge_rL2_internalYorZ_over15 = True  
this_combo_is_trash__5__edge_X_T_rL_over15 = True    
this_combo_is_trash__6__edge_rL_T_internalYorZ_over15 = True    
this_combo_is_trash__7__edge_S2_over14 = True    
this_combo_is_trash__8__edge_S_WCR_over14 = True    
this_combo_is_trash__9__corner_internalX_over17 = True   
this_combo_is_trash__10__corner_LwithR_over17 = True    
this_combo_is_trash__11__edge_S2_internalX = True    
this_combo_is_trash__12__edge_rL_T_u_internalX_over15 = True    
this_combo_is_trash__13__edge_S_LwithR = True
This_combo_is_trash__15__INTENDED_FOR_NON_BD_TUNNELS__edge_T_internalWCR_over15 = True
This_combo_is_trash__16__INTENDED_FOR_NON_BD_TUNNELS__edge_rL_DL43_internalWCR_over15 = True
this_combo_is_trash__17__corner_internalu_internalX_over16 = True    
This_combo_is_trash__18__INTENDED_FOR_NON_BD_TUNNELS__edge_internalu_internalX_over15 = True
This_combo_is_trash__19__INTENDED_FOR_NON_BD_TUNNELS__edge_internalu_T_over14 = True
This_combo_is_trash__20__INTENDED_FOR_NON_BD_TUNNELS__edge_T2_DL22_internalWCR_over14 = True


this_combo_is_trash__14__INTENDED_FOR_NON_BD_TUNNELS__edge_LwithR_over15 = False   
****************



I had THOUGHT to put in a second, HOMOGENEOUS, input file too. That is, a real file from edge AU or corners AK or whatever. 
I just wanted to test the functionality of the "input_is_homogeneous" boolean.
But:  If something goes haywire there I should know.
If the app starts testing EVERY alg for files of 50,000 algs, it will take minutes instead of seconds.
If the app fails to test every alg for the heterogeneous test input file, the results will be all wrong. Mostly because
(totally because?) the baseline length restrictions for edge algs will be applied haphazardly.



June 16, 2025 Tested each method in BASELINE individually, by commenting out all others. Some spot 
checking involved, but went very well !!!!




#################
The first 180 algs in the heterogeneous input file were chosen carefully to demonstrate that the app could hit its marks. Then there is 
a random assortment of (1) algs I knew would survive filtering, and (2) just a bunch of algs that frankly will probably be 
filtered out immediately because they contain B (and other stuff). Finally, I put in a bunch of leading_X algs with and without 
tri-turns (RL) to test the booleans.





There are 4 DEPRECATED test_output files, each titled for choice of boolean in the --DEPRECATED AND GONE-- MAIN file.
The six original individual test files are out of date. But the program as a whole has been tested.
################



This has already been done: I tested each method individually (each method filters something undesireable). I ran
the program and got the [[now out of date]] output file. I put the input and output files in 2 columns of an excel spreadsheet, then used
conditional formatting to find unique values. The main thing is to ensure that each alg that gets filtered out has
been filtered out WITH CAUSE. We don't want to lose valuable algs. (But it's not the end of the world if a few bad algs 
get through).

Then I tested two methods in tandem to make sure nothing weird happened.
