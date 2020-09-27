def spiral_copy(inputMatrix):
  row, col  = len(inputMatrix), len(inputMatrix[0])
  result = []
  side = 0 
  
  
  col0, col1 = 0 , col - 1
  row0, row1 = 0, row - 1
  

#  while row0 < row and row1 >= 0 and col1 >= 0 and col0 < col and row0 <= row1 and col0 <= col1:
  while row0 <= row1 and col0 <= col1:
    
    if side == 0:
      
      for c in range(col0, col1+1):
        #print(c)
        result.append(inputMatrix[row0][c])
      row0+=1
       # print(result)
    elif side ==1 :
      for r in range(row0, row1+1):
        result.append(inputMatrix[r][col1])
      col1-=1
      
    elif side ==2 :
      for c in range(col1, col0-1, -1):
        result.append(inputMatrix[row1][c])
      row1-=1
      
    else:
      for r in range(row1, row0-1, -1):
        result.append(inputMatrix[r][col0])
      col0+=1
    side = (side+1)%4  
  
  
  return result
  
inputMatrix =[[1,2,3,4,5],[6,7,8,9,10]] # row: 2, col 5
print(spiral_copy(inputMatrix))  