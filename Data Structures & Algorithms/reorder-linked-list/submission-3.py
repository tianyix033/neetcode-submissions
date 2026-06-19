# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        if not head or not head.next:
            return head
        prev = head
        mid = head.next
        head.next = None
        while mid:
            nxt = mid.next
            mid.next = prev
            prev = mid
            mid = nxt
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        size = 0
        slow = head
        fast = head
        if not fast.next:
            return
        fast = fast.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        cur = slow.next
        slow.next = None
        cur = self.reverseList(cur)
        start = head
        while start.next:
            start_next = start.next
            start.next = cur
            cur_next = cur.next
            cur.next = start_next
            cur = cur_next
            start = start_next
        start.next = cur
        return 
        

        
        