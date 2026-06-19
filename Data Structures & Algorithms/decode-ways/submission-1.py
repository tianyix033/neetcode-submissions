class Solution:
    def numDecodings(self, s: str) -> int:
        # last character alone is always decodable; serves as base case
        cache = {} 
        def isvalid(pos, size):   # checks s[pos:pos+size] is valid
            if pos >= len(s):
                return 0
            if s[pos] == '0':
                return 0
            return int(int(s[pos:pos + size]) < 27)

        def decodable(start_i):
            if start_i in cache:
                return cache[start_i]
            if start_i == len(s):
                return 1
            if start_i == len(s) - 1:
                return isvalid(start_i, 1)
            res = (isvalid(start_i, 1) * decodable(start_i + 1)) + (isvalid(start_i, 2) * decodable(start_i + 2))
            cache[start_i] = res
            return res

        return decodable(0)
            
        
        