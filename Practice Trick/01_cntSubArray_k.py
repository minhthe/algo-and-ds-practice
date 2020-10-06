'''https://leetcode.com/problems/subarray-sum-equals-k'''
import collections
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = collections.defaultdict(int)
        mp[0] = 1
        total_s = 0
        cnt = 0 
        for i, v in enumerate(nums):
            total_s += v
            if total_s - k in mp:
                cnt += mp[total_s - k]
            mp[total_s] += 1
        return cnt