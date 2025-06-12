
import datetime

from helper_methods.create_alg_dict import create_alg_dict
from methods.special_prohibitions_T_S_rL import special_prohibitions_T_S_rL
from methods.contains_RL_tri_turn_AND_Leading_X import contains_RL_tri_turn_AND_Leading_X
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


isTest = False
if not isTest:
      print("\n TESTING WILL FAIL. APP IS NOT CHECKING ALGS FOR EDGE vs. CORNER.  TO TEST PROPERLY, TURN isTest BOOLEAN to TRUE\n")
if isTest:
      print("\n app is in testing mode. It checks each alg for edge vs. corner. Not performant\n")
      # Not performant means:  5 minutes versus 10 seconds




#CONFIGURATION BOOLEANS


#    Managing tolerance level for unwieldy algs
# CONFIGURATION    CONFIGURATION    CONFIGURATION  
# CONFIGURATION    CONFIGURATION    CONFIGURATION

is_trash_1__edge_over16 = True

is_RL_forbidden_everywhere = False                    # FALSE should be the default. (RL_turns are tri-turns occuring in the X-axis)
is_RL_forbidden_for_Leading_X_algs = False             # FALSE should be the default.  The "forbidden_everywhere" boolean will override this if "forbidden_everywhere" is set to True. "Forbidden everywhere" paints with a broad stroke in its own method
isAppFilteringByLength = False                         # TRUE should be the default
edgeAlgMaxLength = 16
edgeAlg_with_S_turns_MaxLength = 15



# Specialty prohibitions: 
# THESE ACTUALLY DO WORK FOR EDGE ALGS !!!  
# # And yes, it doesn't affect the corner algs. Tested, yes
# 
# I probably need to eliminate 18 rL algs (applies to corners)
# I'm going to need to change the test suite, or add something...
#  
# # THESE ACTUALLY DO WORK FOR EDGE ALGS !!!  
# # And yes, it doesn't affect the corner algs. Tested, yes   
is_T_rL_length16_notIsCornerAlg_forbidden_when_together = False  # EDGE algs with length 16 or greater that include T and rL are forbidden
is_S_rL_length15_notIsCornerAlg_forbidden_when_together = False  # EDGE algs with length 15 or greater that include S and rL are forbidden

# UNTESTED.  (Well, tested and failed, I think. Or broke the app. Or something)
is_internalYorZ_rL_length18_IsCornerAlg_forbidden_when_together = False    # not used yet

# CONFIGURATION    CONFIGURATION    CONFIGURATION
# CONFIGURATION    CONFIGURATION    CONFIGURATION




startTime = datetime.datetime.now()  # to monitor performance of program

with open("/Users/justindudley/dev/cube/Alg_Slice_And_Widen_daddy/filter-and-sort/INPUT_file/final_alg_list_input.txt") as file_input:
    algs = file_input.read().splitlines() 




# NOTE:  with isTest set to false, only the FIRST ALG in the list is checked for isCornerAlg, group_number, and pattern !!!!   In my other app, alg-slice-and-widen, each of the hundreds of algs are identified. But this app here must process hundreds of thousands of algs, so I don't want the performance hit of checking each one.
pattern = find_pattern(algs[0])
group_number, isCornerAlg = find_group_and_kingdom(pattern)   # note destructuring syntax




algs_to_trash = []
for alg in algs:
    
    if isTest:
          pattern = find_pattern(alg)
          group_number, isCornerAlg = find_group_and_kingdom(pattern) 

         

    alg = alg.strip()



    # OBLIGATORY FILTERING

    if contains_bad_turns(alg):
         algs_to_trash.append(alg)
         continue

    if contains_both_T_and_S(alg):
          algs_to_trash.append(alg)
          continue

    if contains_tri_turn(alg, is_RL_forbidden_everywhere):
          algs_to_trash.append(alg)
          continue

    if contains_RL_tri_turn_AND_Leading_X(alg, is_RL_forbidden_for_Leading_X_algs):
          algs_to_trash.append(alg)
          continue

    if contains_T_not_in_UTU(alg):
          algs_to_trash.append(alg)
          continue
    
    if contains_S_not_in_LSr(alg):
          algs_to_trash.append(alg)
          continue
    
    if contains_internal_TY_or_ZT(alg):
          algs_to_trash.append(alg)
          continue

    if contains_internal_SY_or_ZS(alg):
          algs_to_trash.append(alg)
          continue


    # CREATE ALG_DICT FOR EACH ALG, DURING LOOP. This is done here, AFTER 99% of the algs have already been trashed, for performance reasons
    alg_dict = create_alg_dict(alg, isCornerAlg)
#     print(alg_dict)



      # COMING SOON -- OPTIONAL FILTERING BASED ON CONFIGURATION BOOLEANS
    if special_prohibitions_T_S_rL(alg, isCornerAlg, is_T_rL_length16_notIsCornerAlg_forbidden_when_together, is_S_rL_length15_notIsCornerAlg_forbidden_when_together):
          algs_to_trash.append(alg)


    if isAppFilteringByLength:
          # can make and pass more booleans if more criteria are desired
          if alg_is_too_long(alg, isCornerAlg, edgeAlgMaxLength, edgeAlg_with_S_turns_MaxLength):
                algs_to_trash.append(alg)



filtered_algs_set = set(algs).difference(set(algs_to_trash))  # filtered_algs == everything in algs that isn't in bad_algs
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
