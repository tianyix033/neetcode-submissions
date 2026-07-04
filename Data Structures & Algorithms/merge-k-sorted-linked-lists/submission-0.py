# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        mins = []
        res = ListNode()    # sentinel header
        cur = res
        counter = 0
        for node in lists:
            if node:
                heapq.heappush(mins, (node.val, counter, node))
                counter += 1
        while mins:
            min_val, c, min_node = heapq.heappop(mins)
            counter += 1
            cur.next = ListNode(min_val)
            cur = cur.next
            if min_node.next:
                heapq.heappush(mins, (min_node.next.val, counter, min_node.next))
                counter += 1
        return res.next

        