from typing import List


class Solution:
    """
    failed because of memory exceed
    using 1, 0 2 dim array approach is wrong
    """
    def trap(self, height: List[int]) -> int:
        w = len(height)
        h = max(height)
        n = [[0 for j in range(w)] for i in range(h)]
        visited = [[False for j in range(w)] for i in range(h)]
        ans = 0

        for i in range(w):
            for j in range(0, height[i]):
              n[h-1-j][i] = 1

        # for i in range(h):
        #     for j in range(w):
        #       # print(n[i][j], end='')
        #     print("")
        
        for row in range(h):
            for col in range(w):
                if n[row][col] == 0 and not visited[row][col]:
                    x = col
                    visited[row][x] = True
                    wall_l, wall_r = False, False
                    count = 1
                    
                    if x !=0 and n[row][x-1] == 1:
                        wall_l = True
                    
                    while x+1<w:
                        # print(x)
                        if n[row][x+1] == 1:
                            wall_r = True
                            break
                        visited[row][x+1] = True
                        count += 1
                        x+=1
                        

                    if wall_l and wall_r:
                        ans += count
        return ans

# height = [4,2,0,3,2,5]
height = [0,1,0,2,1,0,1,3,2,1,2,1]
sol = Solution()
print(sol.trap(height))