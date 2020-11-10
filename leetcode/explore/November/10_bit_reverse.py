class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        
        
        row, col = len(A), len(A[0])
        rst = [[0 for i in range(col)] for j in range(row)]
    
        for r in range(row):
            for c in range(  col - 1 , -1, -1):
                rst[r][c] = 1 if A[r][(col - c -1)] == 0 else 0 ###### 0 1 2 3 
            
        return rst