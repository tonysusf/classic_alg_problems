# https://leetcode.com/problems/maximum-product-subarray/description/


def max_product(nums):
    if len(nums) == 0:
        return 0

    max_prod = min_prod = nums[0]
    result = max_prod
    for i in range(1, len(nums)):
        new_max_prod = max(nums[i], nums[i] * max_prod, nums[i] * min_prod)
        min_prod = min(nums[i], nums[i] * max_prod, nums[i] * min_prod)
        max_prod =  new_max_prod
        result = max(result, max_prod)
    return result


nums = [2, 3, -2, 4]
assert max_product(nums) == 6

nums = [-2, 0, -1]
assert max_product(nums) == 0
