class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        rst = []
        
        i  = 0 
        
        j = 1
        
        def f(l,r):
            tmp = ""
            if l!=r-1:
                tmp = "{0}->{1}".format(nums[l], nums[r-1])
            else:
                tmp = "{0}".format(nums[l])
            return tmp
                
        while j <= len(nums):
                
            if j != len(nums) and nums[j] - nums[j-1] == 1:
                j+=1
            else:
                rst.append(f(i,j))
                i = j 
                j += 1
        return rst