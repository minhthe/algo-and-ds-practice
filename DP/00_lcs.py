'''https://leetcode.com/problems/longest-common-subsequence'''
class Solution:
	def longestCommonSubsequence(self, text1: str, text2: str) -> int:
		l1, l2 = len(text1), len(text2)
		rst = 0 
		mp = {}
		def f(i,j):
			if (i,j) in mp: return mp[(i,j)]
			if i == l1  or j == l2: return 0
			if text1[i] == text2[j]:
				mp[(i,j)] =  1 + f(i+1, j+1)
				return mp[(i,j)]
			else:
				mp[(i,j)] = max(  f(i+1, j), f(i, j+1) )
				return mp[(i,j)]
				
		rst = f(0,0)
		return rst