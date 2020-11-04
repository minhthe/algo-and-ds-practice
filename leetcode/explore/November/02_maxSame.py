'''https://leetcode.com/problems/consecutive-characters/'''
class Solution:
	def maxPower(self, s: str) -> int:
		n = len(s)
		max_v = 1
		cnt = 1
		for i in range(1, n):
			if(s[i] != s[i-1]):
				cnt = 1
			else:
				cnt  += 1 
			max_v = max(cnt, max_v)
		return max_v