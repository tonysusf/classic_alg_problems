# https://leetcode.com/problems/container-with-most-water/description/

def get_max_area(nums):
    max_area = 0
    l = 0
    r = len(nums) - 1

    while l < r:
        max_area = max(max_area, min(nums[l], nums[r]) * (r - l))
        if nums[l] <= nums[r]:
            l += 1
        else:
            r -= 1
    return max_area


nums = [1,8,6,2,5,4,8,3,7]
assert get_max_area(nums) == 49


nums = [1, 1]
assert get_max_area(nums) == 1

nums = [1]
assert get_max_area(nums) == 0


