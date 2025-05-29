
import datetime

from methods.pattern_and_group_and_kingdom_finder.find_group_and_kingdom import find_group_and_kingdom
from methods.pattern_and_group_and_kingdom_finder.find_pattern import find_pattern
from methods.sort_the_algs import sort_the_algs
from methods.contains_bad_turns import contains_bad_turns
from methods.contains_both_T_and_S import contains_both_T_and_S
from methods.contains_tri_turn import contains_tri_turn
from methods.contains_T_not_in_UTU import contains_T_not_in_UTU
from methods.contains_S_not_in_LSr import contains_S_not_in_LSr
from methods.contains_internal_TY_or_ZT import contains_internal_TY_or_ZT
from methods.contains_internal_SY_or_ZS import contains_internal_SY_or_ZS
from methods.alg_is_too_long import alg_is_too_long


# The other branch of this repo is fully functional but SLOW. (7 HOURS versus 9 SECONDS)
# The hold up WASN'T in the filtering process. It was in comparing EACH of the 500,000 algs in algs to EACH of the 499,000 algs in bad_algs. Oops.

startTime = datetime.datetime.now()  # to monitor performance of program


# BOOLEANS to be set for EACH RUN
# BOOLEANS to be set for EACH RUN
isAppFilteringByLength = False
edgeAlgMaxLength = 16
edgeAlg_with_S_turns_MaxLength = 15
if isAppFilteringByLength:
      print("\n Warning:  the app IS set to filter by length !!! \n")
# BOOLEANS to be set for EACH RUN
# BOOLEANS to be set for EACH RUN




with open("/Users/justindudley/dev/cube/Alg_Slice_And_Widen_daddy/filter-and-sort/INPUT_file/final_alg_list_input.txt") as file_input:
    algs = file_input.read().splitlines() 




# NOTE:  only the FIRST ALG in the list is checked for isCornerAlg, group_number, and pattern !!!!   In my other app, alg-slice-and-widen, each of the hundreds of algs are identified. But this app here must process hundreds of thousands of algs, so I don't want the performance hit of checking each one.
pattern = find_pattern(algs[0])
group_number, isCornerAlg = find_group_and_kingdom(pattern)   # note destructuring syntax




bad_algs = []
for alg in algs:

    alg = alg.strip()



    if contains_bad_turns(alg):
         bad_algs.append(alg)

    if contains_both_T_and_S(alg):
          bad_algs.append(alg)

    if contains_tri_turn(alg):
          bad_algs.append(alg)

    if contains_T_not_in_UTU(alg):
          bad_algs.append(alg)
    
    if contains_S_not_in_LSr(alg):
          bad_algs.append(alg)
    
    if contains_internal_TY_or_ZT(alg):
          bad_algs.append(alg)

    if contains_internal_SY_or_ZS(alg):
          bad_algs.append(alg)

    if isAppFilteringByLength:
          # can make and pass more booleans if more criteria are desired
          if alg_is_too_long(alg, isCornerAlg, edgeAlgMaxLength, edgeAlg_with_S_turns_MaxLength):
                bad_algs.append(alg)



filtered_algs_set = set(algs).difference(set(bad_algs))  # filtered_algs == everything in algs that isn't in bad_algs
filtered_algs = list(filtered_algs_set)
filtered_algs.sort()  # KEEP -- This alphabetizes the filtered list right before sorting it. This is important because even small changes to the filtering functionality have really weird results on the order of the algs, and without sorting alphabetically here, I keep getting results that, while valid, no longer match my test output file !!
sorted_algs = sort_the_algs(filtered_algs)
       


# WRITE TO FILE:  filtered algs
dt = datetime.datetime.now()
output_filename = '/Users/justindudley/dev/cube/Alg_Slice_And_Widen_daddy/filter-and-sort/OUTPUT_files/%s.txt'%(dt.strftime("%a") + "_" + dt.strftime("%I") + ":" + dt.strftime("%M") + ":" + dt.strftime("%S") + "_output")
with open(output_filename, "x") as output_file:
	for alg in filtered_algs:
		output_file.write(f"{alg}\n")


# WRITE TO FILE:  filtered AND SORTED algs
sorted_output_filename = '/Users/justindudley/dev/cube/Alg_Slice_And_Widen_daddy/filter-and-sort/OUTPUT_files/%s.txt'%(dt.strftime("%a") + "_" + dt.strftime("%I") + ":" + dt.strftime("%M") + ":" + dt.strftime("%S") + "_SORTED_output")
with open(sorted_output_filename, "x") as sorted_output_file:
	for alg in sorted_algs:
		sorted_output_file.write(f"{alg}\n")



print("\ntime elapsed: ", datetime.datetime.now() - startTime, "\n\n")
