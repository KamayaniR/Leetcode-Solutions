"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        curr = root

        while curr.left:
            head = curr
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next 
            curr = curr.left 
        return root 


