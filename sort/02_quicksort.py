'''https://leetcode.com/problems/sort-an-array'''
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        
        def f(start, end):
            
            pivot = nums[end]
            
            partition_idx = start

            # 3 6 3 9 4 5
            
            for i in range(start, end):
                if pivot > nums[i]:
                    nums[i], nums[partition_idx] =  nums[partition_idx] , nums[i]
                    partition_idx += 1
            nums[end], nums[partition_idx] =  nums[partition_idx] , nums[end]
                             
                
            
            return partition_idx
            
            
            
        def quicksort(l , r):
            
            
            if l<=r:
                partition_idx = f( l , r)
                quicksort(l ,partition_idx  -1 )
                quicksort( partition_idx + 1, r )
            return nums
                
                
        
        quicksort( 0, len(nums) -1 )
        
        
        return nums
        