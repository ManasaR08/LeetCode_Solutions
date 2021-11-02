class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        tmp = []
        rows = len(matrix)
        cols = len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                tmp.append(matrix[r][c])
        if target in tmp:
            return True
        else:
            return False
        