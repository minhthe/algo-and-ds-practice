class Solution:
	def canReach(self, arr: List[int], start: int) -> bool:
		
		n = len(arr)
		visisted = set()
		
		def f(pos, visisted):
			## base condtion
			if pos in visisted or (not 0 <= pos <= n - 1  ): return False
			if arr[pos] == 0: return True
            
			visisted.add(pos)
			if f(pos + arr[pos], visisted): return True	
			if f(pos - arr[pos], visisted): return True
			visisted.remove(pos)
			return False
		
		
		return f(start, visisted)