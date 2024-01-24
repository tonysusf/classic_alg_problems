# https://leetcode.com/problems/meeting-rooms-ii/submissions/

def min_meeting_rooms(intervals):
    if not intervals:
        return 0
    # must be sorted for each
    start_times = sorted([x[0] for x in intervals])
    end_times = sorted(x[1] for x in intervals)

    start_idx = end_idx = room_count = 0
    while start_idx < len(intervals):
        if start_times[start_idx] >= end_times[end_idx]:
            room_count -= 1 # meeting ended so release a room
            end_idx += 1
        room_count += 1 # add a new room each time
        start_idx += 1
    return room_count


intervals = [[0,30],[5,10],[15,20]]
assert min_meeting_rooms(intervals) == 2

intervals = [[7,10],[2,4]]
assert min_meeting_rooms(intervals) == 1