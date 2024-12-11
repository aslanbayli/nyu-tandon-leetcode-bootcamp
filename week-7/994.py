class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh_oranges = 0
        rotten_queue = deque()
        
        # Count fresh oranges and add rotten ones to queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                elif grid[r][c] == 2:
                    rotten_queue.append((r, c))
        
        # If no fresh oranges, return 0
        if fresh_oranges == 0:
            return 0
            
        # Directions for 4-directional movement
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        minutes_passed = 0
        
        # BFS to simulate rotting process
        while rotten_queue and fresh_oranges > 0:
            minutes_passed += 1
            
            for _ in range(len(rotten_queue)):
                x, y = rotten_queue.popleft()
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    
                    # Check if neighboring cell is a fresh orange
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh_oranges -= 1
                        rotten_queue.append((nx, ny))
        
        # Return -1 if fresh oranges remain, otherwise return minutes passed
        return minutes_passed if fresh_oranges == 0 else -1
