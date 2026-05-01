class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.length = len(grid[0])
        self.height = len(grid)
        self.visited = [[False for _ in range(self.length)] for _ in range(self.height)]
        
        def dfs(i, j, grid):
            self.visited[i][j] = True
            if (j-1) >=0 and grid[i][j-1] == "1" and not self.visited[i][j-1]:
                dfs(i, j-1, grid)
            if (j+1) < self.length and grid[i][j+1] == "1" and not self.visited[i][j+1]:
                dfs(i, j+1, grid)
            if (i-1) >=0 and grid[i-1][j] == "1" and not self.visited[i-1][j]:
                dfs(i-1, j, grid)
            if (i+1) < self.height and grid[i+1][j] == "1" and not self.visited[i+1][j]:
                dfs(i+1, j, grid)
            return
        
        res = 0
        
        for i in range(self.height):
            for j in range(self.length):
                if not self.visited[i][j] and grid[i][j] == "1":
                    dfs(i, j, grid)
                    res += 1

        return res