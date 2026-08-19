class Node():
    def __init__(self, neighbors=None, value=None):
        self.neighbors = neighbors if neighbors is not None else {}
        self.value = value

class PrefixTree:
    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        current = self.head
        substr = ""
        for ch in word:
            substr += ch
            if substr in current.neighbors:
                current = current.neighbors[substr]
            else:
                current.neighbors[substr] = Node(value=substr)
                current = current.neighbors[substr]
        if substr in current.neighbors:
            return
        current.neighbors[substr] = Node(value=substr)

    def search(self, word: str) -> bool:
        current = self.head
        substr = ""

        for ch in word:
            substr += ch
            if substr not in current.neighbors:
                return False
            current = current.neighbors[substr]
        return substr in current.neighbors

    def startsWith(self, prefix: str) -> bool:
        current = self.head
        substr = ""
        for ch in prefix:
            substr += ch
            if substr not in current.neighbors:
                return False
            current = current.neighbors[substr]
        return True