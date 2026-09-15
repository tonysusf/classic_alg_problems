# https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter
import heapq

def top_k_frequent_v1(nums, k):
    if k == len(nums):
        return nums

    num_count_dict = dict(Counter(nums))
    print(num_count_dict)

    return heapq.nlargest(k, num_count_dict.keys(), key = num_count_dict.get)


def top_k_frequent_v2(nums, k):
    counts = Counter(nums)

    buckets = [[] for _ in range(len(nums) + 1)]

    for value, frequency in counts.items():
        buckets[frequency].append(value)

    result = []

    for bucket in reversed(buckets):
        for value in bucket:
            result.append(value)

            if len(result) == k:
                return result


nums = [1,1,1,2,2,3]
k = 2
print(top_k_frequent_v1(nums, k))
print(top_k_frequent_v2(nums, k))


nums = [1,1,1,2,2,3]
k = 3
print(top_k_frequent_v1(nums, k))
print(top_k_frequent_v2(nums, k))