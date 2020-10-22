class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        
        for item in asteroids: 
            if not stk or stk[-1] < 0: stk.append(item)
            elif( item < 0 ):
                if stk and stk[-1] == abs(item): 
                    stk.pop()
                    continue
                while  stk and stk[-1] > 0 and  stk[-1] < abs(item) :
                    stk.pop()
                if stk and stk[-1] == abs(item): 
                    stk.pop()
                    continue                    
                if not stk or stk[-1] < 0   : stk.append(item)
                    
            else:        
                stk.append(item)
        return stk
        