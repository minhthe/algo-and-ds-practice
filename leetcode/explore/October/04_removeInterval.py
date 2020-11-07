''''https://leetcode.com/problems/remove-covered-intervals/''''
class Solution:
	def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
		
		intervals.sort()
		pos = 0
		cnt = 0 
		for i in range(1, len(intervals)):
			# 1 4 2 3
			a, b = intervals[i]
			c, d = intervals[pos]
			if c <= a and b <= d or a == c and d<=b : 
				cnt += 1
				if a == c: pos = i 
			else:
				pos = i
		return len(intervals) - cnt