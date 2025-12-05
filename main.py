
import datetime

from methods.sort_the_algs import sort_the_algs
from methods.contains_bad_turns import contains_bad_turns
from methods.contains_both_T_and_S import contains_both_T_and_S
from methods.contains_tri_turn import contains_tri_turn
from methods.contains_T_not_in_UTU import contains_T_not_in_UTU
from methods.contains_S_not_in_LSr import contains_S_not_in_LSr
from methods.contains_internal_TY_or_ZT import contains_internal_TY_or_ZT
from methods.contains_internal_SY_or_ZS import contains_internal_SY_or_ZS

startTime = datetime.datetime.now()  # to monitor performance of program


with open("INPUT_file/final_alg_list_input.txt") as file_input:
    algs = file_input.read().splitlines() 



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




print("\n\n\n")
filtered_algs = []
for alg in algs:
       if alg not in bad_algs:
              filtered_algs.append(alg)

sorted_algs = sort_the_algs(filtered_algs)
       


# WRITE TO FILE:  filtered algs
dt = datetime.datetime.now()
output_filename = 'OUTPUT_files/%s.txt'%(dt.strftime("%a") + "_" + dt.strftime("%I") + "h-" + dt.strftime("%M") + "m-" + dt.strftime("%S") + "s_output")
with open(output_filename, "x") as output_file:
	for alg in filtered_algs:
		output_file.write(f"{alg}\n")


# WRITE TO FILE:  filtered AND SORTED algs
sorted_output_filename = 'OUTPUT_files/%s.txt'%(dt.strftime("%a") + "_" + dt.strftime("%I") + "h-" + dt.strftime("%M") + "m-" + dt.strftime("%S") + "s_SORTED_output")
with open(sorted_output_filename, "x") as sorted_output_file:
	for alg in sorted_algs:
		sorted_output_file.write(f"{alg}\n")



print("time elapsed: ", datetime.datetime.now() - startTime)
