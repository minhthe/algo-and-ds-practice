''''https://leetcode.com/problems/contiguous-array''''
import collections
class Solution:
	def findMaxLength(self, nums: List[int]) -> int:
		rst = 0
		mp = collections.defaultdict(lambda : int(1e9))
		mp[0] = -1
		end_sum = 0 
	
		for i, v in enumerate(nums):
			if v == 0: v = -1
			end_sum += v
			if end_sum in mp:
				rst = max(rst,i - mp[end_sum])
			mp[end_sum] = min(i, mp[end_sum])
		
		return rst
