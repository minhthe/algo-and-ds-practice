import collections
class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        arr = collections.deque(tokens)
        if not arr or arr[0] > P : return 0
        P = P - arr[0]
        arr.popleft()
        score = 1
        max_v = 1
        while arr:
            if arr[0] > P:
                score -= 1 
                P += arr[-1]
                arr.pop()
            else:
                
                score += 1
                P -= arr[0]
                arr.popleft()
                max_v = max(max_v, score)
        
        
        
        
        return max_v