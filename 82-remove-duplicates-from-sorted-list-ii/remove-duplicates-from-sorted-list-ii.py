# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode()
        tmp = prev
        curr = head
        prev.next = curr
        d = {}
        while curr:
            if curr.val not in d:
                d[curr.val] = 0
            d[curr.val] += 1
            curr = curr.next
        
        curr = head
        while curr:
            while curr and d[curr.val] > 1:
                curr = curr.next
            prev.next = curr
            if curr:
                curr = curr.next
                prev = prev.next

        return tmp.next
            