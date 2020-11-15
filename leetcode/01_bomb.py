'''https://leetcode.com/problems/defuse-the-bomb/'''
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n , tmp = len(code), code
        if k == 0: return [0] * n
        def f(pos, tmp):
            sub = 0
            if k > 0:
                for j in range(pos+1, pos + k + 1, 1 ):
                    sub += tmp[  j % n   ]
                return sub
            j = 1
            while j <= -k:
                sub += tmp[  (pos - j)% n   ]
                j += 1
            return sub
                
        rst= [0 for i in range(n)]
        for i in range(n):
            rst[i] = f(i, tmp)
        return rst
        