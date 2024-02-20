# https://leetcode.com/problems/product-of-array-except-self/submissions/


def product_except_self(nums):
    l = [0] * len(nums)
    l[0] = 1
    r = 1
    for i in range(1, len(nums)):
        l[i] = l[i-1] * nums[i-1]

    for i in range(len(nums)-2, -1, -1):
        r *= nums[i+1]
        l[i] *= r
    return l


nums = [1,2,3,4]
assert product_except_self(nums) == [24,12,8,6]

nums = [-1,1,0,-3,3]
assert product_except_self(nums) == [0,0,9,0,0]

