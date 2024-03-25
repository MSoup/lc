# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # a cycle exists if a slow pointer reaches a fast pointer eventually, and there is no cycle if a fast pointer reaches the end
        slow = current = head
        if not head:
            return False
            
        while current.next and current.next.next:
            current = current.next.next
            slow = slow.next

            if current == slow:
                return True
        return False