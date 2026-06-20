class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        partition = []
        def helper(i):
            if i >= len(s):
                res.append(partition.copy())
                return
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    partition.append(s[i : j + 1])
                    helper(j + 1)
                    partition.pop()

        helper(0)
        return res

    def isPalindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
        