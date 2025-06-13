# THIS METHOD AND ITS SUPPORTING FILES WERE BORROWED FROM MY ALG-SLICE-AND-WIDEN APP



# The 3x3 cube has 3 "KINGDOMS" or "orbits":   Center pieces, Corner pieces, Edge pieces
# In most but not all solving systems, the centers are presumed to be fixed and do not constitute an orbit

from variables.constants import STICKERS_SITTING_IN_CORNER_POSITIONS_ABCDUVWX__ALL_GROUPS
from variables.constants import STICKERS_SITTING_IN_CENTER_POSITIONS__GROUP_1
from variables.constants import STICKERS_SITTING_IN_CENTER_POSITIONS__GROUP_2
from variables.constants import STICKERS_SITTING_IN_CENTER_POSITIONS__GROUP_3
from variables.constants import STICKERS_SITTING_IN_CENTER_POSITIONS__GROUP_4
from variables.constants import STICKERS_SITTING_IN_CENTER_POSITIONS__GROUP_5
from variables.constants import STICKERS_SITTING_IN_CENTER_POSITIONS__GROUP_6




def find_group_and_kingdom(pattern):

    group_number = -1
    isCornerAlg = False
    stickers_sitting_in_center_positions = pattern[0:6]  # indexes of center positions
    stickers_sitting_in_corner_positions_ABCDUVWX = pattern[6:10] + pattern[26:30]  # indexes of positions A,B,C,D and of U,V,W,X



    # discover whether alg swaps CORNERS or EDGES:
    for sticker in stickers_sitting_in_corner_positions_ABCDUVWX:
        count = 0
        for i in range(8):
            if stickers_sitting_in_corner_positions_ABCDUVWX[i] == STICKERS_SITTING_IN_CORNER_POSITIONS_ABCDUVWX__ALL_GROUPS[i]:
                count += 1

        if count == 6:
            isCornerAlg = True    # Two corners are out of place and must have been swapped.  (When count == 8, we have an edge swap alg, so isCornerAlg == False, which is set as the default at top)



    # discover GROUP NUMBER:
    if stickers_sitting_in_center_positions == STICKERS_SITTING_IN_CENTER_POSITIONS__GROUP_1:
        group_number = 1

    if stickers_sitting_in_center_positions == STICKERS_SITTING_IN_CENTER_POSITIONS__GROUP_2:
        group_number = 2
            
    if stickers_sitting_in_center_positions == STICKERS_SITTING_IN_CENTER_POSITIONS__GROUP_3:
        group_number = 3
    
    if stickers_sitting_in_center_positions == STICKERS_SITTING_IN_CENTER_POSITIONS__GROUP_4:
        group_number = 4
    
    if stickers_sitting_in_center_positions == STICKERS_SITTING_IN_CENTER_POSITIONS__GROUP_5:
        group_number = 5
    
    if stickers_sitting_in_center_positions == STICKERS_SITTING_IN_CENTER_POSITIONS__GROUP_6:
        group_number = 6
        



    return [group_number, isCornerAlg]