# https://leetcode.com/problems/k-closest-points-to-origin/


import heapq


def k_closest_using_sort(points, k):
    points.sort(key=lambda x: x[0]*x[0] + x[1]*x[1])
    return points[:k]

def k_closest_using_heap(points, k):
    max_heap = []
    for (x, y) in points:
        distance = -(x*x + y*y) # use negative to convert min heap to max heap
        if len(max_heap) == k:
            heapq.heappushpop(max_heap, (distance, x, y))
        else:
            heapq.heappush(max_heap, (distance, x, y))
    result = [[x, y] for (distance, x, y) in max_heap]
    return result

def _2d_list_to_set(l):
    tmp_set = set()
    for row in l:
        tmp_str = '-'.join([str(x) for x in row])
        tmp_set.add(tmp_str)
    return tmp_set

points = [[1,3],[-2,2]]
k = 1
assert k_closest_using_sort(points, k) == [[-2,2]]
assert k_closest_using_heap(points, k) == [[-2,2]]


points = [[3,3],[5,-1],[-2,4]]
k = 2
assert k_closest_using_sort(points, k) == [[3,3],[-2,4]]
assert _2d_list_to_set(k_closest_using_heap(points, k)) == _2d_list_to_set([[3,3],[-2,4]])
