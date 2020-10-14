'''https://leetcode.com/problems/valid-palindrome/'''
class Solution:
	def isPalindrome(self, s: str) -> bool:
		ans = True
		left, right = 0, len(s) - 1
		
		while left<right:
			ll, rr = s[left], s[right]
			if not(ord("a")  <=   ord(ll.lower()) <= ord("z") or ord("0")  <=   ord(ll.lower()) <= ord("9") )  : 
				left+=1
				continue
			if not (ord("a")  <=   ord(rr.lower()) <= ord("z")  or ord("0")  <=   ord(rr.lower()) <= ord("9")): 
				right -= 1
				continue
			if ll.lower() != rr.lower(): return False
			left += 1
			right -= 1
		return ans