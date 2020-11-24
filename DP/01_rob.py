class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 0: return 0
        ans = max(nums)
        
        for i in range(2, n):
            if i >= 3:
                nums[i] = max(nums[i] + nums[i-2], nums[i] + nums[i-3])
                ans = max(ans , nums[i])
            else:                
                nums[i] = nums[i] + nums[i-2]
                ans = max(nums[i], ans)
        
        return ans
            
        