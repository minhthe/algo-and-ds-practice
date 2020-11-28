class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s & 1: return False
        s = s // 2
        mp = {}
        # nums = [item for item in nums if item <= s]
        def f(nums, s, pos):
            if (s,pos) in mp: return mp[(s, pos)] 
            if s == 0:
                mp[(s, pos)] = True
                return True
            
            if pos >= len(nums):
                mp[(s, pos)] = False
                return False
            
            if nums[pos] <= s:
                pick = f(nums, s - nums[pos], pos+1)
                if pick : 
                    mp[(s, pos)] = True
                    return True
                not_pick = f(nums, s, pos+1)
                if not_pick: 
                    mp[(s, pos)] = True
                    return True
            else:
                not_pick = f(nums, s, pos+1)
                if not_pick:
                    mp[(s, pos)] = True
                    return True
            mp[(s, pos)]  = False
            return False
            
        return f(nums, s, 0)
        
        
        