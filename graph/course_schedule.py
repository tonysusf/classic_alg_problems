# https://leetcode.com/problems/course-schedule/

from collections import defaultdict


def has_cycle(current, edges, visited, in_path):
    if in_path[current]:
        return True # cycle found
    if visited[current]:
        return False
    visited[current] = True
    in_path[current] = True
    for other_node in edges[current]:
        if has_cycle(other_node, edges, visited, in_path):
            return True # bubble up
    in_path[current] = False # reset
    return False

def can_finish_courses(num_of_courses, prerequisites):
    edges = defaultdict(list) # key as target course, value as dependent courses
    for p in prerequisites:
        edges[p[1]].append(p[0])
    visited = [False] * num_of_courses
    in_path = [False] * num_of_courses
    for current in range(num_of_courses):
        if has_cycle(current, edges, visited, in_path):
            return False # can't finish
    return True

num_of_courses = 2
prerequisites = [[1, 0]]
assert can_finish_courses(num_of_courses, prerequisites) == True


num_of_courses = 2
prerequisites = [[1, 0], [0, 1]]
assert can_finish_courses(num_of_courses, prerequisites) == False
