# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#https://app.codility.com/demo/results/training6FDFVU-76B/
def solution(A):
    # write your code in Python 3.6
    missing_number = A[0]
    for i in range(1, len(A)):
        missing_number ^= A[i]
    return missing_number