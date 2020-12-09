import collections
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mp = collections.defaultdict(int)
        cnt = 0
        for item in time:
            m = item % 60
            cnt += mp[(60-m)%60]
            mp[m] += 1
        return cnt    