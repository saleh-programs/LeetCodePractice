"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        
        newHead = Node(head.val, None)
        current = head
        current2 = newHead
        size = 1
        references = {head: 0}
        visited = {0: newHead}

        while current.next:
            size += 1
            current2.next = Node(current.next.val, None, None)
            references[current.next] = size-1
            visited[size-1] = current2.next
            current = current.next
            current2 = current2.next

        current = head
        current2 = newHead
        count = 0
        while current:
            count += 1
            if current.random:
                index = references[current.random]
                current2.random = visited[index]
            current = current.next
            current2 = current2.next
        
        return newHead        