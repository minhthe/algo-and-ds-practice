'''https://leetcode.com/problems/basic-calculator-ii'''
class Solution:
    def calculate(self, s: str) -> int:
        rst = 0 
        stk = []
        op =  "+"
        cur = 0 
        
        for i, c in enumerate(s):
            
            if c.isdigit():
                cur = cur*10 + int(c)
            
            if c.isdigit() is False and c != " " or (i == len(s) -1):
                
                if op == "+":
                    stk.append(cur)
                elif op == "-":
                    stk.append(-cur)
                elif op == "*":
                    stk.append(cur*(stk.pop()))
                else:
                    stk.append(int(stk.pop() / cur))                
                op = c
                cur = 0 
        return sum(stk)