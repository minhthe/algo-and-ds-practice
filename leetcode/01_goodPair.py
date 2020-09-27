'''https://leetcode.com/problems/number-of-good-pairs/'''
import collections
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        mp = collections.Counter(nums)
        result = 0
        for key in mp:
            result += mp[key]*(mp[key] -1) //2
        return result