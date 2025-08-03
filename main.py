
import datetime

from methods.identify_alg import identify_alg
from methods.sort_the_algs import sort_the_algs
from methods.create_alg_dict import create_alg_dict
from methods.input_is_homogeneous import input_is_homogeneous
from methods.tunnel_is_other_than_edge_BD import tunnel_is_other_than_edge_BD
from methods__filtering.alg_contains_combo__corner_rL_internalYorZ_over17 import alg_contains_combo__corner_rL_internalYorZ_over17
from methods__filtering.alg_contains_combo__edge_S_over15 import alg_contains_combo__edge_S_over15
from methods__filtering.alg_contains_combo__edge_S_rL_over14 import alg_contains_combo__edge_S_rL_over14
from methods__filtering.alg_contains_combo__edge_over16 import alg_contains_combo__edge_over16
from methods__filtering.contains_bad_turns import contains_bad_turns
from methods__filtering.contains_both_T_and_S import contains_both_T_and_S
from methods__filtering.contains_tri_turn__UD_FB_rl import contains_tri_turn__UD_FB_rl
from methods__filtering.contains_T_not_in_UTU import contains_T_not_in_UTU
from methods__filtering.contains_S_not_in_LSr import contains_S_not_in_LSr
from methods__filtering.contains_internal_TY_or_ZT import contains_internal_TY_or_ZT
from methods__filtering.contains_internal_SY_or_ZS import contains_internal_SY_or_ZS
from methods__optional_filtering.alg_contains_combo__corner_LwithR_over17 import alg_contains_combo__corner_LwithR_over17
from methods__optional_filtering.alg_contains_combo__corner_X_rL_over17 import alg_contains_combo__corner_X_rL_over17
from methods__optional_filtering.alg_contains_combo__corner_internalX_over17 import alg_contains_combo__corner_internalX_over17
from methods__optional_filtering.alg_contains_combo__corner_rL_over17 import alg_contains_combo__corner_rL_over17
from methods__optional_filtering.alg_contains_combo__corner_internalu_internalX_over16 import alg_contains_combo__corner_internalu_internalX_over16
from methods__optional_filtering.alg_contains_combo__edge_LwithR_over15 import alg_contains_combo__edge_LwithR_over15
from methods__optional_filtering.alg_contains_combo__edge_S2_internalX import alg_contains_combo__edge_S2_internalX
from methods__optional_filtering.alg_contains_combo__edge_S2_over14 import alg_contains_combo__edge_S2_over14
from methods__optional_filtering.alg_contains_combo__edge_S_LwithR import alg_contains_combo__edge_S_LwithR
from methods__optional_filtering.alg_contains_combo__edge_T2_DL22_internalWCR_over14 import alg_contains_combo__edge_T2_DL22_internalWCR_over14
from methods__optional_filtering.alg_contains_combo__edge_T_internalWCR_over15 import alg_contains_combo__edge_T_internalWCR_over15
from methods__optional_filtering.alg_contains_combo__edge_T_rL_over15 import alg_contains_combo__edge_T_rL_over15
from methods__optional_filtering.alg_contains_combo__edge_S_WCR_over14 import alg_contains_combo__edge_S_WCR_over14
from methods__optional_filtering.alg_contains_combo__edge_X_T_rL_over15 import alg_contains_combo__edge_X_T_rL_over15
from methods__optional_filtering.alg_contains_combo__edge_internalu_T_over14 import alg_contains_combo__edge_internalu_T_over14
from methods__optional_filtering.alg_contains_combo__edge_internalu_internalX_over15 import alg_contains_combo__edge_internalu_internalX_over15
from methods__optional_filtering.alg_contains_combo__edge_rL2_internalYorZ_over15 import alg_contains_combo__edge_rL2_internalYorZ_over15
from methods__optional_filtering.alg_contains_combo__edge_rL_DL43_internalWCR_over15 import alg_contains_combo__edge_rL_DL43_internalWCR_over15
from methods__optional_filtering.alg_contains_combo__edge_rL_T_internalYorZ_over15 import alg_contains_combo__edge_rL_T_internalYorZ_over15
from methods__optional_filtering.alg_contains_combo__edge_rL_T_u_internalX_over15 import alg_contains_combo__edge_rL_T_u_internalX_over15



