class WordDictionary:
    class Node:
        def __init__(self):
            self.children = {}
            self.is_eow = False

    def __init__(self):
        self.root = self.Node()

    def addWord(self, word: str) -> None:
        curr_node = self.root
        word_idx = 0
        while word_idx < len(word) and word[word_idx] in curr_node.children:
            curr_node = curr_node.children[word[word_idx]]
            if word_idx == len(word) - 1:
                curr_node.is_eow = True
            word_idx += 1
            
        while word_idx < len(word):
            child = self.Node()
            curr_node.children[word[word_idx]] = child
            curr_node = child
            if word_idx == len(word) - 1:
                curr_node.is_eow = True
            word_idx += 1
        

    def search(self, word: str) -> bool:
        def dfs(word_idx, curr_node):
            if word_idx == len(word):
                return True
            res = False
            c = word[word_idx]
            if c == '.':
                if word_idx == len(word) - 1:
                    for child_node in curr_node.children.values():
                        if child_node.is_eow:
                            res = True
                else:
                    for child_node in curr_node.children.values():
                        res = res or dfs(word_idx + 1, child_node)
            else:   # c is a specific letter
                if word_idx == len(word) - 1:
                    if c in curr_node.children:
                        res = curr_node.children[c].is_eow
                else:
                    if c in curr_node.children:
                        res = dfs(word_idx + 1, curr_node.children[c])
            return res

        return dfs(0, self.root)
