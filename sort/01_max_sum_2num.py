'''https://www.lintcode.com/problem/maximum-sum-of-two-numbers/description'''
import collections
class Solution:
    """
    @param A: An Integer array
    @return: returns the maximum sum of two numbers
    """
    def MaximumSum(self, A):
        A.sort()
        mp = collections.defaultdict(list)
        for item in A:
            s = sum(list( int(k) for k in str(item)))
            mp[s].append(item)
        result = -1
        for key in mp:
            tmp = mp[key]
            if len(tmp) >= 2:
                result = max(result, tmp[-1] + tmp[-2]    )
        return result