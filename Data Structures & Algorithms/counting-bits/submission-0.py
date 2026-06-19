class Solution:
    def countBits(self, n: int) -> List[int]:
        def countBitsSingle(num):
            count = 0
            while num:
                count += num & 1
                num = num>>1
            return count
        
        res = []
        for i in range(n + 1):
            res.append(countBitsSingle(i))
        
        return res
        