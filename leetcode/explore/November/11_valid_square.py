class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        store = set()
        #p1 p2         
        store.add(  (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2   )
        
        #p1 p3        
        store.add(  (p1[0] - p3[0])**2 + (p1[1] - p3[1])**2   )
        
        #p1 p4
        store.add(  (p1[0] - p4[0])**2 + (p1[1] - p4[1])**2   )
        
        #p2 p3
        store.add(  (p2[0] - p3[0])**2 + (p2[1] - p3[1])**2   )        
        
        #p2 p4
        store.add(  (p2[0] - p4[0])**2 + (p2[1] - p4[1])**2   )
              
        #p3 p4 
        store.add(  (p3[0] - p4[0])**2 + (p3[1] - p4[1])**2   )
        
        
        return len(store) == 2 and 0 not in store