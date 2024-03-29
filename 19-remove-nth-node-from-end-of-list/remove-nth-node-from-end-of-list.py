# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        tmp = dummy = ListNode()
        tmp.next = curr
        
        for _ in range(n): 
            if not curr:
                return head
            curr = curr.next

        while curr:
            curr = curr.next
            tmp = tmp.next

        tmp.next = tmp.next.next

        return dummy.next