# https://leetcode.com/problems/find-peak-element/

def find_peak_element(nums):
    l = 0
    r = len(nums) - 1
    while l < r:
        mid = l + (r-l)//2
        if nums[mid] > nums[mid+1]: # peak in left side or mid
            r = mid
        else: # peak in right side
            l = mid + 1
    return l


assert find_peak_element([1,2,3,1]) == 2

assert find_peak_element([1,2,1,3,5,6,4]) == 5

assert find_peak_element([1,2,3]) == 2

assert find_peak_element([1,3,1,2]) == 1
