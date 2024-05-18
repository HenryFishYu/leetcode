class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        col_set = set()
        positive_diag = set()
        negative_diag = set()
        def backtrack(r: int):
            if r==n:
                nonlocal res
                res += 1
                return

            for c in range(n):
                if c in col_set or (r+c) in positive_diag or (r-c) in negative_diag:
                    continue

                col_set.add(c)
                positive_diag.add(r+c)
                negative_diag.add(r-c)
                backtrack(r+1)
                col_set.remove(c)
                positive_diag.remove(r + c)
                negative_diag.remove(r - c)

        backtrack(0)
        return res

print(Solution().totalNQueens(100))
