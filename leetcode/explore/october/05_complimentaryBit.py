class Solution:
	def bitwiseComplement(self, N: int) -> int:
		# xor with 2^n
		a = bin(N)[2:]
		n = len(a)
		return N ^(2**(n) - 1 )