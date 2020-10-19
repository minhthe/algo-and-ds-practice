class Solution:
	def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
		cnt =  0 
		p = 1 
		start = 0
		for end, value in enumerate(nums):
			p *= value
			while start <= end and p >= k:
				p = p//nums[start]
				start += 1 
			cnt += end - start + 1
		return cnt