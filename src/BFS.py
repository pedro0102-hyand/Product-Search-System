from collections import deque

def bfs(root):

    if root is None:
        return []
    
    queue = deque([root]) # raiz no inicio da fila
    visited = []

    while queue:

        # remove do inicio da fila e adiciona na lista de visitados
        current = queue.popleft()
        visited.append(current.key)

        if current.left:
            queue.append(current.left)
        
        if current.right:
            queue.append(current.right)

    return visited

