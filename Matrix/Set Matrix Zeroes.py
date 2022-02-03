class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        foundZeroes = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    foundZeroes.append((i, j))
                    
        setZeroes = set()
        
        for zero in foundZeroes:
            (i, j) = zero
            for k in range(len(matrix)):
                matrix[k][j] = 0
                
            for k in range(len(matrix[0])):
                matrix[i][k] = 0
                
        return matrix
        
        
                    
        
            