# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        tmp = dummyL = ListNode()

        dummyL.next = curr
        # set curr into place such that the gap is n
        count = 0
        while count < n:
            curr = curr.next
            count += 1

        # gap is now set
        while curr:
            curr = curr.next
            dummyL = dummyL.next

        dummyL.next = dummyL.next.next

        return tmp.next