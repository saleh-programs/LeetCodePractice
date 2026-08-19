# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        current = head
        while True:
            minVal = [float("inf"), None]
            for i in range(len(lists)):
                if lists[i]:
                    val = lists[i].val
                    if val <= minVal[0]:
                        minVal[0] = val
                        minVal[1] = i
            if minVal[1] is None:
                break
            else:
                current.next = lists[minVal[1]]
                current = current.next        
                lists[minVal[1]] = lists[minVal[1]].next

        return head.next


                
            
            