class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        for c in word:
            if c not in self.children:
                self.children[c] = TrieNode()
            self = self.children[c]
        self.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        root = TrieNode()
        for word in words:
            root.addWord(word)
        visited = set()
        res = set()
        word = []
        
        def dfs(r, c, node):
            if (not (0 <= r < rows) or not (0 <= c < cols) or (r, c) in visited or board[r][c] not in node.children):
                return
            char = board[r][c]
            visited.add((r, c))
            word.append(char)
            if node.children[char].isWord:
                res.add(''.join(word))
            dfs(r + 1, c, node.children[char])
            dfs(r - 1, c, node.children[char])
            dfs(r, c + 1, node.children[char])
            dfs(r, c - 1, node.children[char])
            word.pop()
            visited.remove((r, c))

        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root)

        return list(res)
