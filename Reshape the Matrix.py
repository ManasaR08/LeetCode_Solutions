class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        if rows * cols != r * c:
            return mat
        temp = []
        result = [ [ 0 for i in range(c) ] for j in range(r) ]
        for i in range(rows):
            for j in range(cols):
                temp.append(mat[i][j])
        print(temp)
        val = 0
        for p in range(r):
            for q in range(c):
                result[p][q] = temp[val]
                val += 1
        return result 
                
                
        