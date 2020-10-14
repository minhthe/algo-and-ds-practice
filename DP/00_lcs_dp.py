'''https://leetcode.com/problems/longest-common-subsequence'''
class Solution:
	def longestCommonSubsequence(self, text1: str, text2: str) -> int:
		m, n = len(text1), len(text2)
		
		rst = [ [0 for i in range(n+1)] for j in range(m+1) ]
		
		for i in range(1, m+1):
			for j in range(1, n+1):
				if text1[i-1] == text2[j-1]:
					rst[i][j] = rst[i-1][j-1] + 1
				else:
					rst[i][j] = max(rst[i-1][j], rst[i][j-1])
		return rst[m][n]