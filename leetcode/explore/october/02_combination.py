class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        tmp, rst = [], []
        pos = 0 
        mp= {}
        def generate(tmp, rst, pos):
        
            if pos >= len(candidates) or sum(tmp) > target : return
            
            
            if sum(tmp) == target and ''.join(str(item) for item in sorted(tuple(tmp))) not in mp:
                rst.append(tmp[:])
                mp[''.join(str(item) for item in sorted(tuple(tmp)))] = True
                
            for i in range(0, len(candidates)):
                tmp.append(candidates[i])
                generate(tmp, rst, i)
                tmp.pop()
            return rst
                
                
        generate(tmp, rst, pos)
        return rst