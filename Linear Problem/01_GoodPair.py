'''https://leetcode.com/problems/number-of-good-pairs/'''
import collections
class Solution:
	def numIdenticalPairs(self, nums: List[int]) -> int:
		
		mp = collections.defaultdict(int)
		cnt = 0 
		for i, v in enumerate(nums):
			 cnt += mp[v]
			 mp[v] += 1 
		return cnt
		