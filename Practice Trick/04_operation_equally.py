'''https://leetcode.com/problems/minimum-moves-to-equal-array-elements'''
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        req = 0 
        target = min(nums)
        for item in nums:
            req += item - target
        
        return req