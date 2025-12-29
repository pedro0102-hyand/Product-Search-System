from src.bst import BinarySearchTree
from src.dfs import dfs
from src.bfs import bfs
from src.dataset import generate_products
from src.filters import filter_products
import time


def main():
    # =========================
    # Configuração do experimento
    # =========================
    DATASET_SIZE = 15  # aumente para 10000, 20000, etc.

    print(f"📦 Gerando dataset com {DATASET_SIZE} produtos...")
    products = generate_products(DATASET_SIZE)

    # =========================
    # Construção da BST
    # =========================
    bst = BinarySearchTree()

    print("🌳 Inserindo produtos na BST...")
    start_insert = time.perf_counter()

    for product in products:
        bst.insert(product["id"], product)

    end_insert = time.perf_counter()
    print(f"⏱️ Tempo de inserção: {end_insert - start_insert:.4f}s\n")

    # =========================
    # DFS manual
    # =========================
    print("🔍 Executando DFS manual (pilha)...")
    start_dfs = time.perf_counter()

    dfs_result = dfs(bst.root)

    end_dfs = time.perf_counter()
    print(f"⏱️ Tempo DFS: {end_dfs - start_dfs:.4f}s")
    print(f"📊 Nós visitados (DFS): {len(dfs_result)}\n")

    # =========================
    # BFS manual
    # =========================
    print("🌊 Executando BFS manual (fila)...")
    start_bfs = time.perf_counter()

    bfs_result = bfs(bst.root)

    end_bfs = time.perf_counter()
    print(f"⏱️ Tempo BFS: {end_bfs - start_bfs:.4f}s")
    print(f"📊 Nós visitados (BFS): {len(bfs_result)}\n")

    # =========================
    # Busca pontual na BST
    # =========================
    search_id = products[len(products) // 2]["id"]
    print(f"🎯 Buscando produto com ID = {search_id}")

    node = bst.search(search_id)
    if node:
        print("✅ Produto encontrado:")
        print(node.data)
    else:
        print("❌ Produto não encontrado")
    

    print("\n🔍 Filtrando: Categoria 'Eletrônicos' com preço até R$ 500.00")
    cheap_electronics = filter_products(
        bst.root, 
        category="Eletrônicos", 
        max_price=500.0
    )

    print(f"📊 Encontrados: {len(cheap_electronics)} produtos")
    for p in cheap_electronics[:3]: # Mostra os 3 primeiros resultados
        print(f" - {p['name']}: R$ {p['price']} (Rating: {p['rating']})")


if __name__ == "__main__":
    main()
