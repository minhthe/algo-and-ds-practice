'''https://leetcode.com/problems/sort-colors'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a,b,c =0,0,0
        for item in nums:
            if item == 0: a +=1
            elif item == 1: b+=1
            else: c+=1
        pos = 0
        while pos < len(nums) : 
            if a > 0: 
                nums[pos] = 0 
                a -= 1
            elif b > 0: 
                nums[pos] = 1 
                b -= 1
            else: 
                nums[pos] = 2
                c -= 1
                
            pos+=1
            
        return nums