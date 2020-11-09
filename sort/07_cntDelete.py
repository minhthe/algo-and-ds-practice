'''https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/''''
import collections
class Solution:
	def minDeletions(self, s: str) -> int:
		c = collections.Counter(s)
		cc = sorted(c.values(), reverse = True)
		tmp = cc[0]
		cnt = 0
		for i in range(1, len(cc)):
			if tmp == 0:
				cnt += cc[i] 
				continue
			elif cc[i] >= tmp:
				tmp = tmp  - 1
				cnt += cc[i] - tmp
			else: 
				tmp = cc[i]
		return cnt