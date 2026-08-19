# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        beforeTail = current
        tail = current
        distance = 0
        while current:
            current = current.next
            if distance < n:
                distance += 1
            else:
                beforeTail = tail
                tail = tail.next
        if head == tail and n == 1:
            return None
        elif head == tail and n > 1:
            return tail.next
        else:
            beforeTail.next = tail.next
        return head
