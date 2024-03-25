# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        current = dummy

        while current:
            prev = current
            current = current.next
            while current and current.val == val:
                current = current.next
            prev.next = current
        
        return dummy.next