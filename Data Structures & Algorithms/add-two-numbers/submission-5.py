# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        current1 = l1
        value1 = 0
        magnitude = 1
        while current1 != None:
            value1 += current1.val * magnitude
            current1 = current1.next
            magnitude *= 10
    

        current2 = l2
        value2 = 0
        magnitude = 1
        while current2 != None:
            value2 += current2.val * magnitude
            current2 = current2.next
            magnitude *= 10

        number = value1 + value2
        if number == 0:
            return ListNode(0,None)

        digits = len(str(number))
        magnitude = 10 ** (digits - 1)
        prev = None

        print(number, magnitude)
        while digits != 0:

            value = number // magnitude
            number -= (value * magnitude)
            digits -= 1
            magnitude //= 10

            newNode = ListNode(value, prev)
            prev = newNode
        
        return prev
