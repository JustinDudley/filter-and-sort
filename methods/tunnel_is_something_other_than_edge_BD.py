
from variables.constants import Tunnel_BD_Shell_Pattern


def tunnel_is_something_other_than_edge_BD(pattern):

    # This syntax finds the last 49 indices of the list. So, it looks at all the corner and edge stickers, not the center stickers
    if pattern[-48:] == Tunnel_BD_Shell_Pattern:
        return False
    

    return True