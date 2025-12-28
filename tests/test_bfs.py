from src.bst import BinarySearchTree
from src.bfs import bfs


def build_sample_tree():
    bst = BinarySearchTree()
    bst.insert(10, "A")
    bst.insert(5, "B")
    bst.insert(15, "C")
    bst.insert(3, "D")
    bst.insert(7, "E")
    return bst


def test_bfs_traversal():
    bst = build_sample_tree()

    result = bfs(bst.root)

    # Ordem esperada por nível
    assert result == [10, 5, 15, 3, 7]


def test_bfs_empty_tree():
    result = bfs(None)
    assert result == []
