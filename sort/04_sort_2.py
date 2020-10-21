import collections
class Solution:
    def frequencySort(self, s: str) -> str:
        
        mp = {}
        for c in s:
            if c not in mp:
                mp[c] = [-1, c]
            else:
                mp[c][0] -= 1 
        rst = ""
        for k, v in sorted(mp.items(), key = lambda x: x[1]):
            rst += v[1]*(-v[0])
        return rst
        