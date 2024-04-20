class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append_head(self, new_head: Node):
        if not self.head:
            self.head = self.tail = new_head
        else:
            new_head.prev = None
            new_head.next = self.head
            self.head.prev = new_head
            self.head = new_head

        self.size += 1

    def remove(self, node: Node):
        # only node
        if node.prev == None and node.next == None:
            self.head = self.tail = None
        # if it's the head
        elif node == self.head:
            self.head = self.head.next
            self.head.prev = None
        # if tail
        elif node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        # if in middle
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        
        self.size -= 1

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.list = LL()

    def get(self, key: int) -> int:
        if key in self.cache:
            # move node to head
            node = self.cache[key]
            self.list.remove(node)
            self.list.append_head(node)

            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        # if key exists we remove prev node
        if key in self.cache:
            self.list.remove(self.cache[key])
        

        node = Node(key=key, val=value)
        self.list.append_head(node)
        self.cache[key] = node

        # remove last element
        if self.list.size > self.capacity:
            key_to_remove = self.list.tail.key
            node_to_remove = self.list.tail
            self.list.remove(node_to_remove)
            del self.cache[key_to_remove]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)