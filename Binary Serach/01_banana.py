'''https://leetcode.com/problems/koko-eating-bananas/'''
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        
        
        n = len(piles)
        l, r = 1, max(piles)
        def f(num):
            s = 0
            for item in piles:
                s +=math.ceil(item/num)
            # print('df',num, s)
            if s < H: return 1
            elif s == H: return 0
            else: return -1
        while l <= r:
        
            mid = int( (r-l)/2 + l )
            tmp = f(mid)
            if(tmp == 0): return mid
            elif tmp == 1: r = mid - 1
            else: l = mid  +1
            
        print(l)
        return l