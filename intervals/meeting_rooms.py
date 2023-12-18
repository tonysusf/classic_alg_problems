# https://leetcode.com/problems/meeting-rooms/

def can_attend_meetings(intervals):
    intervals.sort() # sort on start-time by default
    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i+1][0]: # overlap
            return False
    return True


intervals = [[3, 20],[4, 10],[15, 20]]
assert can_attend_meetings(intervals) == False

intervals = [[4, 6], [1, 4]]
assert can_attend_meetings(intervals) == True