# bfs for single connected component: starting from one node and traveling only nodes reachable from that source

from collections import deque


def bfs(adj):
  V = len(adj)
  visited = [False] * V
  res = []

  root = 0
  q = deque()
  visited[root] = True
  q.append(root)

  while q:
    curr = q.popleft()
    res.append(curr)

    # visit all the unvisited neighbours of current node
    for x in adj[curr]:
      if not visited[x]:
        visited[x] = True
        q.append(x)