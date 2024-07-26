# with some trepidation, I begin a third project
# I know that "doing things the right way" is best, but at least for a moment, I'm going to forger ahead
# and try to get this job done!
# It would be great to go ahead and develop all my "bad factors" ideas. But I'm just not sure it's necessary.


import datetime

from methods.is_bad_pattern_when_capitalized import is_bad_pattern_when_capitalized

startTime = datetime.datetime.now() # to monitor performance of program



with open("/Users/justindudley/dev/cube/Alg_Slice_And_Widen_daddy/filter-and-sort/INPUT_file/final_alg_list_input.txt") as file_input:
    algs = file_input.read().splitlines() 


bad_algs = []
for alg in algs:
    alg = alg + " "
    if alg.find("B") >= 0:
        bad_algs.append(alg.strip())
    elif alg.find("b") >= 0:
        bad_algs.append(alg.strip())
    elif alg.find("H") >= 0:
        bad_algs.append(alg.strip())
    elif alg.find("S2") >= 0:
        bad_algs.append(alg.strip())
    

    if is_bad_pattern_when_capitalized(alg):
        bad_algs.append(alg.strip())
    
    

print("\n\n\n")
for alg in bad_algs:
    #    print("bad_alg: ", alg)
    pass


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
