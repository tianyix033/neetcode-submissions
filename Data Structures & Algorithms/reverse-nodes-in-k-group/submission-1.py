# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = ListNode(-1, head)
        curr_head = head
        prev_tail = res
        while True:
            next_head = curr_head
            counter = 0
            while next_head is not None and counter < k:
                next_head = next_head.next
                counter += 1
            if counter < k:
                prev_tail.next = curr_head
                return res.next
            node_1 = curr_head
            node_2 = curr_head.next
            counter = 1 # we'll reverse head in next iter, so count this in
            while counter < k:
                node_3 = node_2.next
                node_2.next = node_1
                node_1 = node_2
                node_2 = node_3
                counter += 1
            prev_tail.next = node_1
            prev_tail = curr_head
            curr_head = next_head
        return res.next
            
            
