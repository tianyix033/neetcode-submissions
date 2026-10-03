from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordLen = len(beginWord)
        wordList.append(beginWord)
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        track = 0       # track 0 means begin, track 1 means end
        queue = {0: deque([beginWord]), 1: deque([endWord])}
        dist = 0
        visited = {0: set(), 1: set()}
        while queue[track]:
            
            for i in range(len(queue[track])):
                word = queue[track].popleft()
                if word in visited[1 - track]:
                    return dist
                if word in visited[track]:
                    continue
                visited[track].add(word)
                for j in range(wordLen):
                    for letter in range(ord('a'), ord('z') + 1):
                        # if letter == ord(word[j]):
                        #     continue
                        possible_word = word[:j] + chr(letter) + word[j + 1:]
                        if possible_word in wordSet and possible_word not in visited[track]:
                            queue[track].append(possible_word)
            dist += 1
                
            track = 0 if len(queue[0]) < len(queue[1]) else 1

        return 0