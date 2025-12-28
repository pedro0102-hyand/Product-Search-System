from src.bst import BinarySearchTree
from src.filters import filter_products

def test_filter_by_category():
    bst = BinarySearchTree()
    bst.insert(1, {"category": "Eletrônicos", "price": 100, "rating": 5})
    bst.insert(2, {"category": "Roupas", "price": 50, "rating": 4})
    
    # Testa filtro de categoria
    result = filter_products(bst.root, category="Eletrônicos")
    assert len(result) == 1
    assert result[0]["category"] == "Eletrônicos"

def test_filter_by_price_and_rating():
    bst = BinarySearchTree()
    bst.insert(1, {"category": "Livros", "price": 200, "rating": 3.0})
    bst.insert(2, {"category": "Livros", "price": 50, "rating": 4.5})
    
    # Livros abaixo de 100 com rating min 4
    result = filter_products(bst.root, category="Livros", max_price=100, min_rating=4.0)
    assert len(result) == 1
    assert result[0]["price"] == 50