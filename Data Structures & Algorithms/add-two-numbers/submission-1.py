# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # intuitive, but garbage, but cheating with python a lot

        result = ListNode()
        current = result
        carry = 0
        while l1 or l2 or carry:
            op1 = 0
            op2 = 0
            if l1:
                op1 = l1.val
                l1 = l1.next
            if l2:
                op2 = l2.val
                l2 = l2.next
            total = op1 + op2 + carry
            carry = 0
            if total > 9:
                total = total % 10
                carry = 1
            current.next = ListNode(total)
            current = current.next
        return result.next


