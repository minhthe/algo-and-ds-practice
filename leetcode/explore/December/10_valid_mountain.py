class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        n = len(arr)      
        p = 0
        flag = False
        
        while p < n - 1 and  arr[p] < arr[p+1]:
            flag = True
            p += 1
            
        if not flag: return False 
        
        flag = False
        
        while p < n - 1 and arr[p] > arr[p+1]:
            flag = True
            p += 1        
        return p == n - 1 and flag
        