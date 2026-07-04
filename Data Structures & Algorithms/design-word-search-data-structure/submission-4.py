class WordDictionary:
    class Node:
        def __init__(self):
            self.children = {}
            self.is_eow = False

    def __init__(self):
        self.root = self.Node()

    def addWord(self, word: str) -> None:
        curr_node = self.root
        for c in word:
            if c not in curr_node.children:
                curr_node.children[c] = self.Node()
            curr_node = curr_node.children[c]
        curr_node.is_eow = True
        

    def search(self, word: str) -> bool:
        def dfs(word_idx, curr_node):
            if word_idx == len(word):
                return curr_node.is_eow
            res = False
            c = word[word_idx]
            if c == '.':
                for child_node in curr_node.children.values():
                    res = res or dfs(word_idx + 1, child_node)
            else:   # c is a specific letter
                if c in curr_node.children:
                    res = dfs(word_idx + 1, curr_node.children[c])
            return res

        return dfs(0, self.root)
