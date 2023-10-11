#!/usr/bin/python3

def best_score(a_dictionary):
    bst_value = 0
    bst_key = None
    if a_dictionary:
        for bk, bv in a_dictionary.items():
            if bv > bst_value:
                bst_value = bv
                bst_key = bk
        return bst_key
    else:
        return None
