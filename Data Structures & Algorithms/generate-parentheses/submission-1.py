class Solution:
        def generateParenthesis(self, n: int) -> List[str]:
            dp = [[] for _ in range(n + 1)]
            dp[0] = [""]
            for k in range(n + 1):
                for i in range(k):
                    for left in dp[i]:
                        for right in dp[k - i - 1]:
                            dp[k].append(f'({left}){right}')
            return dp[n]
            
