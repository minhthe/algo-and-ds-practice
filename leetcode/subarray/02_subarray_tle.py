'''https://leetcode.com/problems/subarray-product-less-than-k/'''
class Solution:
	def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
		
		n = len(nums)
		prefix = [1] * (n)
		for i,item in enumerate(nums):
			if i==0: 
				prefix[i] = item
			else:
				prefix[i] = prefix[i-1] * item
		
		cnt = 0 
		# 0 1 2 3 
		# 1 2 3 4
		# 1 2 6 24
		for i in range(n):
			for j in range(i+1, n+1):
				if i == 0:
					p = prefix[j-1]
					
				else:
					p = prefix[j-1] // prefix[i-1]
					
				if p < k : cnt += 1
				
		return cnt