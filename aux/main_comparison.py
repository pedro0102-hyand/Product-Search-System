from src.bst import BinarySearchTree
from src.avl_tree import AVLTree
from src.dataset import generate_products
import time
import random


def measure_tree_performance(tree_class, products, name):
    """
    Mede o desempenho de uma árvore em diferentes operações.
    """
    print(f"\n{'='*60}")
    print(f"🌳 Testando: {name}")
    print(f"{'='*60}")
    
    tree = tree_class()
    
    # ========================================
    # INSERÇÃO
    # ========================================
    print(f"\n📥 Inserindo {len(products)} produtos...")
    start = time.perf_counter()
    
    for product in products:
        tree.insert(product["id"], product)
    
    insert_time = time.perf_counter() - start
    print(f"⏱️  Tempo de inserção: {insert_time:.4f}s")
    
    # Altura da árvore
    if hasattr(tree, 'get_height'):
        print(f"📏 Altura da árvore: {tree.get_height()}")
        print(f"🎯 Balanceada: {'✅ Sim' if tree.is_balanced() else '❌ Não'}")
        
        # Mostrar fator de balanceamento da raiz
        if tree.root:
            balance = tree.root.get_balance()
            print(f"⚖️  Balance da raiz: {balance:+d} (direita - esquerda)")
    
    # ========================================
    # BUSCA
    # ========================================
    print(f"\n🔍 Realizando 1000 buscas aleatórias...")
    
    search_keys = [random.choice(products)["id"] for _ in range(1000)]
    
    start = time.perf_counter()
    found = 0
    
    for key in search_keys:
        if tree.search(key):
            found += 1
    
    search_time = time.perf_counter() - start
    print(f"⏱️  Tempo total: {search_time:.4f}s")
    print(f"📊 Média por busca: {(search_time/1000)*1000:.4f}ms")
    print(f"✅ Encontrados: {found}/1000")
    
    # ========================================
    # REMOÇÃO
    # ========================================
    print(f"\n🗑️  Removendo 100 produtos aleatórios...")
    
    delete_keys = [random.choice(products)["id"] for _ in range(100)]
    
    start = time.perf_counter()
    
    for key in delete_keys:
        tree.delete(key)
    
    delete_time = time.perf_counter() - start
    print(f"⏱️  Tempo de remoção: {delete_time:.4f}s")
    
    if hasattr(tree, 'get_height'):
        print(f"📏 Altura após remoções: {tree.get_height()}")
        print(f"🎯 Ainda balanceada: {'✅ Sim' if tree.is_balanced() else '❌ Não'}")
    
    return {
        "name": name,
        "insert_time": insert_time,
        "search_time": search_time,
        "delete_time": delete_time,
        "height": tree.get_height() if hasattr(tree, 'get_height') else "N/A"
    }


