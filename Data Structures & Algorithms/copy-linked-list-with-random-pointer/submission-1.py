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
            return None
        orig_cursor = head
        mydict = {} # key is the node pointed to, val is its index
        old_arr = []
        new_arr = []
        length = 0
        while orig_cursor:
            old_arr.append(orig_cursor)
            mydict[orig_cursor] = length
            new_arr.append(Node(orig_cursor.val))
            orig_cursor = orig_cursor.next
            length += 1
        for i in range(length):
            old_node_rand = old_arr[i].random
            if old_node_rand:   # not null
                new_arr[i].random = new_arr[mydict[old_node_rand]]
        for i in range(length - 1):
            new_arr[i].next = new_arr[i + 1]
        return new_arr[0]

            