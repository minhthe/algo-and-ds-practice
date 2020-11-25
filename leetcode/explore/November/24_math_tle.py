class Solution:
	def calculate(self, s: str) -> int:
	
		nums =  []
		mul, div, neg = False, False, False
		num = ""
		i = 0 
		s = ''.join( c for c in list(s) if c !=" ")
		while i < len(s):

			while i< len(s) and s[i] in [str(i) for i in range(0,10)]: 
				num += s[i]
				i+=1			
				
			if len(nums) >= 1 and (mul or div ) :
				a = nums.pop()
				b = int(num)
				# print(mul,div)
				nums = nums + [a*b] if mul else nums + [int(a/b)]
				mul, div, neg = False, False, False
				num = ""
		
			if i < len(s) and  s[i] == "*" : mul = True			
			if i < len(s) and s[i] == "/": div = True					
			if len(num) : nums  = nums + [ - int(num)] if neg else nums + [ int(num)]
			if neg : neg = False
			if i < len(s) and  s[i] == "-": neg = True	
			num = ""		
			i += 1
		
		return sum(nums)