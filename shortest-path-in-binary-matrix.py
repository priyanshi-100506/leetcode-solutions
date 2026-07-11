from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        
        # Check if the start or end cell is blocked
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
            
        # Single-cell matrix edge case
        if n == 1:
            return 1
            
        # 8-directional movements
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        
        queue = deque([(0, 0, 1)]) # (row, col, distance)
        grid[0][0] = 1 # Mark start cell as visited
        
        while queue:
            r, c, dist = queue.popleft()
            
            # Reached target destination
            if r == n - 1 and c == n - 1:
                return dist
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check boundaries and if the cell is open (0)
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1 # Mark as visited in-place
                    queue.append((nr, nc, dist + 1))
                    
        return -1
