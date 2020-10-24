'''https://leetcode.com/problems/132-pattern/'''
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2: return False
        
        def f(x,y):
            arr = nums[y+1:]
            
            tmp = sorted(arr)
            
            l , r = 0,  len(tmp) -1
            while l <= r:
                m = int( (r-l)/2 + l )
                if nums[x] < tmp[m] < nums[y]: return True
                elif tmp[m] > nums[y]: r = m - 1
                else: l = m + 1
                
            return False
            
        for i in range(n-2):
            for j in range(i+1, n -1):
                if nums[i] < nums[j]:
                    if(f(i,j)): return True                    
        return False