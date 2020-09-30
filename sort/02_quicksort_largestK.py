class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #### the largest is the k = 1 
        ## when the partition_idx = n - 1
        ## n - k == partion_indx => return that
        def findPartition_index(start, end):
            pivot = nums[end]
            p_idx = start
            for i in range(start, end):
                if pivot > nums[i]:
                    nums[p_idx], nums[i] = nums[i], nums[p_idx] 
                    p_idx += 1
            nums[p_idx], nums[end] = nums[end], nums[p_idx] 
            
            return p_idx
            
        def findLargestK(l, r):
            
            if l <= r:
                partition_index = findPartition_index(l, r)
                if partition_index == len(nums) - k: return nums[partition_index]
                if partition_index > len(nums) - k: return findLargestK(l, partition_index - 1)
                return findLargestK(partition_index+ 1, r)
            
        return findLargestK(0, len(nums) -1 )
        