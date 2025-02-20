# with some trepidation, I begin a third project
# I know that "doing things the right way" is best, but at least for a moment, I'm going to forge ahead
# and try to get this job done!
# It would be great to go ahead and develop all my "bad factors" ideas. But I'm just not sure it's necessary.



# could probably filter out any algs that have both a T AND and S...



# ADD SORTING
# Leading YorZ at top
# Next, trailing YorZ
# Next, algs containing u, d, f, or b [these should have no YorZ, right?]
# Next, everything else [meaning no u,d,f,b, and contains internal YorZ]
# SEE PYDROID. I wrote a quick sorting program there.



# Sorting:  Can put L,l at bottom, can put D at bottom
# Internal YorZ should be WAY at bottom
# sort in this order:  leading YorZ, trailing YorZ, contains, udfb, all others.  These SHOULD be all distinct groups.
# Before sorting into the 4 groups:  Sort them by length-without-WCR. Then this length sorting should be preserved when
#    I sort into the 4 groups



# Presumably I will be sorting in addition to filtering.
# LOOK FOR INVERSES (of EACH output alg) in this app too!!!!!!!



import datetime

from methods.contains_bad_turns import contains_bad_turns
from methods.contains_tri_turn import contains_tri_turn
from methods.contains_T_not_in_UTU import contains_T_not_in_UTU
from methods.contains_S_not_in_RSL import contains_S_not_in_RSL
from methods.contains_internal_TY_or_ZT import contains_internal_TY_or_ZT
from methods.contains_internal_SY_or_ZS import contains_internal_SY_or_ZS

startTime = datetime.datetime.now()  # to monitor performance of program


with open("/Users/justindudley/dev/cube/Alg_Slice_And_Widen_daddy/filter-and-sort/INPUT_file/final_alg_list_input.txt") as file_input:
    algs = file_input.read().splitlines() 



bad_algs = []
for alg in algs:

    alg = alg.strip()



    if contains_bad_turns(alg):
         bad_algs.append(alg)
      
    if contains_tri_turn(alg):
          bad_algs.append(alg)

    if contains_T_not_in_UTU(alg):
          bad_algs.append(alg)
    
    if contains_S_not_in_RSL(alg):
          bad_algs.append(alg)
    
    if contains_internal_TY_or_ZT(alg):
          bad_algs.append(alg)

    if contains_internal_SY_or_ZS(alg):
          bad_algs.append(alg)




print("\n\n\n")
filtered_algs = []
for alg in algs:
       if alg not in bad_algs:
              filtered_algs.append(alg)


       

# WRITE TO FILE
dt = datetime.datetime.now()
output_filename = '/Users/justindudley/dev/cube/Alg_Slice_And_Widen_daddy/filter-and-sort/OUTPUT_files/%s.txt'%(dt.strftime("%a") + "_" + dt.strftime("%I") + ":" + dt.strftime("%M") + ":" + dt.strftime("%S") + "_output")
with open(output_filename, "x") as output_file:
	for alg in filtered_algs:
		output_file.write(f"{alg}\n")



print("time elapsed: ", datetime.datetime.now() - startTime)



# Sorting code concept.  Created in Pydroid. 
# algs = ["A B C D u", "Y F B U L R U", "Z C G H J K L","A B C D Y", "Y G F B U L R U", "C G H J K L Z", "A B C D r", "Y F B U L U", "Z C G H J K L J Y"]

# leading_YorZ_algs = []
# trailing_Yorz_algs = []
# udfb_algs = []
# all_other_algs = []
# wide_turns = ["u", "d", "b", "f"]

# def alg_contains_udfb(alg):
# 	for turn in wide_turns:
# 		if turn in alg:
# 			return True
# 	return False
	

# for alg in algs:
# 	if alg[0] == "Y" or alg[0] == "Z":
# 		leading_YorZ_algs.append(alg)
# 	elif alg_contains_udfb(alg):
# 		udfb_algs.append(alg)


# special_algs = leading_YorZ_algs + udfb_algs
# leftover_algs = [i for i in algs if i not in special_algs]


# print(algs)
# print("\n\n")
# print(leading_YorZ_algs )
# print("\n\n")
# print(special_algs)
# print("\n\n")
# print(leftover_algs)




# Or, simpler:
# good = [x for x in mylist if x in goodvals]
# bad = [x for x in mylist if x not in goodvals]

# tested the following briefly, seems to work:
# leading_YorZ = [i for i in algs if i[0] == "Y" or i[0] == "Z"]
# print(leading_YorZ)
# The thing is, the various groups (leading YorZ, trailing YorZ, udfb) SHOULD be mutually independent, so I 
# shouldn't need an if statement. They don't need to progress.
