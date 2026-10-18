from collections import defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if len(words) == 1:
            return "".join(list(set(words[0])))
        left = 0
        right = 1
        biggerChars = defaultdict(list)   # biggerChars[i] contains a list of all bigger chars
        smallerCount = defaultdict(int)     # smallerCount[i] counts number of chars smaller
        while right < len(words):
            for i in range(len(words[left])):
                if i == len(words[right]):
                    return ""
                leftChar, rightChar = words[left][i], words[right][i]
                if leftChar != rightChar:
                    biggerChars[leftChar].append(rightChar)
                    smallerCount[rightChar] += 1
                    break
            right += 1
            left += 1

        stack = []
        allChars = set([char for word in words for char in word])
        for char in allChars:
            if smallerCount[char] == 0:
                stack.append(char)
        res = []        
        while stack:
            char = stack.pop()
            res.append(char)
            for bigger in biggerChars[char]:
                smallerCount[bigger] -= 1
                if smallerCount[bigger] == 0:
                    stack.append(bigger)

        for count in smallerCount.values():
            if count > 0:
                return ""

        return "".join(res)



                