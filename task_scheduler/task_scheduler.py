# https://leetcode.com/problems/task-scheduler/

from collections import Counter

def least_interval(tasks, n):
    task_counts = Counter(tasks)
    max_freq = max(task_counts.values())
    max_freq_count = sum(1 for count in task_counts.values() if count == max_freq)

    part_count = max_freq - 1
    part_length = n + 1
    empty_slots = part_count * part_length + max_freq_count

    return max(len(tasks), empty_slots)


tasks = ["A", "A", "A", "B", "B", "B"]
assert least_interval(tasks, 2) == 8

tasks = ["A","C","A","B","D","B"]
assert least_interval(tasks, 2) == 6

tasks = ["A","A","A", "B","B","B"]
assert least_interval(tasks, 3) == 10
