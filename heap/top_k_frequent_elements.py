# https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter
import heapq

def top_k_frequent_v1(nums, k):
    if k == len(nums): return nums
    num_count_dict = dict(Counter(nums))
    return heapq.nlargest(k, num_count_dict.keys(), key = num_count_dict.get)


def top_k_frequent_v1b(nums, k):
    if k == len(nums): return nums
    counts = Counter(nums)
    return [num for num, freq in counts.most_common(k)]


# bucket sort, using index, runtime O(n) space O(n)
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

# use min heap, runtime O(m+k) space O(k)
def top_k_frequent_v3(nums, k):
    counts = Counter(nums)
    heap = []

    for num, freq in counts.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)

    return [num for freq, num in heap]


nums = [1,1,1,2,2,3]
k = 2
print('--- input is ---', nums)
print(top_k_frequent_v1(nums, k))
print(top_k_frequent_v1b(nums, k))
print(top_k_frequent_v2(nums, k))
print(top_k_frequent_v3(nums, k))


nums = [1,1,1,2,2,3]
print('--- input is ---', nums)
k = 3
print(top_k_frequent_v1(nums, k))
print(top_k_frequent_v1b(nums, k))
print(top_k_frequent_v2(nums, k))
print(top_k_frequent_v3(nums, k))
