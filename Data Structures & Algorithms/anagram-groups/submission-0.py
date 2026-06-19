class Solution:
    def mapIntoFrozenSet(self, word):
        myDict = {}
        for char in word:
            if char not in myDict:
                myDict[char] = 1
            else:
                myDict[char] += 1
        return frozenset(myDict.items())
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictOfSets = {}
        for subString in strs:
            tempSet = self.mapIntoFrozenSet(subString)
            if tempSet not in dictOfSets:
                dictOfSets[tempSet] = [subString]
            else:
                dictOfSets[tempSet].append(subString)
        listOfLists = []
        for values in dictOfSets.values():
            listOfLists.append(values)
        return listOfLists
        