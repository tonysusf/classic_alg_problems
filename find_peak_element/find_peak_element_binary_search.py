# https://leetcode.com/problems/find-peak-element/


def find_peak_element(nums):
    l = 0
    r = len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] > nums[mid + 1]: # decrasing, peak should be in left side, so move r to left
            r = mid
        else: # increasing, peak should be in right side, so move l to right
            l = mid + 1
    return l

assert find_peak_element([1,2,3,1]) == 2

assert find_peak_element([1,2,1,3,5,6,4]) == 5
