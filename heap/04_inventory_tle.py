''''https://leetcode.com/problems/sell-diminishing-valued-colored-balls/''''
import heapq
class Solution:
	def maxProfit(self, inventory: List[int], orders: int) -> int:
		
		m = [-item for item in inventory]
		heapq.heapify(m)
		
		rst = 0 
		while orders and m:
			largest = heapq.heappop(m) * (-1)
			if m : 
				next = -m[0]
				r = largest - next + 1
			if m and r <= orders:
				rst += (largest + next) * r // 2
				orders -= r
				heapq.heappush(m, -( largest - r )  )
				# print(largest, next, r, '--', m)
			else: 
				point = largest  - orders + 1
				rst += (largest + point) * (orders)// 2 
				break
		return rst % int(1e9+7)