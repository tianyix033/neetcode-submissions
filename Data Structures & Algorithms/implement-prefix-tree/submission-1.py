class PrefixTree:
    class Node:
        def __init__(self, val, eow=False):
            self.val = val
            self.children = {}  # char: node
            self.is_eow = eow

    def __init__(self):
        self.root = self.Node(None)  # sentinel root node

    def insert(self, word: str) -> None:
        i = 0
        cursor = self.root
        matches_this_round = True
        while word[i] in cursor.children:
            if i == len(word) - 1:
                cursor.children[word[i]].is_eow = True
                return
            cursor = cursor.children[word[i]]
            i += 1
        while i < len(word):
            node = self.Node(word[i], eow=(i == len(word) - 1))
            cursor.children[word[i]] = node
            cursor = node
            i += 1          

    def search(self, word: str) -> bool:
        return self.query(word, False)

    def startsWith(self, prefix: str) -> bool:
        return self.query(prefix, True)

    def query(self, word, is_prefix):
        cursor = self.root
        for i, c in enumerate(word):
            if c in cursor.children:
                next_node = cursor.children[c]
                if i == len(word) - 1:
                    return True if is_prefix else next_node.is_eow
                else:
                    cursor = next_node
            else:
                return False
        
        