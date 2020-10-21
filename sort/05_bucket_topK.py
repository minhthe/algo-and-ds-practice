''''https://leetcode.com/problems/top-k-frequent-elements/''''
import collections
class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		counter = collections.Counter(nums)
		max_v = max(counter.values())
		rst = [[] for i in range(max_v+1)]
		for u, v in counter.items():
			rst[v] += [u]
		tmp = []
		for i in range(max_v, 0, -1):
			if rst[i]: tmp += rst[i]
			if len(tmp) == k: return tmp
		return tmp