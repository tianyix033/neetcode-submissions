class Solution:
    def countBits(self, n):
        res = [0]
        offset = 0
        for i in range(1, n + 1):
            if (i >= (2 * offset)):
                offset = i
            res.append(1 + res[i - offset])
        return res
        