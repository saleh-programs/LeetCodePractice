class Node():
    def __init__(self, neighbors=None, value=None):
        self.neighbors = neighbors if neighbors is not None else {}
        self.value = value
        self.isWord = False

class PrefixTree:
    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        current = self.head
        substr = ""
        for ch in word:
            if ch in current.neighbors:
                current = current.neighbors[ch]
            else:
                current.neighbors[ch] = Node(value=ch)
                current = current.neighbors[ch]
        current.isWord = True

    def search(self, word: str) -> bool:
        current = self.head

        for ch in word:
            if ch not in current.neighbors:
                return False
            current = current.neighbors[ch]
        return current.isWord

    def startsWith(self, prefix: str) -> bool:
        current = self.head
        for ch in prefix:
            if ch not in current.neighbors:
                return False
            current = current.neighbors[ch]
        return True