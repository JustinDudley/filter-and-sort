# with some trepidation, I begin a third project
# I know that "doing things the right way" is best, but at least for a moment, I'm going to forge ahead
# and try to get this job done!
# It would be great to go ahead and develop all my "bad factors" ideas. But I'm just not sure it's necessary.



import datetime

from methods.contains_bad_turns import contains_bad_turns
from methods.contains_tri_turn import contains_tri_turn
from methods.contains_T_not_in_UTU import contains_T_not_in_UTU
from methods.contains_S_not_in_RSL import contains_S_not_in_RSL
from methods.contains_internal_TY_or_TZ import contains_internal_TY_or_TZ
from methods.contains_internal_SY_or_SZ import contains_internal_SY_or_SZ

startTime = datetime.datetime.now()  # to monitor performance of program



with open("/Users/justindudley/dev/cube/Alg_Slice_And_Widen_daddy/filter-and-sort/INPUT_file/final_alg_list_input.txt") as file_input:
    algs = file_input.read().splitlines() 


#######
# need to remove Y0 from the 81,000 algs!
# AND reinstate the YorZ at end of alg.
# So basically, I just need to run the program again and paste over the old data! 
#######



# Presumably I will be sorting in addition to filtering.
# I can print to file BEFORE the sorting step if desired, if it helps for testing purposes.


# Sorting:  Can put L,l at bottom, can put D at bottom
# Internal YorZ should be WAY at bottom



bad_algs = []
for alg in algs:

    alg = alg.strip()



    if contains_bad_turns(alg):
         bad_algs.append(alg)

      # I should winnow  down original algs list each time so the program doesn't take so long to run
      # or maybe not. It may be easier to test the program the way it is.
      
    if contains_tri_turn(alg):
          bad_algs.append(alg)

    if contains_T_not_in_UTU(alg):
          bad_algs.append(alg)
    
    if contains_S_not_in_RSL(alg):
          bad_algs.append(alg)
    
    if contains_internal_TY_or_TZ(alg):
          bad_algs.append(alg)

    if contains_internal_SY_or_SZ(alg):
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
