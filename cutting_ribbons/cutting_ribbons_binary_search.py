# https://leetcode.com/problems/cutting-ribbons/


def max_ribbon_length(ribbons, k):
    # k is num of ribbons to cut
    def can_cut_len(curr_len):
        return sum(x // curr_len for x in ribbons) >= k

    l, r = 1, max(ribbons)
    max_can_cut_len = 0
    while l <= r:
        mid = (l + r) // 2
        if can_cut_len(mid):
            max_can_cut_len = mid
            l = mid + 1
        else:
            r = mid - 1
    return max_can_cut_len


assert max_ribbon_length([9,7,5], 3) == 5

assert max_ribbon_length([7,5,9], 4) == 4

assert max_ribbon_length([2,1,1], 4) == 1