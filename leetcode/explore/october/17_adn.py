class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        mp = {}
        n = len(s)
        hash_value = 0 
        
        ans = set([])
        
              
        if n == 10: return []
        
        mp[s[:10]] = (0,9, s[:10])
        for i in range(1, n-10+1, 1):
            if s[i:i+10] in mp and s[i:i+10] == mp[s[i:i+10]][2]:
                ans.add(s[i:i+10])
            else:
                mp[s[i:i+10]] = (i, i+10, s[i:i+10])
        return list(ans)
        