# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/

class SparseVector:
    def __init__(self, nums):
        self.data = {}
        for i in range(len(nums)):
            if nums[i] != 0:
                self.data[i] = nums[i]

    def dotProduct(self, other_vec):
        result = 0
        # for a key if zero in a but not zero in b then ignore
        for k in self.data:
            result += self.data[k] * other_vec.data[k] if k in other_vec.data else 0
        return result

v1 = SparseVector([1,0,0,2,3])
v2 = SparseVector([0,3,0,4,0])
assert v1.dotProduct(v2) == 8

v1 = SparseVector([0,1,0,0,0])
v2 = SparseVector([0,0,0,0,2])
assert v1.dotProduct(v2) == 0


v1 = SparseVector([0,1,0,0,2,0,0])
v2 = SparseVector([1,0,0,0,3,0,4])
assert v1.dotProduct(v2) == 6
