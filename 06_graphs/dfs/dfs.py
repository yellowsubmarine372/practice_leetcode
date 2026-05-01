def dfsRec(adj, visited, s, res):
  visited[s] = True
  res.append(s)

  # **Recursively** visit all the adjacent vertices that are not visited yet
  for x in adj[s]:
    if not visited[x]:
      dfsRec(adj, visited, x, res)

def dfs(adj):
  # initialize
  visited = [False]*len(adj) #[False * len(adj)] -> [0]
  res = []
  dfsRec(adj, visited, 0, res)
  return res