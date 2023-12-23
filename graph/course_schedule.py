# https://leetcode.com/problems/course-schedule/

from collections import defaultdict


def has_cycle_in_dfs(course_idx, adj_edges, visited, is_parent):
    if is_parent[course_idx]:
        return True # cycle found
    if visited[course_idx]:
        return False
    visited[course_idx] = True
    is_parent[course_idx] = True
    for neighbor in adj_edges[course_idx]:
        if has_cycle_in_dfs(neighbor, adj_edges, visited, is_parent):
            return True # bubble up
    is_parent[course_idx] = False
    return False

def can_finish_courses(num_of_courses, prerequisites):
    adj_edges = defaultdict(list) # key as target course, value as dependent courses
    for pr in prerequisites:
        adj_edges[pr[1]].append(pr[0])
    visited = [False] * num_of_courses
    is_parent = [False] * num_of_courses
    for course_idx in range(num_of_courses):
        if has_cycle_in_dfs(course_idx, adj_edges, visited, is_parent):
            return False # has cycle then can't schedule
    return True

num_of_courses = 2
prerequisites = [[1, 0]]
assert can_finish_courses(num_of_courses, prerequisites) == True


num_of_courses = 2
prerequisites = [[1, 0], [0, 1]]
assert can_finish_courses(num_of_courses, prerequisites) == False
