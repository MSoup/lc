# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = prev = ListNode(-1, head)
        curr = head

        while curr and curr.next:
            # save a reference to the next pair
            nextPair = curr.next.next
            nextNode = curr.next

            nextNode.next = curr
            curr.next = nextPair
            prev.next = nextNode
            
            
            prev = curr
            curr = nextPair
            
        return tmp.next