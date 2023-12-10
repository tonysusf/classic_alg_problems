# https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

def remove_element(nums, target):
    p2 = 0 # pointer for write
    for p in range(len(nums)):
        if nums[p] != target:
            nums[p2] = nums[p]
            p2 += 1
    print(nums)
    return p2


nums = [3,2,2,3]
k = remove_element(nums, 3)
assert k == 2
assert sorted(nums[:k]) == [2,2]

nums = [0,1,2,2,3,0,4,2]
k = remove_element(nums, 2)
assert k == 5
assert sorted(nums[:k]) == sorted([0,1,4,0,3])