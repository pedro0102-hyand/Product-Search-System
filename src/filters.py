def filter_products(root, category = None, max_price = None, min_rating = None):
    
    # usar DFS para filtrar produtos na árvore

    if root is None:
        return []
    
    results =[]
    stack = [root]

    while stack:

        current = stack.pop()
        product = current.data #acessando dados do produto

        # lógica de filtro
        match = True

        # verifica se o user definiu uma categoria para filtrar
        if category and product.get("category") != category:
            match = False
        
        # verifica preco maximo
        if max_price and product.get("price") > max_price:
            match = False
        
        # verifica nota minima
        if min_rating and product.get("rating") < min_rating:
            match = False
        
        if match:
            results.append(product)

        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    
    return results
