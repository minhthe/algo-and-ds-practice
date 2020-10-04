'''https://leetcode.com/problems/01-matrix'''
import collections
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        row, col = len(matrix), len(matrix[0])
        
        visisted =  [ [False for j in range(col)] for i in range(row)] 
        
        que = collections.deque([])
        
        dx, dy  = [-1,1, 0 ,0 ], [0,0,-1,1]
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    que.append( (i,j,0) ) 
                    visisted[i][j] = True
        while que:
            
            
            
            r, c, val =  que.popleft()
            
            
            for i in range(4):
                x, y= dx[i]+ r,dy[i]+c
                if x in range(row) and y in range(col) and visisted[x][y] is False :
                    matrix[x][y] = val + 1
                    que.append(  ( x, y, val+1  ) )
                    visisted[x][y] = True
        return matrix