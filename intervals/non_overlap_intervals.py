# https://leetcode.com/problems/non-overlapping-intervals/

# sort by end time to achive minimum remove
# e.g. [1, 3], [1, 4], [1, 2], [2, 3] sort -> [1, 2], [1, 3], [2, 3], [1, 4] -> remove [1, 3], [1, 4]
def remove_overlap_intervals(intervals):
    intervals.sort(key = lambda x: x[1]) # sort by end time
    print('sorted', intervals)
    remove_count = 0
    current = None
    
    for interval in intervals: # scan by start time
        if current is None or interval[0] >= current: # no overlap
            current = interval[1]
        else:
            remove_count += 1 # otherwise overlap found
    print(remove_count)
    return remove_count


intervals = [[1,2],[2,3],[3,4],[1,3]]
assert remove_overlap_intervals(intervals) == 1


intervals = [[1,2],[1,2],[1,2]]
assert remove_overlap_intervals(intervals) == 2


intervals = [[1,2],[2,3]]
assert remove_overlap_intervals(intervals) == 0


