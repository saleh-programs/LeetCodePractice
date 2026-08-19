# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        save = None
        prev = None

        while current != None:
            save = current.next
            current.next = prev
            prev = current
            current = save

        return prev