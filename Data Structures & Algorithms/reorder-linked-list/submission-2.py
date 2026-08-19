# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return 

        current = head
        half = [None, 0, None]
        oddVal = None
        size = 0
        while current:
            size += 1
            if size // 2 > half[1]:
                half[1] += 1
                half[2] = half[0]
                if not half[0]:
                    half[0] = current
                else:
                    half[0] = half[0].next
            current = current.next

        if size % 2 != 0:
            oddVal = half[0]
            half[0] = half[0].next
            if half[2]:
                half[2].next = None
        
        current = half[0]
        prev = None
        while current:
            backdoor = current.next
            current.next = prev
            prev = current
            current = backdoor
        rightHead = prev

        start = ListNode()
        dummy = start
        for _ in range(size//2):
            a, b = head, rightHead
            head = head.next
            rightHead = rightHead.next

            dummy.next = a
            a.next = b 
            dummy = b
        if oddVal:
            dummy.next = oddVal
            oddVal.next = None
            

