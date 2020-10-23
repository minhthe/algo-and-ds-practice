# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#https://app.codility.com/demo/results/trainingU3JNHR-YUR/
def solution(A, K):
    # write your code in Python 3.6
    pass    
    n = len(A)
    if n ==0 : return A   
    pos = K % n 
    first = n - pos
    return A[first:] + A[:first]