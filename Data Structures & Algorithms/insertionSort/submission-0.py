# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = []
        for i in range(len(pairs)):
            if (i > 0) and (pairs[i].key < pairs[i-1].key):
                temp = pairs[i]
                j = i - 1
                while (j >= 0) and (temp.key < pairs[j].key):
                    pairs[j+1] = pairs[j]
                    j -= 1
                pairs[j + 1] = temp
            res.append(pairs.copy())
        return res

        