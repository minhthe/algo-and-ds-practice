class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        p1 = []
        p2 = []
        rst =  -1
        
        for i in range(1, int(n **(0.5) + 1)  ):
            
            if n % i == 0: 
                p1.append(i)
                if n//i != i : p2.append(n//i)
        
        if k > len(p1) + len(p2) : return rst
        if k <= len(p1): return p1[k-1]
        return p2[ - ( k - len(p1) )   ]
        