class Solution:
    def numDecodings(self, s: str) -> int:
        dp2 = 1
        dp1 = 1
        # setup
        if s[len(s) - 1] == '0':
            dp1 = 0
        
        for i in range(len(s) - 2, -1, -1):
            dp0 = 0
            if s[i] != '0':
                dp0 += dp1
                if int(s[i : i + 2]) < 27:
                    dp0 += dp2

            dp2 = dp1
            dp1 = dp0
                

        return dp1