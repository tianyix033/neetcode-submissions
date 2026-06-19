class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(arr, left_count):
            if len(arr) == 2 * n:
                res.append("".join(arr))
                return
            if left_count == n:   # we used all ( allowed
                arr.append(")")
                helper(arr, left_count)
                arr.pop()
            elif 2 * left_count == len(arr):     # must have ( next for legal expression
                arr.append("(")
                helper(arr, left_count + 1)
                arr.pop()
            else:
                arr.append("(")
                helper(arr, left_count + 1)
                arr.pop()
                arr.append(")")
                helper(arr, left_count)
                arr.pop()

        helper([], 0)
        return res
        