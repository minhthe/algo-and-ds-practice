''https://www.lintcode.com/problem/maximum-size-subarray-sum-equals-k''''
class Solution:

	def maxSubArrayLen(self, nums, k):
		rst = 0 
		mp = {0: -1}
		running_sum = 0 
		for i,v in enumerate(nums):
			running_sum += v
			if running_sum - k in mp:
				rst = max(rst, i - mp[running_sum - k])
			elif running_sum not in mp:
				mp[running_sum] = i
		return rst