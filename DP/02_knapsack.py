class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1 : return False
        s = s // 2
        
        @lru_cache(None)
        def f(s, pos):
            
            if pos == - 1 or s < 0 : return False
            
            if s == 0 : return True
            
            if f(s - nums[pos], pos -1 ) : return True
        
            if f(s, pos - 1): return True
                    
        return f(s, len(nums)-1)
    