class Node:
  def __init__(self,state,children = None):
    self.state = state
    self.children = children if children is not None else []
  
  def dfs(self,goal,path=None):
    if path is None:
      path = []
    path.append(self.state)
    if self.state == goal:
      return path
    for child in self.children:
      result = child.dfs(goal,path.copy())
      if result:
        return result
  
if __name__ == '__main__':
  node_h = Node('h')
  node_i = Node('i')
  node_j = Node('j')
  node_k = Node('k')
  node_g = Node('g')
  node_d = Node('d',[node_h])
  node_e = Node('e',[node_i,node_j])
  node_f = Node('f',[node_k])
  node_c = Node('c',[node_f,node_g])

  node_b = Node('b',[node_d,node_e])
  root = Node('a',[node_b,node_c])

  goal = 'e'
  path = root.dfs(goal)
  if path:
    print("path to goal","-->".join(path))
  else:
    print("Goal not found in the tree")
