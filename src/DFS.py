def dfs(root):

    if root is None:
        return []

    stack = [root]
    visited = []

    while stack:
        current = stack.pop()      # remove do topo da pilha
        visited.append(current.key)

        # primeiro o filho direito, depois o esquerdo
        # para que o esquerdo seja processado primeiro
        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)

    return visited


