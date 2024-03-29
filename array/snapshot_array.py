# https://leetcode.com/problems/snapshot-array/

class SnapshotArrayV1:
    def __init__(self, length):
        self.snap_id = 0
        self.array = [{0: 0} for _ in range(length)]

    def set(self, index, val):
        self.array[index][self.snap_id] = val

    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        snaps = self.array[index]
        while snap_id not in snaps:
            snap_id -= 1
        return snaps[snap_id]


class SnapshotArrayV2:
    def __init__(self, length):
        self.snap_id = 0
        self.array = [{0: 0} for _ in range(length)]

    def set(self, index, val):
        self.array[index][self.snap_id] = val

    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        snaps = self.array[index]
        left, right = 0, snap_id + 1
        while left < right:
            mid = left + (right - left) // 2
            if mid not in snaps:
                right = mid
            else:
                left = mid + 1
        return snaps[left - 1] if left > 0 else 0

obj = SnapshotArrayV1(3)
obj.set(0, 5)
assert obj.snap() == 0
obj.set(0, 6)
assert obj.get(0, 0) == 5

obj = SnapshotArrayV2(3)
obj.set(0, 5)
assert obj.snap() == 0
obj.set(0, 6)
assert obj.get(0, 0) == 5

