import collections
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        mp = collections.defaultdict(int)
        rst = 0 
        for item in nums:
            mp[item] += 1
            rst += (mp[item] - 1)
        return rst