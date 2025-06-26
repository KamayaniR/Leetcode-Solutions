# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = ListNode(0,head)
        dummy = curr
        fast = head

        for i in range(n):
            fast = fast.next
        while fast:
            fast = fast.next
            dummy = dummy.next

        dummy.next = dummy.next.next
        return curr.next



