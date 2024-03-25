# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        d = {}
        while headA:
            val1 = headA.val
            if val1 not in d:
                d[val1] = [headA]
            elif headA in d[val1]:
                return headA
            else:
                d[val1].append(headA)
            
            headA = headA.next

        while headB:
            val2 = headB.val
            if val2 not in d:
                d[val2] = [headB]
            elif headB in d[val2]:
                return headB
            else:
                d[val2].append(headB)

            headB = headB.next
        
        return None