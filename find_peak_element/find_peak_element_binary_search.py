# https://leetcode.com/problems/find-peak-element/

def find_peak_element(nums):
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = l + (r-l)//2
        # left neighbour greater, move r towards left side
        if m > 0 and nums[m-1] > nums[m]:
            r = m-1
        # right neighbour greater, move l towards right side
        elif m < len(nums)-1 and nums[m+1] > nums[m]:
            l = m+1
        else: # peak found
            return m

assert find_peak_element([1,2,3,1]) == 2

assert find_peak_element([1,2,1,3,5,6,4]) == 5

assert find_peak_element([1,2,3]) == 2

assert find_peak_element([1,3,1,2]) == 1
