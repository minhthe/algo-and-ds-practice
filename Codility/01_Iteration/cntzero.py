'''https://app.codility.com/demo/results/training4C2JRM-36Q/'''
def solution(N):
    bin_arr = list(bin(N)[2:])
    cnt = 0 
    start = 0
    for end,v in enumerate(bin_arr):
        if end == 0: continue
        if v == '1':  # 1 0 0 1
            cnt = max(cnt, end - start - 1 )
            start = end
    
    return cnt