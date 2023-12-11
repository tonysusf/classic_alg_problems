# https://leetcode.com/problems/merge-intervals/

def merge_intervals(intervals):
    intervals = sorted(intervals, key=lambda x: x[0])
    current = None
    results = []
    for i in range(len(intervals)):
        if current is None:
            current = intervals[i]
        elif current[1] >= intervals[i][0]: # got overlap
            current[1] = max(current[1], intervals[i][1]) # merge
        else: # no overlap
            results.append(current) # only add if no overlap
            current = intervals[i]
    # add the last one
    results.append(current)
    print(results)
    return results


intervals = [[1,3],[2,6],[8,10],[15,18]]
assert merge_intervals(intervals) == [[1,6],[8,10],[15,18]]


intervals = [[1,4],[4,5]]
assert merge_intervals(intervals) == [[1,5]]


intervals = [[1,4],[4,5], [5, 6]]
assert merge_intervals(intervals) == [[1,6]]

