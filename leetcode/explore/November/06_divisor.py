import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(pos):
            
            tmp = 0
            for item in nums:
                tmp += math.ceil(item/pos)
            # print(pos, tmp)
            return tmp <= threshold
        def bs(left, right):
            
            while left < right:
                mid = int( (right - left)/2 + left )
                tmp = 0
                for item in nums:
                    tmp += math.ceil(item/mid)
               ####### -------tmp---
            
                if tmp > threshold:
                    left = mid + 1
                else:
                    right = mid 
            return left
            
        # sum/ x = d -> 
        s = sum(nums)
        min_v = math.ceil(s/threshold)
        
#         for i in range(min_v, max(nums)+1, 1):
            
#             if(check(i)):
#                 return i
        
    
        return bs(min_v, max(nums))