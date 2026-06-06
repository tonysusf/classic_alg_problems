# https://leetcode.com/problems/insert-interval/
# Insert a interval into a sorted interval list

def insert_sorted_intervals(intervals, new_interval):
    left = []
    i = 0
    # left side
    while i < len(intervals) and intervals[i][1] < new_interval[0]:
        left.append(intervals[i])
        i += 1
    # merge
    while i < len(intervals) and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    right = intervals[i:]
    return left + [new_interval] + right

def _to_str(l):
    for row in l:
        row.sort()
        for i in range(len(row)):
            row[i] = str(row[i])
    l = [','.join(k) for k in l]
    l.sort()
    out = '|'.join(l)
    return out


intervals = [[1,3],[6,9]]
new_interval = [2,5]
assert _to_str(insert_sorted_intervals(intervals, new_interval)) == _to_str([[1,5],[6,9]])


intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
new_interval = [4,8]
assert _to_str(insert_sorted_intervals(intervals, new_interval)) == _to_str([[1,2],[3,10],[12,16]])

