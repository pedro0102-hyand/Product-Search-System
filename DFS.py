def dfs(root):

    stack = [root] # comeca pela raiz
    visited = [] # lista de vértices visitados

    while stack :

        # Remove do topo da Pilha e adiciona na lista de visitados
        current = stack.pop()
        visited.append(current.key)

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)
    
    return visited

