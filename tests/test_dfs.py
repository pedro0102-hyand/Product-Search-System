from src.bst import BinarySearchTree
from src.dfs import dfs


def build_sample_tree():
    """
    Árvore usada nos testes:

            10
           /  \
          5    15
         / \
        3   7
    """
    bst = BinarySearchTree()
    bst.insert(10, "A")
    bst.insert(5, "B")
    bst.insert(15, "C")
    bst.insert(3, "D")
    bst.insert(7, "E")
    return bst


def test_dfs_traversal():
    bst = build_sample_tree()

    result = dfs(bst.root)

    # DFS manual usando pilha (pré-ordem implícita)
    assert result == [10, 5, 3, 7, 15]


def test_dfs_empty_tree():
    result = dfs(None)
    assert result == []


def test_dfs_visits_all_nodes():
    bst = build_sample_tree()

    result = dfs(bst.root)

    # Garante que todos os nós foram visitados
    assert len(result) == 5
    assert set(result) == {10, 5, 3, 7, 15}
