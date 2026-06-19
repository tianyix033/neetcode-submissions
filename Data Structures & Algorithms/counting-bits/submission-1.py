class Solution:
    def countBits(self, n):
        res = [0]
        for i in range(1, n + 1):
            prev = res[-1]
            test = i ^ (i - 1)
            if test == 1:
                res.append(prev + (i & 1))
            else:
                val = 0
                while test:
                    test >>= 1
                    val += 1
                res.append(prev - val + 2)
        return res
        