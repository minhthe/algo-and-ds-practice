'''
https://www.lintcode.com/problem/meeting-rooms
'''
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        # Write your code here
        if not intervals: return True 
        max_v = max(list(item.end for item in intervals))
        rank = [0]*(max_v+1)
        for item in intervals:
            x, y=  item.start, item.end 
            rank[x] += 1 
            rank[y] -= 1
        s = 0 
        for i in range(max_v+1):
            s += rank[i] 
            if s > 1: return False
        return True