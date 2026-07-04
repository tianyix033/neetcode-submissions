# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2Lists(list1, list2):
            res = ListNode()
            cur = res
            while list1 and list2:
                if list1.val < list2.val:
                    cur.next = ListNode(list1.val)
                    list1 = list1.next
                else:
                    cur.next = ListNode(list2.val)
                    list2 = list2.next
                cur = cur.next
            if not list1:
                cur.next = list2
            else:
                cur.next = list1
            return res.next
        
        res = []
        while len(lists) > 1:
            for i in range(0, len(lists) - 1, 2):
                lists[i] = merge2Lists(lists[i], lists[i + 1])
            lists = [lists[i] for i in range(0, len(lists), 2)]
        
        return lists[0] if lists else None
