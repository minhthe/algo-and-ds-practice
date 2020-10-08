import random
class Solution:
	def findKthLargest(self, nums: List[int], k: int) -> int:
	# apply quick sort when the k = 1 == len(k) - 1
		left , right, n = 0, len(nums) - 1, len(nums) 	

		def findPartition(left, right):
			r = random.randint(left, right)
			pivot = nums[r]
			p_idx = left 
			nums[r], nums[right] = nums[right], nums[r]
			for i in range(left, right):
				if nums[i] < pivot:
					nums[p_idx], nums[i]= nums[i], nums[p_idx], 
					p_idx += 1 
			nums[p_idx], nums[right] = nums[right], nums[p_idx]
			return p_idx
		def findK(left , right):
			if(left <= right):
				p_partition = findPartition(left , right)
				if len(nums) - k == p_partition: return nums[p_partition]
				elif len(nums) - k > p_partition: return findK(p_partition+1, right)
				else:return findK(left, p_partition -1)
		return findK(left, right)
