# https://leetcode.com/problems/continuous-subarray-sum/


def check_subarray_sum(nums, k):
    lookup = {0: -1}
    run_sum = 0
    for i in range(len(nums)):
        run_sum += nums[i]
        run_sum %= k

        if run_sum in lookup:
            if i - lookup[run_sum] > 1: return True
        else:
            lookup[run_sum] = i
    return False


assert check_subarray_sum([23,2,4,6,7], 6) == True

assert check_subarray_sum([23,2,6,4,7], 6) == True

assert check_subarray_sum([23,2,6,4,7], 13) == False
