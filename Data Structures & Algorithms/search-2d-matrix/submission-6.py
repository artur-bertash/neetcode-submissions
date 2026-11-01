class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        l, r = 0, len(matrix) * len(matrix[0]) - 1

        while l <= r:
            m = (l + r) // 2
            el = matrix[m // len(matrix[0])][m % len(matrix[0])]

            if el < target:
                l = m + 1
            elif el > target:
                r = m - 1
            else:
                return True
        return False