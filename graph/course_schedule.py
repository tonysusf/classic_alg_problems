# https://leetcode.com/problems/course-schedule/

from collections import defaultdict
from collections import deque


def can_finish_courses(n, prerequisites):
    pre_to_courses = [[] for _ in range(n)] # list with size n, each is a list too
    count_per_course = [0] * n # prerequisite count per course

    for c, p in prerequisites:
        pre_to_courses[p].append(c)
        count_per_course[c] += 1

    tmp_ready = [i for i in range(n) if count_per_course[i] == 0]
    queue = deque(tmp_ready) # list of ready to start courses
    done_count = 0 # finished course count

    while queue:
        c = queue.popleft() # current course
        done_count += 1
        for other_c in pre_to_courses[c]:
            # remove prerequisite to the course just finished
            count_per_course[other_c] -= 1
            if count_per_course[other_c] == 0:
                queue.append(other_c)
    return done_count == n



num_of_courses = 2
prerequisites = [[1, 0]]
assert can_finish_courses(num_of_courses, prerequisites) == True


num_of_courses = 2
prerequisites = [[1, 0], [0, 1]]
assert can_finish_courses(num_of_courses, prerequisites) == False
