class Solution:
	def getDecimalValue(self, head: ListNode) -> int:
		
		rst =  0
		while head:
			rst = rst * (2) + head.val	
			head = head.next
		return rst