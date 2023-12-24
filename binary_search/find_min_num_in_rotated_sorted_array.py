# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


def find_min(nums):
    if len(nums) == 1:
        return nums[0]
    if not nums:
        return None

    l = 0
    r = len(nums) - 1

    if nums[r] > nums[0]:
        return nums[0]

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] > nums[mid + 1]: # smallest one is on the right
            return nums[mid + 1]
        if nums[mid - 1] > nums[mid]: # itself is the smallest one
            return nums[mid]

        if nums[mid] > nums[0]:
            l = mid + 1
        else:
            r = mid - 1


nums = [3, 6, 12, 1, 2]
assert find_min(nums) == 1

nums = nums = [4, 5, 16, 7, 0, 1, 2]
assert find_min(nums) == 0

nums = [11, 13, 15, 17]
assert find_min(nums) == 11

nums = [1]
assert find_min(nums) == 1

nums = []
assert find_min(nums) == None