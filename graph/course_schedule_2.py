from typing import *
from collections import deque

def find_order(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    graph = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

    queue = deque()
    for course in range(numCourses):
        if indegree[course] == 0:
            queue.append(course)

    order = []
    while queue:
        course = queue.popleft()
        order.append(course)
        for next_course in graph[course]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                queue.append(next_course)

    if len(order) == numCourses:
        print('output is', order)
        return order
    return []


num_of_courses = 2
prerequisites = [[1, 0]]
assert find_order(num_of_courses, prerequisites) == [0,1]

num_of_courses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
result = find_order(num_of_courses, prerequisites)
assert  result == [0,2,1,3] or result == [0,1,2,3]
