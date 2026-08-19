# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slowCurrent = head
        fastCurrent = head
        while fastCurrent and fastCurrent.next:
            slowCurrent = slowCurrent.next
            fastCurrent = fastCurrent.next.next
            if slowCurrent == fastCurrent:
                return True
        return False
