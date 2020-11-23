class Solution:
	def uniqueMorseRepresentations(self, words: List[str]) -> int:
		morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
		
		rst =  set()
		
		def f(s):
			ans = ""
			for letter in s:
				idx = ord(letter) - ord("a")
				ans += morse[idx] 
			return ans		
				
		for word in words:
			rst.add(f(word))
		
		return len(rst)