import heapq
class Solution:

    def MaximumSum(self, A):
        
        pq = [-item for item in A]
        print(pq)
        heapq.heapify(pq)
        mp = {}
        result = -1
        # print('df')
        
        def getsum(num):
            
            ans = 0 
            while num >0 :
                
                ans += num % 10 
                num = num//10
                
                
            return ans
        while pq:
            
            
            u = heapq.heappop(pq)
            s = getsum(-u)
            if s in mp:
                
                result = max(result, mp[s] + (-u))
            else:
                mp[s] = -u
             
           
        return result