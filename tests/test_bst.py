from src.bst import BinarySearchTree


def test_insert_and_search():
    bst = BinarySearchTree()

    bst.insert(10, "A")
    bst.insert(5, "B")
    bst.insert(15, "C")

    node = bst.search(10)
    assert node is not None
    assert node.data == "A"

    node = bst.search(5)
    assert node is not None
    assert node.data == "B"

    node = bst.search(15)
    assert node is not None
    assert node.data == "C"


def test_search_not_found():
    bst = BinarySearchTree()

    bst.insert(10, "A")
    bst.insert(5, "B")

    node = bst.search(99)
    assert node is None


def test_root_assignment():
    bst = BinarySearchTree()
    assert bst.root is None

    bst.insert(1, "X")
    assert bst.root is not None
    assert bst.root.key == 1

def test_delete_node():
    bst = BinarySearchTree()
    bst.insert(10, "Raiz")
    bst.insert(5, "Esquerda")
    bst.insert(15, "Direita")
    
    # Remove um nó folha
    bst.delete(15)
    assert bst.search(15) is None
    
    # Remove o nó raiz (nó com filho)
    bst.delete(10)
    assert bst.search(10) is None
    assert bst.root.key == 5
