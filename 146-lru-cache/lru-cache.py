class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.capacity = 0

    def append(self, node: Node):
        # appending as the only node
        if not self.head:
            self.head = self.tail = node

        # head and tail are the same
        elif self.head == self.tail:
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.head.next = self.tail

        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

        self.capacity += 1

    def remove(self, node: Node):
        # given a node that exists in this list, remove it
        # the only node
        if self.head == node and self.tail == node:
            self.head = self.tail = None

        elif self.head == node:
            self.head = self.head.next
            self.head.prev = None

        elif self.tail == node:
            self.tail = self.tail.prev
            self.tail.next = None

        else:
            # middle
            node.prev.next = node.next
            node.next.prev = node.prev

        self.capacity -= 1


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.list = LinkedList()

    def get(self, key):
        if key in self.cache:
            node_to_refresh = self.cache[key]
            self.list.remove(node_to_refresh)
            self.list.append(node_to_refresh)
            return self.cache[key].val
        return -1

    def put(self, key, val):
        node = Node(key, val)
        if key not in self.cache:
            self.cache[key] = node
            self.list.append(node)
        else:
            # key is in cache
            node_to_remove = self.cache[key]
            self.list.remove(node_to_remove)
            self.list.append(node)
            self.cache[key] = node

        if self.list.capacity > self.capacity:
            del self.cache[self.list.tail.key]
            self.list.remove(self.list.tail)
