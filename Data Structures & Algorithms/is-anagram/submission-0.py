class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myDict = {}
        for char in s:
            if char not in myDict:
                myDict[char] = 1
            else:
                myDict[char] += 1
        for char in t:
            if char not in myDict:
                return False
            myDict[char] -= 1
        for key,value in myDict.items():
            if value != 0:
                return False
        return True

        