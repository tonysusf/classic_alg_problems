# https://leetcode.com/problems/merge-sorted-array/

# merge nums1 and nums2 into nums1. both are pre-sorted. need O(n).

def merge(nums1, len1, nums2, len2):
    p1 = len1 - 1
    p2 = len2 - 1
    for t in range(len1 + len2 -1, -1, -1): # go backwards
        if p2 < 0:
            break
        if p1 >= 0 and nums1[p1] > nums2[p2]: # pick from nums1
            nums1[t] = nums1[p1]
            p1 -= 1
        else: # pick from nums2
            nums1[t] = nums2[p2]
            p2 -= 1

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
merge(nums1, 3, nums2, 3)
assert nums1 == [1,2,2,3,5,6]


nums1 = [1]
nums2 = []
merge(nums1, 1, nums2, 0)
assert nums1 == [1]


nums1 = [0]
nums2 = [1]
merge(nums1, 0, nums2, 1)
assert nums1 == [1]