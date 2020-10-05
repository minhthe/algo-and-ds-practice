'''https://assessments.hired.com/challenges/147822
'''

def solution(arr):
	ans = ""
	
	n =len(arr)	
	if n <= 1: return ans
	def f(pos):
		if pos >= n: return 0
		s = 0
		u, v= pos * 2 + 1, pos * 2 + 2
		
		if u < n and arr[u] != -1 :
			s = s + arr[u] + f(u)
		if v < n and arr[v] != -1 :
			s = s + arr[v] + f(v)
		return s

	
	left = f(1) + arr[1]
	right = f(2) + arr[2]
	print(left ,right)
	if left == right: return  ""
	if left < right: return  "Right"
	else: return  "Left"
	return ans