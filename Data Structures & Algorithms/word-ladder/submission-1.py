from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordLen = len(wordList[0])
        wordList.append(beginWord)
        patterns = defaultdict(list)
        for word in wordList:
            for i in range(wordLen):
                pattern = word[:i] + '*' + word[i + 1:]
                patterns[pattern].append(word)
        # print(patterns)

        visited = set()
        queue = deque([beginWord])
        res = 0
        while queue:
            res += 1
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                if word in visited:
                    continue
                visited.add(word)
                for j in range(wordLen):
                    pattern = word[:j] + '*' + word[j + 1:]
                    for neighbor in patterns[pattern]:
                        if neighbor not in visited:
                            queue.append(neighbor)
        return 0

                    
