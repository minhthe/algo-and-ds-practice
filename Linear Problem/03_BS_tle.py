class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <=2 : return False
        rst= []
        for i in range(n-2):
            for j in range(i+1,n-1):
                if nums[i] < nums[j]: rst.append( ( i,j ) )
        
        def f(x,y):
            tmp = nums[y+1:]
            tmp = sorted(tmp)
            l , r = 0 , len(tmp)-1
            while l <= r:
                z = int( (r - l )/2 +l )
                if nums[x] < tmp[z] < nums[y]: return True
                elif  tmp[z] > nums[y] : r = z - 1
                else: l = z + 1
                
            
            return False
        
        
       
        for x, y in rst:
            if(f(x,y)): return True
        return False
            
            