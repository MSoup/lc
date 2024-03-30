class Node:
    def __init__(self, key = None, val = 0):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:
    def __init__(self):
        self.head = Node()

    def put(self, key: int, value: int) -> None:        
        curr = self.head
        while curr:
            if curr.key == key:
                curr.val = value
                return

            if curr.next is None:
                curr.next = Node(key, value)
                return

            curr = curr.next
        
        

    def get(self, key: int) -> int:
        curr = self.head
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        curr = self.head
        prev = None
        while curr:
            prev = curr
            curr = curr.next

            if curr and curr.key == key:
                prev.next = curr.next
                break
        



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)