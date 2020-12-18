import collections
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        # a + b    c  = -d)

        mp = collections.defaultdict(int)
        cnt = 0
        for a in A:
            for b in B:
                mp[(a+b)] += 1
        for c in C:
            for d in D:
                if -(c+d) in mp:
                    cnt += mp[-(c+d)]

        return cnt