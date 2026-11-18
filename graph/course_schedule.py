# https://leetcode.com/problems/course-schedule/

from collections import deque

def can_finish_courses(n, prerequisites):
    print('input is', n, prerequisites)

    ps_to_courses = [[] for _ in range(n)] # list with size n, each is a list too
    count_per_course = [0] * n # prerequisite count per course

    for c, p in prerequisites:
        ps_to_courses[p].append(c)
        count_per_course[c] += 1

    tmp_ready = [i for i in range(n) if count_per_course[i] == 0]
    queue = deque(tmp_ready) # list of ready to start courses
    done_count = 0 # finished course count

    while queue:
        current = queue.popleft() # current course
        done_count += 1
        for oc in ps_to_courses[current]: # oc as other_course
            # remove prerequisite to the course just finished
            count_per_course[oc] -= 1
            if count_per_course[oc] == 0:
                queue.append(oc)
    return done_count == n



num_of_courses = 2
prerequisites = [[1, 0]]
assert can_finish_courses(num_of_courses, prerequisites) == True


num_of_courses = 2
prerequisites = [[1, 0], [0, 1]]
assert can_finish_courses(num_of_courses, prerequisites) == False
