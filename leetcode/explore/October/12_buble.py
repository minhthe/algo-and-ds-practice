import collections
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        
        na, nb = len(A), len(B)
        
        if na != nb: return False
        x ,y = -1 , -1
        cnt =  0 
        for i in range(na):
            if A[i] != B[i]  :
                # x = i.
                if cnt == 0: 
                    x = i 
                elif cnt == 1:
                    y = i
                cnt+=1
                        
                       
                       
                       
        return (cnt == 2 and A[x]==B[y] and A[y] == B[x]) or (A == B and len([u for u,v in collections.Counter(A).items() if v > 1]  ))