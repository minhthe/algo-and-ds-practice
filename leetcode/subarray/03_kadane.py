class Solution:
	def maxSubArray(self, nums: List[int]) -> int:
		max_sum, running_sum = -int(2**31), 0 		
		for item in nums:
			max_sum, running_sum = max(max_sum, running_sum + item), max(0, running_sum + item)
		return max_sum
		