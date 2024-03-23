# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        merged = current = head

        while current:
            if merged.val != current.val:
                merged.next = current
                merged = merged.next
            current = current.next

        if merged:
            merged.next = None
            
        return head