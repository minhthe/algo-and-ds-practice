'''https://leetcode.com/problems/online-stock-span/'''
class StockSpanner:
	def __init__(self):
		self.stk = []		
		
	def next(self, price: int) -> int:
		cnt =  1
		while self.stk and self.stk[-1][0] <= price:
			u, l  = self.stk.pop()
			cnt+= l
		self.stk.append( (price, cnt) )
		return cnt