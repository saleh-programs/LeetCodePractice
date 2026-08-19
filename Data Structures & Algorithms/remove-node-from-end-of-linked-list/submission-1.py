# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        current = head
        while current:
            size += 1
            current = current.next

        removal = (size + 1) - n
        current = head
        if n == size:
            return head.next

        for i in range(removal-2):
            current = current.next

        if n == 1 and size == 1:
            return None
        else:
            current.next = current.next.next
            return head
