'''https://leetcode.com/problems/subarray-product-less-than-k'''
class Solution:
	def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
		j = 0 
		cnt = 0 
		p = 1 
		for i,v in enumerate(nums):
			
			p *= v
			while i + 1 > j and  p >= k:
				p /= nums[j]			
				j+=1 
			
			cnt += (i-j) + 1
		return cnt