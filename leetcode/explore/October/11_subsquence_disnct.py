'''
Greading approach: if the char you want to add, and this char not the last, 
-> consider will add later not NOT to achive lexicographical order
'''
class Solution:
	def removeDuplicateLetters(self, s: str) -> str:
		
		last_index = {c: i for i,c in enumerate(s)}
		
		stk = []
		for i, c in enumerate(s):
			if c in stk: continue
			while stk and stk[-1] > c and last_index[stk[-1]] > i:
				stk.pop()
			stk.append(c)
		return ''.join(stk)