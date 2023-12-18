# https://leetcode.com/problems/meeting-rooms-ii/submissions/

def min_meeting_rooms(intervals):
    if not intervals:
        return 0
    start_times = sorted([k[0] for k in intervals])
    end_times = sorted(k[1] for k in intervals)

    left = right = room_count = 0
    while left < len(intervals):
        if start_times[left] >= end_times[right]:
            room_count -= 1 # meet ended so release a room
            right += 1
        room_count += 1 # use a room
        left += 1   
    return room_count


intervals = [[0,30],[5,10],[15,20]]
assert min_meeting_rooms(intervals) == 2

intervals = [[7,10],[2,4]]
assert min_meeting_rooms(intervals) == 1