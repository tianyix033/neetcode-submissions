class Solution:
    
    def isHappy(self, n: int) -> bool:
        visited = set()
        def helper(n):
            if n == 1:
                return True
            if n in visited:
                return False
            # print(n)
            visited.add(n)
            square = [int(i) ** 2 for i in str(n)]
            return helper(sum(square))
        return helper(n)
        