class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        is_col = False
        
        # 1. Scan the matrix and mark rows/cols using the first row/col
        for r in range(rows):
            # Check if the first column specifically needs to be zeroed out
            if matrix[r][0] == 0:
                is_col = True
                
            # Scan the rest of the row to set flags
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        
        # 2. Use the flags to update the inner matrix cells
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # 3. Update the first row based on matrix[0][0] flag
        if matrix[0][0] == 0:
            for c in range(cols):
                matrix[0][c] = 0

        # 4. Update the first column based on your is_col flag
        if is_col:
            for r in range(rows):
                matrix[r][0] = 0
