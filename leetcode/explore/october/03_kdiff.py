'''
https://leetcode.com/problems/k-diff-pairs-in-an-array/
'''

import collections
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        if k == 0:
            cnt = 0
            tmp = collections.Counter(nums)
            for key in tmp:
                if tmp[key] > 1: cnt+=1
            return cnt
        nums = list(set(nums))
        # nums.sort()
        
        mp = {nums[i]: i for i in range(len(nums)) }
        cnt = 0 
       
        for i, v in enumerate(nums):
            if (v + k) in mp:
                if mp[(v+k)] != i: cnt+=1
        return cnt