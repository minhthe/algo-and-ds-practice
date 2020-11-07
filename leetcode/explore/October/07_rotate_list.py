# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None: return 
        length_ll = 1 
        node = head
        while node.next:
            length_ll += 1
            node = node.next
        node.next = head 
        to_move = length_ll - (k % length_ll) 
        while to_move > 0 : 
            node = node.next
            to_move -= 1 
        head = node.next
        node.next = None 
        return head