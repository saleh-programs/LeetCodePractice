# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        size = 0
        current = head
        endHead = head
        while current:
            size += 1
            current = current.next
            if size % k == 0:
                endHead = current
        groupSize = size - size % k
        if size == groupSize:
            endHead = None

        at = 0
        current = head
        prev = None
        groupHead = head
        mainHead = None
        priorGroup = None
        while current != endHead:
            at += 1
            backdoor = current.next
            current.next = prev
            prev = current
            current = backdoor
            if at % k == 0:
                if priorGroup:
                    priorGroup.next = prev
                priorGroup = groupHead
                groupHead.next = current
                groupHead = current
                if not mainHead:
                    mainHead = prev
        return mainHead




        