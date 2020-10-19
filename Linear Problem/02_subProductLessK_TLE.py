'''https://leetcode.com/problems/subarray-product-less-than-k'''
class Solution:
	def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
		mp = {}
		l , r = 0 , len(nums) - 1
		
		product = [1 for i in range(len(nums))] 		
		product[0] = nums[0]		
		for i in range(1, len(nums)):
			product[i] = product[i-1] * nums[i]
		
		
		def  f(left, right):
			if left > right: return 0 
			if (left, right) in mp : return mp[(left, right)]
			if left == 0: p = product[right]
			else: p = product[right]//product[left -1 ]						
			if p >= k:
				return f(left , right - 1) + f(left+1, right) - f(left+1, right- 1 )
			else:
				l = right - left +1 
				mp[(left, right)] = l * (l+1) //2 
				return  mp[(left, right)]
			
		ans =  f(l, r)
		return ans