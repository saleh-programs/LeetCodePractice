class doublyNode():
    def __init__(self, val=0, to=None,prev=None):
        self.val = val
        self.to = to
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.storage = {}
        self.LRU = None
        self.MRU = None        

    def get(self, key: int) -> int:
        if key in self.storage:
            val = self.storage[key][0]
            node = self.storage[key][1]

            if len(self.storage) == 1 or node == self.MRU:
                
                return val
            if node == self.LRU:
                self.LRU = self.LRU.to
                self.MRU = self.MRU.to
                
                return val
            
            node.prev.to = node.to
            node.to.prev = node.prev

            node.to = self.LRU
            node.prev = self.MRU
            self.MRU.to = node
            self.MRU = node
            
            return val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.storage:
            newNode = doublyNode(key, None, None)
            if not self.LRU:
                self.LRU = newNode
                self.MRU = newNode
                self.LRU.prev = newNode
                self.LRU.to = newNode
            else:
                self.MRU.to = newNode
                newNode.prev = self.MRU
                newNode.to = self.LRU
                self.MRU = newNode
                self.LRU.prev = self.MRU
            self.storage[key] = [value, newNode]

            if len(self.storage) > self.capacity:
                val = self.storage[self.LRU.val]
                del self.storage[self.LRU.val]
                self.LRU = self.LRU.to   
                self.MRU.to = self.LRU            
        else:
            self.storage[key][0] = value
            node = self.storage[key][1]

            if len(self.storage) == 1 or node == self.MRU:
                
                return
            if node == self.LRU:
                self.LRU = self.LRU.to
                self.MRU = self.MRU.to
                
                return
            
            node.prev.to = node.to
            node.to.prev = node.prev

            node.to = self.LRU
            node.prev = self.MRU
            self.MRU.to = node
            self.MRU = node
            
