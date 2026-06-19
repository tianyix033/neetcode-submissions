# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        else:
            
            cur1 = list1
            cur2 = list2
            new_head = list1 if list1.val < list2.val else list2
            while cur1 and cur2:
                if cur1.val < cur2.val:
                    while cur1.next and cur1.next.val < cur2.val:
                        cur1 = cur1.next
                    cur1_next = cur1.next
                    cur1.next = cur2
                    cur1 = cur1_next
                else:
                    while cur2.next and cur2.next.val <= cur1.val:
                        cur2 = cur2.next
                    cur2_next = cur2.next
                    cur2.next = cur1
                    cur2 = cur2_next
            return new_head 
        
        
