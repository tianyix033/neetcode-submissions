# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0, None) # this is a sentinel node; discard at the end
        def helper(l1, l2, cur, add_one):
            if l1 and l2:
                next_val = (l1.val + l2.val + add_one) % 10
                add_one = (l1.val + l2.val + add_one) >= 10
                cur.next = ListNode(next_val)
                helper(l1.next, l2.next, cur.next, add_one)
            elif l1:
                next_val = (l1.val + add_one) % 10
                add_one = (l1.val + add_one) >= 10
                cur.next = ListNode(next_val)
                helper(l1.next, None, cur.next, add_one)
            elif l2:
                next_val = (l2.val + add_one) % 10
                add_one = (l2.val + add_one) >= 10
                cur.next = ListNode(next_val)
                helper(None, l2.next, cur.next, add_one)
            else:
                if add_one:
                    cur.next = ListNode(1)
            
        helper(l1, l2, res, 0)
        res = res.next
        return res
                