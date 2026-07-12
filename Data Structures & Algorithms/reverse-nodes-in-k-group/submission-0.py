# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        next_head = head
        counter = 0
        while next_head is not None and counter < k:
            next_head = next_head.next
            counter += 1
        if counter < k:
            return head
        node_1 = head
        node_2 = head.next
        counter = 1 # we'll reverse head last, so count this in
        while counter < k:
            node_3 = node_2.next
            node_2.next = node_1
            node_1 = node_2
            node_2 = node_3
            counter += 1
        head.next = self.reverseKGroup(next_head, k)
        return node_1


            
            