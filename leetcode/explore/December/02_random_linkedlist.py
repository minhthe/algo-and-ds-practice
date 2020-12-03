import random
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.arr = []
        tmp = head
        while tmp:
            self.arr.append(tmp.val)
            tmp = tmp.next
        
        
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        return self.arr[ random.randint( 0, len(self.arr) - 1 ) ]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()