def test_worst_case_scenario():
    """
    Testa o pior caso: inserção ordenada (crescente).
    BST vira uma lista encadeada, AVL mantém balanceamento.
    """
    print(f"\n{'='*60}")
    print("⚠️  TESTE DE PIOR CASO: Inserção Ordenada")
    print(f"{'='*60}")
    print("\n💡 Inserção ordenada crescente (1, 2, 3, ..., n)")
    print("   BST: Degenera em lista encadeada → O(n)")
    print("   AVL: Mantém balanceamento → O(log n)")
    
    # Usar n menor para BST não estourar recursão
    n = 500  # Reduzido de 1000 para evitar RecursionError
    ordered_products = [{"id": i, "name": f"Product {i}"} for i in range(n)]
    
    print(f"\n⚠️  Nota: Usando n={n} (Python tem limite de ~1000 recursões)")
    print(f"   Com n=1000, BST causaria RecursionError!")
    
    # ========================================
    # BST TRADICIONAL
    # ========================================
    print(f"\n{'─'*60}")
    print("📊 BST Tradicional com inserção ordenada:")
    print(f"{'─'*60}")
    bst = BinarySearchTree()
    
    try:
        start = time.perf_counter()
        for p in ordered_products:
            bst.insert(p["id"], p)
        bst_time = time.perf_counter() - start
        
        print(f"⏱️  Tempo de inserção: {bst_time:.4f}s")
        print(f"⚠️  Estrutura: Lista encadeada (todos à direita)")
        print(f"📏 Altura: ≈ {n} (cada nó só tem filho direito)")
        bst_success = True
    except RecursionError:
        print(f"❌ RecursionError! BST atingiu limite de recursão do Python")
        print(f"   Com inserção ordenada, BST precisa de {n} chamadas recursivas")
        print(f"   Python limita em ~1000 recursões por padrão")
        bst_success = False
        bst_time = float('inf')
    
    # ========================================
    # AVL TREE
    # ========================================
    print(f"\n{'─'*60}")
    print("📊 AVL Tree com inserção ordenada:")
    print(f"{'─'*60}")
    avl = AVLTree()
    
    start = time.perf_counter()
    for p in ordered_products:
        avl.insert(p["id"], p)
    avl_time = time.perf_counter() - start
    
    print(f"⏱️  Tempo de inserção: {avl_time:.4f}s")
    print(f"📏 Altura real: {avl.get_height()}")
    print(f"📐 Altura ideal: log₂({n}) ≈ {n.bit_length()}")
    print(f"🎯 Balanceada: {'✅ Sim' if avl.is_balanced() else '❌ Não'}")
    print(f"⚖️  Balance da raiz: {avl.root.get_balance():+d}")
    
    # ========================================
    # COMPARAÇÃO DE BUSCA
    # ========================================
    if bst_success:
        print(f"\n{'─'*60}")
        print("🔍 TESTE DE BUSCA - Elemento no final (pior caso)")
        print(f"{'─'*60}")
        
        # BST (pior caso O(n) - precisa percorrer toda a "lista")
        start = time.perf_counter()
        bst.search(n-1)
        bst_search = time.perf_counter() - start
        
        # AVL (sempre O(log n))
        start = time.perf_counter()
        avl.search(n-1)
        avl_search = time.perf_counter() - start
        
        print(f"  BST: {bst_search*1000:.6f}ms (O(n) - {n} comparações)")
        print(f"  AVL: {avl_search*1000:.6f}ms (O(log n) - ≈{n.bit_length()} comparações)")
        
        if bst_search > 0 and avl_search > 0:
            speedup = bst_search / avl_search
            print(f"  🚀 Speedup: {speedup:.2f}x mais rápido com AVL")
        
        # ========================================
        # BUSCAS MÚLTIPLAS
        # ========================================
        print(f"\n{'─'*60}")
        print("🔍 TESTE DE BUSCAS MÚLTIPLAS - 100 elementos aleatórios")
        print(f"{'─'*60}")
        
        test_keys = random.sample(range(n), 100)
        
        # BST
        start = time.perf_counter()
        for key in test_keys:
            bst.search(key)
        bst_multi = time.perf_counter() - start
        
        # AVL
        start = time.perf_counter()
        for key in test_keys:
            avl.search(key)
        avl_multi = time.perf_counter() - start
        
        print(f"  BST: {bst_multi*1000:.4f}ms")
        print(f"  AVL: {avl_multi*1000:.4f}ms")
        
        if bst_multi > 0 and avl_multi > 0:
            speedup = bst_multi / avl_multi
            print(f"  🚀 Speedup: {speedup:.2f}x mais rápido com AVL")
            improvement = ((bst_multi - avl_multi) / bst_multi) * 100
            print(f"  📈 Melhoria: {improvement:.1f}%")
    else:
        print(f"\n{'─'*60}")
        print("⚠️  Testes de busca cancelados (BST falhou na inserção)")
        print(f"{'─'*60}")
        print("\n💡 Este é exatamente o problema que AVL resolve!")
        print(f"   Com n={n}, BST já falha. AVL funciona perfeitamente!")
        print(f"   AVL pode lidar com milhões de inserções ordenadas.")


