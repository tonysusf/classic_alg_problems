# https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter
import heapq

def get_top_frequent_numbers(nums, k):
    if k == len(nums):
        return nums

    num_count_dict = dict(Counter(nums))
    print(num_count_dict)

    return heapq.nlargest(k, num_count_dict.keys(), key = num_count_dict.get)


nums = [1,1,1,2,2,3]
k = 2
print(get_top_frequent_numbers(nums, k))


nums = [1,1,1,2,2,3]
k = 3
print(get_top_frequent_numbers(nums, k))