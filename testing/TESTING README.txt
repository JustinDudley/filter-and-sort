TESTING README

Newest material:
The input file is the main test input file. It has all sorts of alg examples designed to trip up the 
app if the app isn't built right. Does it have enough variety to really catch everything?  Probably not. But it's close.

So far I just have a BASELINE output file, for the existing baseline (non-optional) tests. If I add more restrictions to the baseline,
I'll need to change the output file. More importantly, I plan to ADD AN "OPTIONAL" OUTPUT file when I've collected a few optional
restrictions. Honestly, I think if I turn all the optional restrictions to TRUE, for maximum restriction and most trashed algs, that will
be a sufficient test. I don't need to kill myself with 4 or 5 test output files.


I had THOUGHT to put in a HOMOGENEOUS input file too, that is, a real file from edge AU or corners AK or whatever. 
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
