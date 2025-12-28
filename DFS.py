def dfs(root):

    stack = [root] # comeca pela raiz
    visited = [] # lista de vértices visitados

    while stack :

        current = stack.pop()
        visited.append(current.key)

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)
    
    return visited

