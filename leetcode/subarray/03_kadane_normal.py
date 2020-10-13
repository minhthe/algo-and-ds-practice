class Solution:
	def maxSubArray(self, nums: List[int]) -> int:
		max_sum = -int(2**31)
		running_sum =  0 
		for item in nums:
			running_sum += item
			
			if running_sum > max_sum : max_sum = running_sum 
			if running_sum< 0: running_sum = 0 
		return max_sum