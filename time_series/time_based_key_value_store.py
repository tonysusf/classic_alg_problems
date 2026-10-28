# https://leetcode.com/problems/time-based-key-value-store/description/
# python3.14 --version

from collections import defaultdict
from bisect import bisect_right

class TimeMapV1:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, k: str, val: str, ts: int) -> None:
        # key as k
        # value as list of tupple of timestamp and string val
        self.store[k].append((ts, val))

    def get(self, k: str, ts: int) -> str:
        values = self.store.get(k, [])

        # Find first entry with ts > target
        idx = bisect_right(values, ts, key=lambda item: item[0])

        if idx == 0: return ""

        return values[idx - 1][1]


# Manual Binary Search
class TimeMapV2:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, k: str, value: str, timestamp: int) -> None:
        self.store[k].append((timestamp, value))

    def get(self, k: str, timestamp: int) -> str:
        values = self.store.get(k, [])

        left, right = 0, len(values) - 1
        result = ""

        while left <= right:
            mid = (left + right) // 2

            if values[mid][0] <= timestamp:
                result = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return result



tm = TimeMapV1()
tm.set("foo", "bar", 1)
tm.set("foo", "bar2", 4)

print(tm.get("foo", 1))  # "bar"
print(tm.get("foo", 3))  # "bar"
print(tm.get("foo", 4))  # "bar2"
print(tm.get("foo", 5))  # "bar2"
print(tm.get("foo", 0))  # ""

print('-------------------------')
tm = TimeMapV2()
tm.set("foo", "barB", 1)
tm.set("foo", "barB2", 4)

print(tm.get("foo", 1))  # "bar"
print(tm.get("foo", 3))  # "bar"
print(tm.get("foo", 4))  # "bar2"
print(tm.get("foo", 5))  # "bar2"
print(tm.get("foo", 0))  # ""

