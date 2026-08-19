# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # intuitive, but garbage, but cheating with python a lil
        
        str1 = ""
        str2 = ""

        while l1:
            str1 += str(l1.val)
            l1 = l1.next
        while l2:
            str2 += str(l2.val)
            l2 = l2.next
        result = int(str1[::-1]) + int(str2[::-1])
        head = None
        for digit in str(result):
            head = ListNode(int(digit), head)
        return head
            