def explain_balance_factor():
    """
    Explica o conceito de fator de balanceamento com exemplos visuais.
    """
    print(f"\n{'='*60}")
    print("📚 ENTENDENDO O FATOR DE BALANCEAMENTO")
    print(f"{'='*60}")
    
    print("\n🔢 Fórmula: Balance = altura_direita - altura_esquerda")
    print("\n📊 Interpretação:")
    print("   Balance =  0  → Perfeitamente balanceado ✅")
    print("   Balance = +1  → Direita um pouco maior (OK) ✅")
    print("   Balance = -1  → Esquerda um pouco maior (OK) ✅")
    print("   Balance = +2  → Direita muito maior (ROTAÇÃO!) ⚠️")
    print("   Balance = -2  → Esquerda muito maior (ROTAÇÃO!) ⚠️")
    
    print(f"\n{'─'*60}")
    print("Exemplo 1: Árvore Balanceada")
    print(f"{'─'*60}")
    print("""
        10 (balance=0)
       /  \\
      5    15
    
    altura_esquerda = 1, altura_direita = 1
    balance = 1 - 1 = 0 ✅
    """)
    
    print(f"{'─'*60}")
    print("Exemplo 2: Desbalanceada à Direita (RR)")
    print(f"{'─'*60}")
    print("""
        10 (balance=+2) ⚠️
         \\
          15
           \\
            20
    
    altura_esquerda = 0, altura_direita = 2
    balance = 2 - 0 = +2
    Solução: Rotação ESQUERDA
    """)
    
    print(f"{'─'*60}")
    print("Exemplo 3: Desbalanceada à Esquerda (LL)")
    print(f"{'─'*60}")
    print("""
          10 (balance=-2) ⚠️
         /
        5
       /
      3
    
    altura_esquerda = 2, altura_direita = 0
    balance = 0 - 2 = -2
    Solução: Rotação DIREITA
    """)


def main():
    print("🚀 Comparação: BST vs AVL Tree")
    print("=" * 60)
    
    # Explicar fator de balanceamento
    explain_balance_factor()
    
    # Dataset aleatório (caso médio)
    DATASET_SIZE = 5000
    print(f"\n{'='*60}")
    print(f"📦 Gerando dataset com {DATASET_SIZE} produtos (IDs aleatórios)...")
    print(f"{'='*60}")
    products = generate_products(DATASET_SIZE)
    
    # Testar ambas as árvores
    results = []
    
    results.append(measure_tree_performance(
        BinarySearchTree, 
        products, 
        "BST Tradicional (Não Balanceada)"
    ))
    
    results.append(measure_tree_performance(
        AVLTree, 
        products, 
        "AVL Tree (Auto-Balanceada)"
    ))
    
    # Resumo comparativo
    print(f"\n{'='*60}")
    print("📊 RESUMO COMPARATIVO - Dados Aleatórios")
    print(f"{'='*60}")
    
    for result in results:
        print(f"\n{result['name']}:")
        print(f"  Inserção:  {result['insert_time']:.4f}s")
        print(f"  Busca:     {result['search_time']:.4f}s")
        print(f"  Remoção:   {result['delete_time']:.4f}s")
        print(f"  Altura:    {result['height']}")
    
    # Comparação percentual
    if len(results) == 2:
        print(f"\n{'='*60}")
        print("📈 DIFERENÇA PERCENTUAL (AVL vs BST)")
        print(f"{'='*60}")
        
        bst_result = results[0]
        avl_result = results[1]
        
        insert_diff = ((avl_result['insert_time'] - bst_result['insert_time']) / bst_result['insert_time']) * 100
        search_diff = ((avl_result['search_time'] - bst_result['search_time']) / bst_result['search_time']) * 100
        delete_diff = ((avl_result['delete_time'] - bst_result['delete_time']) / bst_result['delete_time']) * 100
        
        print(f"\nInserção: {insert_diff:+.2f}% (AVL {'mais lenta' if insert_diff > 0 else 'mais rápida'})")
        print(f"Busca:    {search_diff:+.2f}% (AVL {'mais lenta' if search_diff > 0 else 'mais rápida'})")
        print(f"Remoção:  {delete_diff:+.2f}% (AVL {'mais lenta' if delete_diff > 0 else 'mais rápida'})")
    
    # Teste do pior caso
    test_worst_case_scenario()
    
    print(f"\n{'='*60}")
    print("✅ Testes concluídos!")
    print(f"{'='*60}")
    print("\n💡 Conclusões:")
    print("   1. AVL garante O(log n) SEMPRE, mesmo no pior caso")
    print("   2. BST pode degenerar para O(n) com inserção ordenada")
    print("   3. AVL tem overhead nas rotações durante inserção")
    print("   4. AVL compensa MUITO em buscas frequentes")
    print("   5. Com dados aleatórios, diferença é menor")
    print("   6. Use AVL quando:")
    print("      - Não controla ordem de inserção")
    print("      - Busca é operação mais frequente")
    print("      - Precisa garantias de performance")


if __name__ == "__main__":
    main()