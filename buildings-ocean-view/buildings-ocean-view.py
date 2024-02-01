# https://leetcode.com/problems/buildings-with-an-ocean-view/


def find_buildings(heights):
    results = []
    max_height = 0
    for i in range(len(heights)-1, -1, -1):
        if max_height < heights[i]:
            results.append(i)
            max_height = heights[i]
    return results[::-1]


assert find_buildings([4,2,3,1]) == [0,2,3]

assert find_buildings([4,3,2,1]) == [0,1,2,3]

assert find_buildings([1,3,2,4]) == [3]
