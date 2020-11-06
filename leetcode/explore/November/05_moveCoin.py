class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        mp=  {1:0, 0: 0}
        for item in position:
            if item & 1: 
                mp[1] += 1
            else:
                mp[0] += 1
        return mp[0] if mp[0]<mp[1] else mp[1]
        