class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        def matrix_mult(a, b):
            return [[a[0][0] * b[0][0] + a[0][1] * b[1][0],\
             a[0][0] * b[0][1] + a[0][1] * b[1][1]],\
             [a[1][0] * b[0][0] + a[1][1] * b[1][0],
             a[1][0] * b[0][1] + a[1][1] * b[1][1]]]

        def matrix_pow(m, n):
            if n == 1:
                return m

            base = matrix_pow(m, n // 2)
            extra = [[1, 0], [0, 1]]
            if n % 2 == 1:
                extra = m
            return matrix_mult(matrix_mult(base, base), extra)

        return matrix_pow([[1, 1], [1, 0]], n)[0][0]
                    