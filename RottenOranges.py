from collections import deque
class Solution:
def orangesRotting(self, grid):
  rows, cols = len(grid), len(grid[0])
  fresh = 0  
  time = 0 
  q = deque()
  for r in range(rows):
    for c in range(cols):
      if grid[r][c] == 2:
        q.append((r,c))
      if grid[r][c] == 1:
        fresh += 1

  directions = [(-1,0), (1,0), (0,1), (0,-1)]
  while fresh > 0 and q: 
    for i in range(len(q)):
      r,c = q.popleft()
      for dr, dc in directions: 
        nr = r + dr
        nc = c + dc 
        if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == 1: 
          grid[nr][nc] == 2
          q.append((nr, nc))
          fresh -= 1 
    time += 1 

 return time
