# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        sortedHead = None
        if list1 and list2:
            if list1.val <= list2.val:
                sortedHead = list1
                list1 = list1.next
            else:
                sortedHead = list2
                list2 = list2.next
        elif not list1 and list2:
            return list2
        else:
            return list1

        current = sortedHead

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        notEmpty = list2 if not list1 else list1
        current.next = notEmpty

        return sortedHead