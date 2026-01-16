# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        prev_node = None
        slow_pointer = head
        fast_pointer = head

        while fast_pointer is not None and fast_pointer.next is not None:
            prev_node = slow_pointer
            slow_pointer = slow_pointer.next 
            fast_pointer = fast_pointer.next.next
        
        prev_node.next = slow_pointer.next
        return head 
        