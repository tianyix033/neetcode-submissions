# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:  # Base case: empty list or single node
            return head
        new_head = self.reverseList(head.next)  # Reverse the rest
        head.next.next = head  # Reverse the link between current node and next node
        head.next = None        # Break the original link
        return new_head         # Propagate the new head