import pytest
from src.avl_tree import AVLTree


def test_avl_insert_and_search():

    avl = AVLTree()
    
    avl.insert(10, "A")
    avl.insert(5, "B")
    avl.insert(15, "C")
    
    assert avl.search(10).data == "A"
    assert avl.search(5).data == "B"
    assert avl.search(15).data == "C"
    assert avl.search(99) is None


def test_avl_left_left_case():
  
    avl = AVLTree()
    
    avl.insert(3, "C")
    avl.insert(2, "B")
    avl.insert(1, "A")  # Deve causar rotação direita
    
    # Verificar estrutura
    assert avl.root.key == 2
    assert avl.root.left.key == 1
    assert avl.root.right.key == 3
    
    # Verificar balanceamento
    assert avl.is_balanced()
    assert avl.get_height() == 2


def test_avl_right_right_case():
   
    avl = AVLTree()
    
    avl.insert(1, "A")
    avl.insert(2, "B")
    avl.insert(3, "C")  # Deve causar rotação esquerda
    
    # Verificar estrutura
    assert avl.root.key == 2
    assert avl.root.left.key == 1
    assert avl.root.right.key == 3
    
    assert avl.is_balanced()
    assert avl.get_height() == 2


def test_avl_left_right_case():

    avl = AVLTree()
    
    avl.insert(3, "C")
    avl.insert(1, "A")
    avl.insert(2, "B")  # Deve causar rotação dupla
    
    assert avl.root.key == 2
    assert avl.root.left.key == 1
    assert avl.root.right.key == 3
    assert avl.is_balanced()


def test_avl_right_left_case():
 
    avl = AVLTree()
    
    avl.insert(1, "A")
    avl.insert(3, "C")
    avl.insert(2, "B")  # Deve causar rotação dupla
    
    assert avl.root.key == 2
    assert avl.root.left.key == 1
    assert avl.root.right.key == 3
    assert avl.is_balanced()


def test_avl_maintains_balance_on_many_insertions():

    avl = AVLTree()
    
    # Inserir valores em ordem crescente (pior caso para BST)
    for i in range(1, 100):
        avl.insert(i, f"Data{i}")
    
    # AVL deve manter balanceamento
    assert avl.is_balanced()
    
    # Altura deve ser logarítmica
    # log₂(99) ≈ 6.6, então altura deve ser <= 10
    assert avl.get_height() <= 10


def test_avl_delete_leaf():

    avl = AVLTree()
    
    avl.insert(10, "A")
    avl.insert(5, "B")
    avl.insert(15, "C")
    
    avl.delete(5)
    
    assert avl.search(5) is None
    assert avl.search(10) is not None
    assert avl.is_balanced()


def test_avl_delete_with_one_child():

    avl = AVLTree()
    
    avl.insert(10, "A")
    avl.insert(5, "B")
    avl.insert(3, "C")
    
    avl.delete(5)
    
    assert avl.search(5) is None
    assert avl.search(3) is not None
    assert avl.is_balanced()


def test_avl_delete_with_two_children():

    avl = AVLTree()
    
    avl.insert(10, "A")
    avl.insert(5, "B")
    avl.insert(15, "C")
    avl.insert(3, "D")
    avl.insert(7, "E")
    
    avl.delete(5)
    
    assert avl.search(5) is None
    assert avl.search(3) is not None
    assert avl.search(7) is not None
    assert avl.is_balanced()


def test_avl_delete_root():

    avl = AVLTree()
    
    avl.insert(10, "A")
    avl.insert(5, "B")
    avl.insert(15, "C")
    
    avl.delete(10)
    
    assert avl.search(10) is None
    assert avl.root.key != 10
    assert avl.is_balanced()


def test_avl_maintains_balance_after_deletions():

    avl = AVLTree()
    
    # Inserir
    for i in range(1, 20):
        avl.insert(i, f"Data{i}")
    
    # Remover metade
    for i in range(1, 10):
        avl.delete(i)
    
    # Deve ainda estar balanceada
    assert avl.is_balanced()


def test_avl_height_vs_bst():
 
    from src.bst import BinarySearchTree
    
    # BST com inserção ordenada (pior caso)
    bst = BinarySearchTree()
    for i in range(1, 50):
        bst.insert(i, f"Data{i}")
    
    # AVL com mesma inserção
    avl = AVLTree()
    for i in range(1, 50):
        avl.insert(i, f"Data{i}")
    
    # AVL deve ter altura muito menor
    assert avl.get_height() <= 8  # log₂(50) ≈ 5.6
    # BST provavelmente tem altura ~50 (lista encadeada)
    
    assert avl.is_balanced()


def test_avl_duplicate_key():

    avl = AVLTree()
    
    avl.insert(10, "Original")
    avl.insert(10, "Atualizado")
    
    node = avl.search(10)
    assert node.data == "Atualizado"


def test_avl_empty_tree():

    avl = AVLTree()
    
    assert avl.root is None
    assert avl.get_height() == 0
    assert avl.search(10) is None
    assert avl.is_balanced()


def test_balance_factor_calculation():
  
    avl = AVLTree()
    
    # Árvore balanceada
    avl.insert(10, "Root")
    avl.insert(5, "Left")
    avl.insert(15, "Right")
    
    # Raiz deve ter balance = 0 (ambos os lados altura 1)
    assert avl.root.get_balance() == 0
    
    # Adicionar mais à direita
    avl.insert(20, "RightRight")
    avl.insert(25, "RightRightRight")
    
    # Após rebalanceamento, árvore deve estar balanceada
    assert avl.is_balanced()
    assert abs(avl.root.get_balance()) <= 1


def test_complex_sequence():
  
    avl = AVLTree()
    
    # Sequência que causa múltiplas rotações
    keys = [50, 25, 75, 10, 30, 60, 80, 5, 15, 27, 55, 65]
    
    for key in keys:
        avl.insert(key, f"Data{key}")
        assert avl.is_balanced(), f"Árvore desbalanceada após inserir {key}"
    
    # Remover alguns nós
    for key in [10, 30, 60]:
        avl.delete(key)
        assert avl.is_balanced(), f"Árvore desbalanceada após remover {key}"
    
    # Verificar que os outros nós ainda estão lá
    for key in [50, 25, 75, 5, 15, 27, 55, 65, 80]:
        assert avl.search(key) is not None