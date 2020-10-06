'''https://leetcode.com/problems/sort-characters-by-frequency/'''
import collections
class Solution:
    def frequencySort(self, s: str) -> str:
        ss = collections.Counter(s)
        rst = ""
        for item in sorted( ss.items(),key = lambda x : x[1], reverse = True ):
            rst += item[0]*item[1]
        return rst