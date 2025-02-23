# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
    
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow is now at middle
        head2 = slow.next
        slow.next = None
        head2 = self.reverse(head2)

        curr = head
        while head2:
            next1 = curr.next
            next2 = head2.next
            curr.next = head2
            head2.next = next1
            curr = next1
            head2 = next2
        return head

    def reverse(self, node):
        prev = None
        current = node
        while current:
            next_temp = current.next  # Save next node
            current.next = prev       # Reverse the link
            prev = current           # Move prev forward
            current = next_temp      # Move current forward
        return prev

    def print_LL(self, node):
        while node:
            print(node.val, end=",")
            node = node.next
        print("Finished")
        