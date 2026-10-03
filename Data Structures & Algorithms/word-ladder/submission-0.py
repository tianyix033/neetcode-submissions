from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def are_adjacent(word1, word2):
            count = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    count += 1
                if count > 1:
                    return False
            return True
        wordList.append(beginWord)  
        adj = defaultdict(list)
        for i in range(len(wordList)):
            for j in range(i):
                word1, word2 = wordList[i], wordList[j]
                if are_adjacent(word1, word2):
                    adj[word1].append(word2)
                    adj[word2].append(word1)

        visited = set()
        queue = deque([beginWord])
        res = 0
        curr_size = 1
        next_size = 0
        while queue:
            res += 1
            for i in range(curr_size):
                word = queue.popleft()
                if word in visited:
                    continue
                visited.add(word)
                if word == endWord:
                    return res
                for neighbor in adj[word]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        next_size += 1

            curr_size = next_size
            next_size = 0

        return 0

        
