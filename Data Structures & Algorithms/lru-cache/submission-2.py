class LRUCache:
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.hashmap = {}   # key: node
        self.lst = LinkedList()


    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.lst.move_to_end(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.value = value
            self.lst.move_to_end(node)
        else:
            if self.size == self.capacity:
                head = self.lst.remove_head()
                del self.hashmap[head.key]
            else:
                self.size += 1
            node = self.lst.append_node(key, value)
            self.hashmap[key] = node


class LinkedList:
    class Node:
        def __init__(self, key, value, prev=None, next=None):
            self.key = key
            self.value = value
            self.prev = prev
            self.next = next

    def __init__(self):
        self.end = self.Node(None, None)   # sentinel trailer node
        self.start = self.Node(None, None, next=self.end) # sentinel header node
        self.end.prev = self.start

    def move_to_end(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = node.next
        next_node.prev = node.prev
        node.prev = self.end.prev
        node.next = self.end
        self.end.prev.next = node
        self.end.prev = node

    def append_node(self, key, value):
        node = self.Node(key, value, prev=self.end.prev, next=self.end)
        self.end.prev.next = node
        self.end.prev = node
        return node

    def remove_head(self):
        head = self.start.next
        self.start.next = head.next
        head.next.prev = self.start
        return head


        
