"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        cur = head
        while cur:
            next_node = cur.next
            cur.next = Node(cur.val, next_node)
            cur = next_node
        cur = head
        while cur:
            cur.next.random = (cur.random.next) if cur.random else None
            cur = cur.next.next
        cur = head
        new_head = cur.next
        while cur and cur.next:
            orig_next = cur.next
            cur.next = cur.next.next
            cur = orig_next
        return new_head