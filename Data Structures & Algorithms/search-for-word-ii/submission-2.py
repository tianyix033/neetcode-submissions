class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.refs = 0

    def addWord(self, word):
        for c in word:
            if c not in self.children:
                self.children[c] = TrieNode()
            self.refs += 1
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
                return 0
            char = board[r][c]
            visited.add((r, c))
            word.append(char)
            found = 0
            if node.children[char].isWord:
                found += 1
                res.add(''.join(word))
                node.children[char].isWord = False
                
            found += dfs(r + 1, c, node.children[char])
            found += dfs(r - 1, c, node.children[char])
            found += dfs(r, c + 1, node.children[char])
            found += dfs(r, c - 1, node.children[char])
            node.refs -= found
            if node.refs == 0:
                node.children = {}
            elif node.refs < 0:
                raise Exception("This shouldn't happen.")
            word.pop()
            visited.remove((r, c))
            return found

        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root)

        return list(res)