# BOOLEANS FOR OPTIONAL FILTERING that are set to TRUE (unless doing some testing)
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



# BOOLEANS FOR OPTIONAL FILTERING that are set to FALSE (unless doing some testing)
this_combo_is_trash__14__INTENDED_FOR_NON_BD_TUNNELS__edge_LwithR_over15 = False    





startTime = datetime.datetime.now()
with open("/Users/justindudley/dev/cube/Alg_Slice_And_Widen_daddy/filter-and-sort/INPUT_file/INPUT__pythonWidened_finished_algs.txt") as file_input:
    algs = file_input.read().splitlines() 

pattern, group_number, isCornerAlg = identify_alg(algs[0])
input_is_homogeneous = input_is_homogeneous(algs)  
tunnel_is_other_than_edge_BD = tunnel_is_other_than_edge_BD(pattern)  # look at pattern of algs[0], determine whether it is edge_BD, which is a more difficult pattern to find algs for and for which I need fewer restrictions and filters


algs_to_trash = []
for alg in algs:
    
    #PRELIMINARIES
    alg = alg.strip()
    if not input_is_homogeneous:
          pattern, group_number, isCornerAlg = identify_alg(alg)
    alg_dict = create_alg_dict(alg, isCornerAlg)  # The longest a run of this program is ever going to take is about 8 seconds. I can make it 4 times faster, 2 seconds, by putting this method below "contains_bad_turns" because that probably eliminates 95% of all the algs by itself. But building the alg_dict at the top looks SO much cleaner for the flow of Main



    # BASELINE FILTERING
    if contains_bad_turns(alg):
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

    if contains_both_T_and_S(alg):
          algs_to_trash.append(alg)
          continue

    if contains_tri_turn__UD_FB_rl(alg):
          algs_to_trash.append(alg)
          continue

    if alg_contains_combo__edge_over16(alg_dict):
          algs_to_trash.append(alg)
          continue 

    if alg_contains_combo__edge_S_over15(alg_dict):
          algs_to_trash.append(alg)
          continue 

    if alg_contains_combo__edge_S_rL_over14(alg_dict): 
          algs_to_trash.append(alg)
          continue 

    if alg_contains_combo__corner_rL_internalYorZ_over17(alg_dict): 
          algs_to_trash.append(alg)
          continue 

    # can add more methods to baseline IF I ALSO CHANGE THE TESTING SUITE
    # can add more methods to baseline IF I ALSO CHANGE THE TESTING SUITE
    # can add more methods to baseline IF I ALSO CHANGE THE TESTING SUITE




    # OPTIONAL FILTERING

    # KEEP:  Optional Rule 3 has been successfully tested.
    if this_combo_is_trash__3__corner_X_rL_over17:
          if alg_contains_combo__corner_X_rL_over17(alg_dict):
                algs_to_trash.append(alg)
                continue  


    # KEEP:  Optional Rule 4 has been successfully tested.
    if this_combo_is_trash__4__edge_rL2_internalYorZ_over15:
          if alg_contains_combo__edge_rL2_internalYorZ_over15(alg_dict):
                algs_to_trash.append(alg)
                continue  
 

    # KEEP:  Optional Rule 5 has been successfully tested.
    if this_combo_is_trash__5__edge_X_T_rL_over15:
          if alg_contains_combo__edge_X_T_rL_over15(alg_dict):
                algs_to_trash.append(alg)
                continue         


    # KEEP:  Optional Rule 6 has been successfully tested.
    if this_combo_is_trash__6__edge_rL_T_internalYorZ_over15:
          if alg_contains_combo__edge_rL_T_internalYorZ_over15(alg_dict):
                algs_to_trash.append(alg)
                continue         


    # KEEP:  Optional Rule 7 has been successfully tested.
    if this_combo_is_trash__7__edge_S2_over14:
          if alg_contains_combo__edge_S2_over14(alg_dict):
                algs_to_trash.append(alg)
                continue   


    # KEEP:  Optional Rule 8 has been successfully tested.
    if this_combo_is_trash__8__edge_S_WCR_over14:
          if alg_contains_combo__edge_S_WCR_over14(alg_dict):
                algs_to_trash.append(alg)
                continue  


    # KEEP:  Optional Rule 9 has been successfully tested.
    if this_combo_is_trash__9__corner_internalX_over17:
          if alg_contains_combo__corner_internalX_over17(alg_dict):
                algs_to_trash.append(alg)
                continue  


    # KEEP:  Optional Rule 10 has been successfully tested.
    if this_combo_is_trash__10__corner_LwithR_over17:
          if alg_contains_combo__corner_LwithR_over17(alg_dict):
                algs_to_trash.append(alg)
                continue      
    

    # KEEP:  Optional Rule 11 has been successfully tested.
    if this_combo_is_trash__11__edge_S2_internalX:
          if alg_contains_combo__edge_S2_internalX(alg_dict):
                algs_to_trash.append(alg)
                continue     
    

    # KEEP:  Optional Rule 12 has been successfully tested.       
    if this_combo_is_trash__12__edge_rL_T_u_internalX_over15:
          if alg_contains_combo__edge_rL_T_u_internalX_over15(alg_dict):
                algs_to_trash.append(alg)
                continue  
    

    # KEEP:  Optional Rule 13 has been successfully tested.          
    if this_combo_is_trash__13__edge_S_LwithR:
          if alg_contains_combo__edge_S_LwithR(alg_dict):
                algs_to_trash.append(alg)
                continue  


    # KEEP:  Optional Rule 15 has been successfully tested.          
    if tunnel_is_other_than_edge_BD:
      if This_combo_is_trash__15__INTENDED_FOR_NON_BD_TUNNELS__edge_T_internalWCR_over15:
            if alg_contains_combo__edge_T_internalWCR_over15(alg_dict):
                  algs_to_trash.append(alg)
                  continue 


    # KEEP:  Optional Rule 16 has been successfully tested.
    if tunnel_is_other_than_edge_BD:
          if This_combo_is_trash__16__INTENDED_FOR_NON_BD_TUNNELS__edge_rL_DL43_internalWCR_over15:
                if alg_contains_combo__edge_rL_DL43_internalWCR_over15(alg_dict):
                  algs_to_trash.append(alg)
                  continue 


    # KEEP:  Optional Rule 17 has been successfully tested.
    if this_combo_is_trash__17__corner_internalu_internalX_over16:
          if alg_contains_combo__corner_internalu_internalX_over16(alg_dict):
                algs_to_trash.append(alg)
                continue  
          

    # KEEP:  Optional Rule 18 has been successfully tested.
    if tunnel_is_other_than_edge_BD:
          if This_combo_is_trash__18__INTENDED_FOR_NON_BD_TUNNELS__edge_internalu_internalX_over15:
                if alg_contains_combo__edge_internalu_internalX_over15(alg_dict):
                      algs_to_trash.append(alg)
                      continue  


    # KEEP:  Optional Rule 19 has been successfully tested.
    if tunnel_is_other_than_edge_BD:
          if This_combo_is_trash__19__INTENDED_FOR_NON_BD_TUNNELS__edge_internalu_T_over14:
                if alg_contains_combo__edge_internalu_T_over14(alg_dict):
                      algs_to_trash.append(alg)
                      continue  


    # KEEP:  Optional Rule 20 has been successfully tested.
    if tunnel_is_other_than_edge_BD:
          if This_combo_is_trash__20__INTENDED_FOR_NON_BD_TUNNELS__edge_T2_DL22_internalWCR_over14:
                if alg_contains_combo__edge_T2_DL22_internalWCR_over14(alg_dict):
                      algs_to_trash.append(alg)
                      continue  



    # FILTERINGS CURRENTLY SET TO FALSE ARE BELOW
    # FILTERINGS CURRENTLY SET TO FALSE ARE BELOW

    # KEEP:  Optional Rule 14 has been successfully tested.  
    if tunnel_is_other_than_edge_BD:
      if this_combo_is_trash__14__INTENDED_FOR_NON_BD_TUNNELS__edge_LwithR_over15:
            if alg_contains_combo__edge_LwithR_over15(alg_dict):
                  algs_to_trash.append(alg)
                  continue  





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
