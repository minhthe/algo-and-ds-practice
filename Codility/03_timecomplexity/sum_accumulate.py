# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    pass
    n = len(A)
    left = [0] * (n)
    right = [0] * n 
    
    left[0] = A[0]
    right[-1] = A[-1]
    for i in range(1,n):
        left[i] = left[i-1] + A[i]
    for i in range(n-2,-1, -1):
        right[i] = right[i+1] + A[i]        
    min_v = int(1e9)
    for i in range(1, n):
        min_v = min(min_v, abs(left[i-1] - right[i] ))
    return min_v