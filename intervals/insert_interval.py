# https://leetcode.com/problems/insert-interval/
# Insert a interval into a sorted interval list

def insert_sorted_intervals(intervals, new_interval):
    # Insert in-place
    for i in range(len(intervals)):
        if new_interval[0] < intervals[i][0]:
            intervals.insert(i, new_interval)
            new_interval = None
            break
    if new_interval:
        intervals.append(new_interval)

	# Merge a sorted interval list
    results = []
    current = None
    for i in range(len(intervals)):
        if current is None:
            current = intervals[i]
        elif current[1] >= intervals[i][0]: # overlap
            current[1] = max(current[1], intervals[i][1]) # merge
        else: # no overlap
            results.append(current)
            current = intervals[i]
    if current:
        results.append(current)
    return results

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

