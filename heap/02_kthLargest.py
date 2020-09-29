import heapq
class Solution:
	def findKthLargest(self, nums: List[int], k: int) -> int:
		result = []
		heapq.heapify(result)
		for item in nums:
			if len(result) < k: heapq.heappush(result, item)
			elif result[0] <= item:
			
				heapq.heappop(result)
				heapq.heappush(result, item)
				print(result)
		return heapq.heappop(result)