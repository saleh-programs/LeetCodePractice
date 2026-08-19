# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        current = head.next
        halfRef = head
        size, half = 1, 1

        end = ListNode(head.val, None)
        while current:
            size += 1
            if math.ceil(size/2) > half:
                half = math.ceil(size/2)
                halfRef = halfRef.next
            end = ListNode(current.val, end)
            current = current.next
        
        startPtr = head
        endPtr = end
        count = 0
        resultHead = ListNode()
        result = resultHead
        while count < size:
            if count % 2 == 0:
                result.next = startPtr
                startPtr = startPtr.next
            else:
                result.next = endPtr
                endPtr = endPtr.next
            count += 1
            result = result.next
        result.next = None
        head = resultHead.next
        while resultHead:
            print(resultHead.val)
            resultHead = resultHead.next
        

        

