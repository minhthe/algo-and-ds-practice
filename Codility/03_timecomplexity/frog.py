# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # write your code in Python 3.6
    pass
    tmp = (Y - X)/ D
    if tmp == int(tmp): return int(tmp)
    else: return int(tmp) + 1