# https://leetcode.com/problems/product-of-array-except-self/submissions/


def product_except_self(nums):
    n = len(nums)
    arr1 = [0] * n
    arr2 = [0] * n
    result = [0] * n
    arr1[0] = arr2[n-1] = 1
    for i in range(1, n):
        arr1[i] = nums[i-1] * arr1[i-1]
        arr2[n-i-1] = nums[n-i] * arr2[n-i]
    
    for i in range(n):
        result[i] = arr1[i] * arr2[i]
    return result

def product_except_self_v2(nums):
    n = len(nums)
    result = [0] * n
    result[0] = 1
    for i in range(n-1): # skip the last one
        result[i+1] = nums[i] * result[i]

    right_product = 1
    for i in range(n): # full scan
        result[n-i-1] = result[n-i-1] * right_product
        right_product *= nums[n-i-1]

    return result


nums = [1,2,3,4]
assert product_except_self(nums) == [24,12,8,6]
assert product_except_self_v2(nums) == [24,12,8,6]

nums = [-1,1,0,-3,3]
assert product_except_self(nums) == [0,0,9,0,0]
assert product_except_self_v2(nums) == [0,0,9,0,0]

