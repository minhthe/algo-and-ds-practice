import random
class Solution:
	def sortArray(self, nums: List[int]) -> List[int]:
		
		left , right = 0, len(nums) - 1
		
		def f(left, right):
			r  = random.randint(left, right)
			pivot = nums[r]
			nums[r], nums[right] =  nums[right], nums[r]
			p_i = left 
			for i in range(left , right ):
				if pivot > nums[i]:
					nums[p_i], nums[i] =  nums[i], nums[p_i]
					p_i += 1
			nums[p_i], nums[right] =  nums[right], nums[p_i]
			return p_i
				
			
			
		def quicksort(left, right):
			
			if left <= right:
				partition = f(left, right)
				quicksort(left , partition  - 1)
				quicksort(partition  + 1, right)
			
		
		
		quicksort(left ,right)
		return nums