# https://leetcode.com/problems/maximum-swap/


def maximum_swap(num):
    l = list(str(num)) # digits of the num
    lookup = {int(l[i]): i for i in range(len(l))} # key as num and value as index

    for i in range(len(l)):
        for other_idx in range(9, int(l[i]), -1): # try find bigger number than itself
            if lookup.get(other_idx, -1) > i: # found
                l[i], l[lookup[other_idx]] = l[lookup[other_idx]], l[i] # swap
                return int(''.join(l))
    return num

assert maximum_swap(2736) == 7236

assert maximum_swap(9973) == 9973

